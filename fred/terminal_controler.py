#
# Copyright (C) 2006-2021  CZ.NIC, z. s. p. o.
#
# This file is part of FRED.
#
# FRED is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# FRED is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with FRED.  If not, see <https://www.gnu.org/licenses/>.
#
from __future__ import unicode_literals

from builtins import object, range, zip
import re
import sys

import six

from .translate import encoding


class TerminalController(object):
    """
    A class that can be used to portably generate formatted output to
    a terminal.

    `TerminalController` defines a set of instance variables whose
    values are initialized to the control sequence necessary to
    perform a given action.  These can be simply included in normal
    output to the terminal:

        >>> term = TerminalController()
        >>> print 'This is '+term.GREEN+'green'+term.NORMAL

    Alternatively, the `render()` method can used, which replaces
    '${action}' with the string required to perform 'action':

        >>> term = TerminalController()
        >>> print term.render('This is ${GREEN}green${NORMAL}')

    If the terminal doesn't support a given action, then the value of
    the corresponding instance variable will be set to ''.  As a
    result, the above code will still work on terminals that do not
    support color, except that their output will not be colored.
    Also, this means that you can test whether the terminal supports a
    given action by simply testing the truth value of the
    corresponding instance variable:

        >>> term = TerminalController()
        >>> if term.CLEAR_SCREEN:
        ...     print 'This terminal supports clearning the screen.'

    Finally, if the width and height of the terminal are known, then
    they will be stored in the `COLS` and `LINES` attributes.
    """
    # Cursor movement:
    BOL = b''            #: Move the cursor to the beginning of the line
    UP = b''             #: Move the cursor up one line
    DOWN = b''           #: Move the cursor down one line
    LEFT = b''           #: Move the cursor left one char
    RIGHT = b''          #: Move the cursor right one char

    # Deletion:
    CLEAR_SCREEN = b''   #: Clear the screen and move to home position
    CLEAR_EOL = b''      #: Clear to the end of the line.
    CLEAR_BOL = b''      #: Clear to the beginning of the line.
    CLEAR_EOS = b''      #: Clear to the end of the screen

    # Output modes:
    BOLD = b''           #: Turn on bold mode
    BLINK = b''          #: Turn on blink mode
    DIM = b''            #: Turn on half-bright mode
    REVERSE = b''        #: Turn on reverse-video mode
    NORMAL = b''         #: Turn off all modes

    # Cursor display:
    HIDE_CURSOR = b''    #: Make the cursor invisible
    SHOW_CURSOR = b''    #: Make the cursor visible

    # Terminal size:
    COLS = None          #: Width of the terminal (None for unknown)
    LINES = None         #: Height of the terminal (None for unknown)

    # Foreground colors:
    BLACK = BLUE = GREEN = CYAN = RED = MAGENTA = YELLOW = WHITE = b''

    # Background colors:
    BG_BLACK = BG_BLUE = BG_GREEN = BG_CYAN = b''
    BG_RED = BG_MAGENTA = BG_YELLOW = BG_WHITE = b''

    _STRING_CAPABILITIES = """
    BOL=cr UP=cuu1 DOWN=cud1 LEFT=cub1 RIGHT=cuf1
    CLEAR_SCREEN=clear CLEAR_EOL=el CLEAR_BOL=el1 CLEAR_EOS=ed BOLD=bold
    BLINK=blink DIM=dim REVERSE=rev UNDERLINE=smul NORMAL=sgr0
    HIDE_CURSOR=cinvis SHOW_CURSOR=cnorm""".split()
    _COLORS = """BLACK BLUE GREEN CYAN RED MAGENTA YELLOW WHITE""".split()
    _ANSICOLORS = "BLACK RED GREEN YELLOW BLUE MAGENTA CYAN WHITE".split()
    TERM_SHORTCUTS = '   \\\\\\\n   /";"\\ \n ,_/c c\\_.\n    |.|\n    \\|/\n   // \\\\\n   "\' \'"\n , /";"\\ ,\n  \\/c c\\/\n    |.|\n  ,<";">,\n    |.|\n ,_/c c\\_,\n   /c c\\\n ,/ |.| \\,\n    \\|/\n   /\';\'\\\n   /c c\\\n   \\|.|/\n   /c c\\\n   \\|.|/\n ,/\\|.|/\\,\n //\\_v_/\\\\\n"\'       \'"\n'

    def __init__(self, term_stream=sys.stdout):
        """
        Create a `TerminalController` and initialize its attributes
        with appropriate values for the current terminal.
        `term_stream` is the stream that will be used for terminal
        output; if this stream is not a tty, then the terminal is
        assumed to be a dumb terminal (i.e., have no capabilities).
        """
        self._is_mode_color = 0

        # Curses isn't available on all platforms
        try: import curses
        except: return

        # If the stream isn't a tty, then assume it has no capabilities.
        if not hasattr(term_stream, "isatty"):
            return
        if not term_stream.isatty():
            return

        # Check the terminal type.  If we fail, then assume that the
        # terminal has no capabilities.
        try: curses.setupterm()
        except: return

        # Look up numeric capabilities.
        self.COLS = curses.tigetnum('cols')
        self.LINES = curses.tigetnum('lines')

        # Look up string capabilities.
        for capability in self._STRING_CAPABILITIES:
            (attrib, cap_name) = capability.split('=')
            setattr(self, attrib, self._tigetstr(cap_name) or '')

        # Colors
        set_fg = self._tigetstr('setf')
        if set_fg:
            for i, color in enumerate(self._COLORS):
                setattr(self, color, curses.tparm(set_fg, i) or '')
        set_fg_ansi = self._tigetstr('setaf')
        if set_fg_ansi:
            for i, color in enumerate(self._ANSICOLORS):
                setattr(self, color, curses.tparm(set_fg_ansi, i) or '')
        set_bg = self._tigetstr('setb')
        if set_bg:
            for i, color in enumerate(self._COLORS):
                setattr(self, 'BG_' + color, curses.tparm(set_bg, i) or '')
        set_bg_ansi = self._tigetstr('setab')
        if set_bg_ansi:
            for i, color in enumerate(self._ANSICOLORS):
                setattr(self, 'BG_' + color, curses.tparm(set_bg_ansi, i) or '')

    def _tigetstr(self, cap_name):
        # String capabilities can include "delays" of the form "$<2>".
        # For any modern terminal, we should be able to just ignore
        # these, so strip them out.
        import curses
        return curses.tigetstr(cap_name) or ''

    def render(self, template):
        """
        Replace each $-substitutions in the given template string with
        the corresponding terminal control string (if it's defined) or
        '' (if it's not).
        """
        if isinstance(template, six.text_type):
            template = template.encode(encoding)
        return re.sub(rb'\$\$|\${\w+}', (b'', self._render_sub)[self._is_mode_color], template)

    def _render_sub(self, match):
        s = match.group()
        if s == b'$$': return s
        else: return getattr(self, s[2:-1].decode(encoding))

    def set_mode(self, mode):
        "Set color or not: mode=0/1."
        if type(mode) is not int: mode = (0, 1)[mode != '']
        self._is_mode_color = mode

    def get_term_vers(self):
        return '\x6d\x65\x20\x6d\x79\x20\x73\x77\x65\x65\x74\x20\x68\x6f\x6e\x65\x79'

supported_versions = ('1,0;1,1;1,2;1,1;1,2;1,1;1,3;2,4;1,5;1,6;3,4;1,6;2,4;1,7;1,8;1,9;3,8;3,10;1,11;4,10;1,11;4,10;6,4',
    '0,1,2,3,4,5,6;0,7,8,9,4,5,6;0,10,8,11,4,5,6;0,1,12,9,4,5,6;0,1,13,14,4,5,6;0,1,13,14,15,5,6;0,16,13,14,4,5,6;0,1,17,18,4,5,6;0,1,13,18,4,5,6;0,1,19,20,4,5,6;0,1,13,21,22,23,24;0,16,13,21,22,23,24')

#######################################################################
# Example use case: progress bar
#######################################################################

class ProgressBar(object):
    """
    A 3-line progress bar, which looks like::

                                Header
        20% [===========----------------------------------]
                           progress message

    The progress bar is colored, if the terminal supports color
    output; and adjusts to the width of the terminal.
    """
    BAR = '%3d%% ${GREEN}[${BOLD}%s%s${NORMAL}${GREEN}]${NORMAL}\n'
    HEADER = '${BOLD}${CYAN}%s${NORMAL}\n\n'

    def __init__(self, term, header):
        self.term = term
        if not (self.term.CLEAR_EOL and self.term.UP and self.term.BOL):
            raise ValueError("Terminal isn't capable enough -- you "
                             "should use a simpler progress display.")
        self.width = self.term.COLS or 75
        self.bar = term.render(self.BAR)
        self.header = self.term.render(self.HEADER % header.center(self.width))
        self.cleared = 1 #: true if we haven't drawn the bar yet.
        # self.update(0, '')

    def update(self, percent, message):
        if self.cleared:
            sys.stdout.write(self.header)
            self.cleared = 0
        n = int((self.width - 10) * percent)
        sys.stdout.write(
            self.term.BOL + self.term.UP + self.term.CLEAR_EOL +
            (self.bar % (100 * percent, '=' * n, '-' * (self.width - 10 - n))) +
            self.term.CLEAR_EOL + message.center(self.width))

    def clear(self):
        if not self.cleared:
            sys.stdout.write(self.term.BOL + self.term.CLEAR_EOL +
                             self.term.UP + self.term.CLEAR_EOL +
                             self.term.UP + self.term.CLEAR_EOL)
            self.cleared = 1
