# -*- coding: utf8 -*-
#!/usr/bin/env python
import re, random, math
import dircache # jen pro testování. v ostré verzi to nebude

import eppdoc
import eppdoc_client
import translate

from session_base import *
from session_transfer import ManagerTransfer, human_readable

from eppdoc import nic_cz_version as eppdoc_nic_cz_version

COLOR = 1
SEPARATOR = '-'*60
OPTIONAL,REQUIRED = range(2)

def __find_index__(array, key):
    index=-1
    for n in range(len(array)):
        if array[n][0][0] == key:
            index = n
            break
    return index


class ManagerCommand(ManagerTransfer):
    """EPP client support.
    This class manage creations of the EPP documents.
    """

    def __init__(self):
        ManagerTransfer.__init__(self)
        self.init_session_commands()
        # output
        #index = __find_index__(self._session_commands, 'output')
        #if index != -1: self._session_commands[index][3].extend(OUTPUT_TYPES)
        # Here is definition of commands  what will not be displayed in the help
        # because we don't make panic to common user.
        # They are used for test or debug only.
        self._hidden_commands = ('answer-cols','hidden','colors','config','null_value','raw-command','raw-answer','send','output')
        self._pattern_session_commands = [] # for recognize command
        self._available_session_commands = [] # for display list of command names
        for n,f,r,p,e,x in self._session_commands:
            if n[0] not in self._hidden_commands:
                self._available_session_commands.append(n[0])
            self._pattern_session_commands.extend(n)
        self.readline_words = [i for i in self._available_session_commands if i!='!'] + self._available_commands

    def init_session_commands(self):
        'Returns tuple of the session commands.'
        # SESSION_COMMANDS: (
        #   (command_name,command_name,command_name)
        #   function
        #   (parameter, parameter)   parameter: (req/opt, name, description, available)
        #   'Description'
        #   (example, example)
        # )
        self._session_commands = (
            (('!',), None, REQUIRED, (_T('command'),_T('Start interactive input mode on this command')), _T("""
! starts interactive input mode. In interactive input mode the program asks
to fill in all command parameters one by one to help users construct proper
syntax. After going through all parameters actual command syntax is displayed
before issuing command to server. 

Interactive mode can be used with EPP commands only."""), ('!create_domain',)),
            (('poll_autoack',), self.__session_poll_ack__, OPTIONAL, (_T('switch'),_T('Turn function on/off.')), _T('Send "poll ack" straight away after "poll req".'), ('poll-autoack on',)),
            (('colors',), self.__session_colors__, OPTIONAL, (_T('switch'),_T('Turn function on/off.')), _T('Turn on/off colored output.'), ('colors on',)),
            (('config',), self.manage_config, OPTIONAL, (), _T('Display or create config file.'), ('config',)),
            (('confirm',), self.__session_confirm__, OPTIONAL, (_T('switch'),_T('Turn function on/off.')), _T('Set on/off command confirmation for sending editable commands to the server.'), ('confirm off',)),
            #(('connect',), self.__session_connect__, OPTIONAL, (), _T('Make connection between client and server without login.'), ()),
            #(('disconnect',), self.__session_disconnect__, OPTIONAL, (), _T('Disconnect from the EPP server.'), ()),
            (('credits',), self.__session_credits__, OPTIONAL, (), _T('Display credits.'), ()),
            (('help','h','?'), None, OPTIONAL, (_T('command'),_T('Get detailed help for this command.')), _T("""
Help displays all available commands (type 'help') or displays 
detailed help for selected command (type 'help command'). 
Help uses synonyms 'help', '?' or 'h'."""), ('help','? update_nsset')),
            (('lang',), self.__session_language__, OPTIONAL, (_T('code'),_T('Set user interface language.')), _T("""
Set the client language and server together. If you are online 
and want to change the server language too, you have to logout 
and login again. Language is also possible to change by 'login'
command or specify in configuration file or set in options on
the command line."""), ('lang cs',)),
            (('license',), self.__session_license__, OPTIONAL, (), _T('Displays license terms of this application.'), ()),
            (('null_value','null'), self.__session_null__, OPTIONAL, (), _T("""
Set representation of the value what is used to mean nothing. Default is NULL.
This value we use if we want to skip over any column in the command parameters. 
Type NULL means we did not put any value in contrast to '' or "" where we put
value of zero length. Synonym of the 'null_value' is 'null'. 
See help for more details."""), ('null_value None','null EMPTY',)),
            (('output',), self.__session_output__, OPTIONAL, (_T('type'),_T('Set the output type.')), _T('Display output in type.'), ('output html',)),
            (('quit','q','exit'), None, OPTIONAL, (), _T("""
Disconnects from the server and exits the application. Synonyms 'q' and 'exit'
can be used to invoke same functionality."""), ()),
            (('raw-answer','raw-a','src-answer','src-a'), self.__session_raw_answer__, OPTIONAL, (_T('mode'),_T('Define display mode. XML (default) or DICT (dict or d).')), _T("""
Display XML source of the EPP answer. If you would display source
without XML tag, type parametr 'dict' or simple 'd'.
Synonyms of 'raw-answer' are 'raw-a', 'src-answer' and 'src-a'."""), ('raw-a','raw-a d','src-a','src-a d')),
            (('raw-command','raw-c','src-command','src-c'), self.__session_raw_command__, 0, (_T('mode'),_T('Define display mode. XML (default) or DICT (dict or d).')), _T("""
Display XML source of the EPP command. If you would display source
without XML tag, type parametr 'dict' or simple 'd'.
Synonyms of 'raw-command' are 'raw-c', 'src-command' and 'src-c'."""), ('raw-c','raw-c d','src-c','src-c d')),
            (('send',), self.__session_send__, REQUIRED, (_T('filename'),_T('any filename'),), _T('Send any file to the server. If filename missing command shows actual folder.'), ('send mydoc.xml',)),
            (('validate',), self.__session_validate__, OPTIONAL, (_T('switch'),_T('Turn validation on/off.')), _T("""
Client doesn't check command parameters itself. It uses for that external application
'xmllint' whats checks all parameters against to schema defined in XML specification.
Switch turns validations ON or OFF. Default is ON. If xmllint is not present 
validation is turned off automaticly."""), ('validate off',)),
            (('verbose',), self.__session_verbose__, OPTIONAL, (_T('level'),_T('Set verbose level. Available levels are 1, 2, 3.')), _T("""
Client displays various informations. They are disparted to verbose levels.
First verbose level (default) is designed to common user and give the output
at the minimum has needed to work with. For inquiring users is aimed second
level where are output all occured messages. The third level displays XML 
sources ad advance, transmited between client and server.

    Verbose modes: 

    1 - brief (default)
    2 - full
    3 - full & XML sources"""), ('verbose 2',)),
        )
        
    def __put_raw_into_note__(self, data):
        "Use pprint for displaying structured data (dict, XML-EPP)."
        if data is None:
            self.append_note(_T('No data'),('RED','BOLD'))
        elif type(data) == dict:
            # Parsed data into dict
            self.append_note(eppdoc.prepare_display(data,COLOR))
        else:
            # XML EPP doc. only for better display
            edoc = eppdoc_client.Message()
            edoc.parse_xml(data)
            if edoc.is_error():
                self.append_note(data,'GREEN') # při parsování se vyskytly chyby
            else:
                self.append_note(edoc.get_xml(),'GREEN')

    def __parse_command_params__(self, command_name, cmdline, interactive=None):
        "Check if parameters are valid. Params save into dict for use to assembling EPP document."
        errors, example, stop = self._epp_cmd.parse_cmd(command_name, cmdline, self._conf, interactive, self._session[VERBOSE], self._session[NULL_VALUE])
        if errors:
            self._errors.extend(errors)
            self._notes_afrer_errors.append(_T("Type '%s' for more information.")%'help %s'%command_name.encode(translate.encoding))
        if example: self.append_note('${BOLD}%s:${NORMAL}\n%s'%(_T('Command to issue'),example.encode(translate.encoding)))
        return (len(errors) == 0), stop

    def get_default_params_from_config(self, command_name):
        'Returns dict with default parameters from config.'
        return self._epp_cmd.get_default_params_from_config(self._conf, command_name)
    
    #==================================================
    #
    # main creation command functions
    #
    #==================================================
    def display_help(self, command_name, command):
        'Display help (build for display)'
        if command_name:
            # help command
            type = ''
            if command_name in self._pattern_session_commands:
                type = 'session'
            else:
                command_name = command_name.replace('-','_')
                if command_name in self._available_commands:
                    type = 'EPP'
            if type:
                parts = command.split()
                if len(parts) > 2:
                    # no parameters are alowed: '?','command'
                    self.append_note('%s: %s'%(_T('ERROR'), _T('Help command can have only one parameter')))
                    self.append_note(_T("Type 'help ?' to get more information about help usage."))
                else:
                    self.__make_help_details__(command_name, type)
            else:
                self.append_note('%s: %s'%(_T('No help available for'),command_name))
                self.__display_help__(command)
        else:
            # help content
            self.append_note('%s\n\n${BOLD}%s:${NORMAL}\n%s\n\n${BOLD}%s:${NORMAL}\n%s\n\n%s %s'%(
            _T('Type "help command" to get details of the chosen command.'),
            _T('Available session commands'),
            __make_help_columns__(self._available_session_commands, 2.0, self._indent_left),
            _T('Available EPP commands'),
            __make_help_columns__(self._available_commands, 3.0, self._indent_left),
            _T('Report bugs to'), self._email_reports_bug
            ))

    def __get_help_session_detail__(self, command_name):
        'Returns set of details of the session command.'
        command_help = notice = ''
        examples = ()
        command_lines = []
        space = ' '*self._indent_left
        for names,func,required,params,explain,ex in self._session_commands:
            if command_name in names:
                notice = explain
                examples = ex
                options = ''
                #if len(names)>1:
                #    command_line += ' (${BOLD}%s:${NORMAL} %s)'%(_T('synonyms'),', '.join(names[1:]))
                # params: (name, description)
                if len(params):
                    if required:
##                        options = ' %s'%' '.join(params[:required])
##                        if len(params)-1 > required: # -1 because first item is param name
##                            options += ' [%s]'%_T('optional')
                        options = ' %s'%params[0]
                    else:
                        options = ' [%s]'%params[0]
                    name = ('%s%s:'%(space,params[0])).ljust(self._ljust+3) # bracket and space '(required) '
##                    command_help = '%s%s'%(name,', '.join(params[1:]))
                    command_help = '%s%s'%(name,params[1])
                command_lines = map(lambda name: '%s%s'%(name,options), names)
                break
        return command_lines, command_help, notice, examples

    def __repalce_static_null_examples__(self, examples):
        'Replace static NULL examples to defined variable NULL_VALUE'
        if self._session[NULL_VALUE] != 'NULL':
            ex = []
            for e in examples:
                ex.append(re.sub('NULL',self._session[NULL_VALUE],e))
        else:
            ex = examples
        return ex

    def __format_help_detail__(self, lines):
        'Format lines with left intentation.'
        space = ' '*self._indent_left
        if type(lines) not in (list, tuple): lines = lines.split('\n')
        if type(lines) is list: lines = list(lines)
        if len(lines):
            if lines[0]=='': lines.pop(0) # remove blank line on the top
            if lines[-1]=='': lines.pop() # remove blank line at the end
        indentation = map(lambda s: '%s%s'%(space,s), lines)
        return '\n'.join(indentation)
        
    def __make_help_details__(self, command_name, type):
        "Make help for chosen command."
        if command_name:
            m = re.match('(\S+)', command_name)
            if m:command_name = m.group(1)
        if command_name:
            # s parametrem - zobrazí se help na vybraný příkaz
            self.append_note('%s: ${BOLD}${GREEN}%s${NORMAL}'%(_T("Help for command"),command_name))
            if type == 'EPP':
                command_line, command_help, notice, examples = self._epp_cmd.get_help(command_name, self._ljust, self._indent_left)
                examples = self.__repalce_static_null_examples__(examples)
                command_lines = (command_line,)
            else:
                command_lines, command_help, notice, examples = self.__get_help_session_detail__(command_name)
            #
            self.append_note('%s:'%_T('DESCRIPTION'),'BOLD')
            self.append_note('${WHITE}%s${NORMAL}'%self.__format_help_detail__(notice))
            #
            if len(command_lines):
                self.append_note('\n%s:'%_T('SYNTAX'),'BOLD')
                self.append_note(self.__format_help_detail__(command_lines))
            #
            if command_help:
                self.append_note('\n%s:'%_T('OPTIONS'),'BOLD')
                self.append_note(command_help)
            #
            if examples:
                self.append_note('\n%s:'%_T('EXAMPLES'),'BOLD')
                self.append_note(self.__format_help_detail__(examples))
            #
            command_name='.' # set name for console part, where we have to check command names
        return command_name

    def epp_command(self, cmdline, raw_command):
        'Find EPP command in input and check if is known.'
        command_name = cmdline
        stop = 0
        m=re.match('(!)?\s*(\S+)',cmdline)
        if m:
            if m.group(2) in self._available_commands:
                command_name = m.group(2)
                all_is_OK, stop = self.__parse_command_params__(command_name, cmdline, m.group(1))
                if stop == 2: return 'q',1 # User press Ctrl+C or Ctrl+D
                if all_is_OK:
                    if not stop:
                        # create document if only 'stop' was not occured.
                        cmd_params = self._epp_cmd.get_params()
                        self.create_command_with_params(command_name, cmd_params)
                else:
                    self.append_error(self._epp_cmd.get_errors()) # any problems on the command line occurrs
            else:
                if m.group(1)=='!':
                    if m.group(2) in self._available_session_commands:
                        if m.group(2).strip() == '!':
                            msg = '%s: %s'%(_T('ERROR'),_T('Illegal use of interactive input mode.'))
                        else:
                            msg = '%s: %s'%(_T('ERROR'),_T('Interactive input mode works with EPP commands only.'))
                    else:
                        msg = '%s: %s %s'%(_T('ERROR'),_T("Unknown command"),m.group(2).encode(translate.encoding))
                else:
                    msg = '%s: %s %s'%(_T('ERROR'),_T("Unknown command"),get_ltext(raw_command))
                self.append_note(msg)
                self.append_note(_T("Type 'help' to list all available commands."))
                self._epp_cmd.help_check_name(self._notes, cmdline)
        return command_name, stop

    def is_online(self, command_name):
        'Check if session is online.'
        return self._session[ONLINE] or command_name in ('hello','login')
        
    def create_command_with_params(self, command_name, dct_params):
        "Create EPP command. Check if session is loggend or not."
        # for build example later
        dct_params['command'] = [command_name]
        dct_params[command_name] = [command_name]
        self._epp_cmd.set_params(dct_params) # set params from API (or one's own)
        self._raw_cmd = ''
        if command_name in ('login','hello'):
            getattr(self,'create_%s'%command_name)()
        else:
            # if attr exists had been check in epp_command() or in API module.
            getattr(self._epp_cmd, "assemble_%s"%command_name)(self.__next_clTRID__())

    def create_eppdoc(self, command):
        "Dispatch command line from user and set internal variables or create EPP document."
        command_name = ''
        command_params = ''
        stop = 0
        self.reset_round()
        cmd = EPP_command = session_command = command.strip()
        match = re.match('!+\s+(.+)',cmd)
        if match: cmd = '!%s'%match.group(1) # removing whitespaces after exclamation
        # Možnost zadání pomlčky místo podtržítka:
        m = re.match('(\S+)(.*)',cmd)
        if m:
            EPP_command = '%s%s'%(m.group(1).replace('-','_'), m.group(2))
            session_command = m.group(1)
            command_params = m.group(2)
        if cmd == '!':
            self.append_note(_T('ERROR: Missing command to start interactive input'))
            self.append_note(_T("Type 'help !' for more information."))
            return command_name, self._raw_cmd, 0
        # help
        help, help_item = None,None
        m = re.match('(h(?:elp)?)(?:$|\s+(\S+))',cmd)
        if m:
            help, help_item = m.groups()
        else:
            m = re.match('(\?)(?:$|\s*(\S+))',cmd)
            if m: help, help_item = m.groups()
        # Resolve three command types: 1. help; 2. session command; 3. EPP command
        if help:
            # 1. help
            self.display_help(help_item, command)
        elif session_command in self._pattern_session_commands:
            # 2. Session commands
            for names,func,req,p,e,x in self._session_commands:
                if session_command in names:
                    if func:
                        name = func(command_params.strip())
                        if name is not None: command_name = name
        elif session_command in self._hidden_commands:
            # undocumented hidden commands for TEST purpose
            if session_command == 'answer-cols':
                self.__session_translate_column_names__(command_params.strip())
            elif session_command == 'hidden':
                self.append_note('%s: ${BOLD}%s${NORMAL}'%(_T('Hidden commands are'),', '.join(self._hidden_commands)))
        else:
            # 3. EPP commands
            cmd = EPP_command
            if type(cmd) != unicode:
                try:
                    cmd = unicode(cmd, translate.encoding)
                except UnicodeDecodeError, msg:
                    self.append_error('UnicodeDecodeError: %s'%msg)
                    cmd = unicode(repr(cmd), translate.encoding)
            command_name, stop = self.epp_command(cmd, command)
            if command_name != 'q': # User press Ctrl+C or Ctrl+D in interactive mode.
                self._raw_cmd = self._epp_cmd.get_xml()
                self.append_error(self._epp_cmd.fetch_errors()) # any problems on the command line occurrs
        return command_name, self._raw_cmd, stop

    def load_filename(self, filepath):
        'Load file and returs name of EPP command.'
        if os.path.isfile(filepath):
            self.append_note('%s: %s'%(_T('Load file'),filepath))
            self._raw_cmd = self._epp_cmd.load_xml_doc(filepath)
            errors = self._epp_cmd.fetch_errors()
            if errors: self.append_note(errors)
            command_name = self.grab_command_name_from_xml(self._raw_cmd)
        else:
            self.append_note('%s: %s'%(_T('Not found'),filepath))
            command_name = ''
        return command_name, self._raw_cmd

    def convert_utf8(self, text_utf8):
        'Convert str in UTF-8 to unicode.'
        error = utext = ''
        try:
            utext = text_utf8.decode('utf-8')
        except UnicodeDecodeError, msg:
            error = 'UnicodeDecodeError: %s'%msg
        return utext, error

    def get_credits(self):
        'Returs credits'
        body, error = load_file(make_filepath('CREDITS'))
        if error:
            report = error
        else:
            report, error = self.convert_utf8(body)
            if error: report += '\n'+error
        return report
        

    #==================================================
    #
    #    Session commands
    #
    #==================================================
    def __session_translate_column_names__(self, param):
        'Set translation of column names in server answer.'
        # TEST only
        if param: self._session[TRANSLATE_ANSWER_COLUMN_NAMES] = re.match('(y(es)?|on|1)',param,re.I) and 1 or 0
        self.append_note('%s: ${BOLD}%s${NORMAL}'%(_T('Translation of answer column names is'),self._session[TRANSLATE_ANSWER_COLUMN_NAMES] and 'ON' or 'OFF'))

    def __session_confirm__(self, param):
        'Set confirm value'
        if param:
            self.set_confirm(param)
        else:
            self.append_note('%s ${BOLD}%s${NORMAL}'%(_T('Command confirmation is'),self._session[CONFIRM_SEND_COMMAND] and 'ON' or 'OFF'))

    def __session_null__(self, param):
        'Set NULL value'
        if param:
            self.set_null_value(param)
            msg = _T('null_value has been set to')
        else:
            msg = _T('null_value is')
        self.append_note('%s ${BOLD}%s${NORMAL}'%(msg,self._session[NULL_VALUE]))

    def __session_validate__(self, param):
        'Set validate value'
        if param:
            value = param.upper()
            if value in ('ON','OFF'):
                self.set_validate(value=='ON' and 1 or 0)
                self.append_note('%s: ${BOLD}%s${NORMAL}'%(_T('Client-side validation has been set to'), self._session[VALIDATE] and 'ON' or 'OFF'))
            else:
                self.append_error('%s %s'%(_T('Invalid Client-side validation parametr'),param))
                self._notes_afrer_errors.append(_T("Type 'help validate' to get more information about client-side validation."))
        else:
            self.append_note('%s: ${BOLD}%s${NORMAL}'%(_T('Client-side validation is'), self._session[VALIDATE] and 'ON' or 'OFF'))
        
    def __session_connect__(self, param):
        'Run connection process'
        if self.is_connected():
            self.append_note(_T('You are connected already. Type disconnect for close connection.'))
        else:
            self.connect() # připojení k serveru
        return 'connect' # Need for fred_console.py where must be displayed server answer.

    def __session_disconnect__(self, param):
        'Run connection process'
        if self.is_connected():
            if self.is_online(''):
                self.send_logout()
            else:
                self.close()
            self.append_note(_T("You has been disconnected."))
        else:
            self.append_note(_T("You are not connected."))

    def __session_colors__(self, param):
        'Set colors mode'
        if param:
            self._session[COLORS] = param.lower()=='on' and 1 or 0
            colored_output.set_mode(self._session[COLORS])
            msg = _T('Colors mode has been set to')
        else:
            msg = _T('Colors mode is')
        self.append_note('%s ${BOLD}%s${NORMAL}'%(msg, self._session[COLORS] and 'ON' or 'OFF'))

    def __session_verbose__(self, param):
        'Set verbose mode'
        if param:
            if self.parse_verbose_value(param) is not None:
                self.append_note('%s ${BOLD}%d${NORMAL}'%(_T('Verbose mode has been set to'), self._session[VERBOSE]))
        else:
            self.append_note('%s ${BOLD}%d${NORMAL}'%(_T('Verbose mode is'), self._session[VERBOSE]))

    def __session_license__(self, param):
        'Display license'
        body, error = load_file(make_filepath('LICENSE'))
        if error: self.append_error(error)
        if body:
            text, error = self.convert_utf8(body)
            if error: self.append_note(error)
            self.append_note(text)
            

    def __session_credits__(self, param):
        'Display credits'
        body, error = load_file(make_filepath('CREDITS'))
        if error: self.append_error(error)
        if body:
            text, error = self.convert_utf8(body)
            if error: self.append_note(error)
            self.append_note(text)

    def __session_poll_ack__(self, param):
        'Set poll acknowledge'
        if param:
            self._session[POLL_AUTOACK] = param in ('on','ON') and 1 or 0
            msg = _T('Autoacknowledge poll has been set to')
        else:
            msg = _T('Autoacknowledge poll is')
        self.append_note('%s ${BOLD}%s${NORMAL}'%(msg, self._session[POLL_AUTOACK] and 'ON' or 'OFF'))

    def __session_output__(self, param):
        'Set output type'
        if param:
            self._session[OUTPUT_TYPE] = self.get_valid_output(param)
            self.get_valid_output(param)
            msg = _T('Output type has been set to')
        else:
            msg = _T('Output type is')
        self.append_note('%s ${BOLD}%s${NORMAL}'%(msg, self._session[OUTPUT_TYPE]))
        
    def __session_send__(self, param):
        'Send any file to the EPP server.'
        command_name = None
        if not param: param = '.'
        if os.path.isdir(param):
            # zobrazit adresář
            self.append_note('%s: %s'%(_T('Dir list'),param))
            try:
                stuff = dircache.listdir(param)
            except OSError, (no, msg):
                stuff = 'OSError: [%d] %s'%(no, msg)
            self.append_note(str(stuff))
        else:
            command_name, xmldoc = self.load_filename(param)
            if command_name == 'login' and not self.is_connected():
                self.connect() # connect to the host
        return command_name

    def __session_raw_answer__(self, param):
        'Display XML answer source.'
        self.append_note(SEPARATOR)
        if param and param[0]=='d': # d dict
            self.append_note(_T('Interpreted answer'),'BOLD')
            self.__put_raw_into_note__(self._dict_answer)
        else: # e epp
            self.append_note(_T('Answer source'),'BOLD')
            self.__put_raw_into_note__(human_readable(self._raw_answer))

    def __session_raw_command__(self, param):
        'Display XML command source.'
        self.append_note(SEPARATOR)
        if param and param[0]=='d': # d dict
            self.append_note(_T('Interpreted command'),'BOLD')
            edoc = eppdoc_client.Message()
            edoc.parse_xml(self._raw_cmd)
            self.__put_raw_into_note__(edoc.create_data())
        else: # e epp
            self.append_note(_T('Command source'),'BOLD')
            self.append_note(human_readable(self._raw_cmd),'GREEN')

    def __session_language__(self, param):
        'Set language'
        if param:
            lang, error = translate.get_valid_lang(param, _T('command'))
            if error:
                self.append_note(_T("Unsupported language code: '%s'.\nAvailable codes are: %s.")%(param, ', '.join(translate.langs.keys())))
                msg = _T('Language is')
            else:
                if self._session[LANG] == lang:
                    self.append_note('%s ${BOLD}%s${NORMAL}'%(_T('User interface language is already'), self._session[LANG]))
                else:
                    self._session[LANG] = lang
                    translate.install_translation(lang)
                    # Refresh texts in EPP Message objects and in EPP Manager:
                    self._epp_cmd.reset_translation()
                    self._epp_response.reset_translation()
                    self.init_session_commands()
                    self.append_note('%s ${BOLD}%s${NORMAL}'%(_T('User interface language has been set to'), self._session[LANG]))
                    if self._session[ONLINE]: self.append_note(_T('Reconnect to change server language too.'))
        else:
            self.append_note('%s ${BOLD}%s${NORMAL}'%(_T('User interface language is'), self._session[LANG]))
        
    #==================================================
    #
    #    EPP commands
    #
    #==================================================
    def create_hello(self):
        'Create EPP document hello'
        if self._auto_connect and not self.is_connected():
            if not self.connect(): return # connect fails
        self._epp_cmd.assemble_hello()

    def create_login(self):
        'Create EPP document login'
        if self._session[ONLINE]:
            # klient je už zalogován
            self.append_note(_T('You are logged already.'))
        else:
            cmd_params = self._epp_cmd.get_params()
            if cmd_params.has_key('lang'):
                self.__session_language__(get_ltext(cmd_params['lang'][0]))
            if self._auto_connect and not self.is_connected():
                # commection MUST be created BEFOR assembling login because of tags
                # <objURI> and <extURI>
                if not self.connect(): return # connect fails
            # prefix 4 ASCII znaků pro clTRID (pro každé sezení nový)
            self._session[CMD_ID] = 0
            self.defs[PREFIX] = ''.join([chr(random.randint(97,122)) for n in range(4)])
            self._epp_cmd.assemble_login(self.__next_clTRID__(), (eppdoc_nic_cz_version, self.defs[objURI], self.defs[extURI], self._session[LANG]))
            if self._epp_cmd._dct.has_key('username'):
                self._session[USERNAME] = self._epp_cmd._dct['username'][0] # for prompt info

    #==================================================

    def get_value_from_dict(self, names, dct = None):
        """Returns safetly value form dict (treat missing keys).
        Parametr names can by str or list ro tuple.
        """
        if dct is None: dct = self._dct_answer
        return eppdoc.get_value_from_dict(dct, names)

    def automatic_login(self, no_outoupt=None):
        'Automatic login if all needed informations are known.'
        if self._session[ONLINE]: return 1 # session is logged on already
        if self.get_config_value(self.config_get_section_connect(), 'nologin', OMIT_ERROR): return 1
        if not self.check_connect_data(self.get_connect_defaults()): return 0
        ok=0
        # set values from config or options as a parsed params
        self._epp_cmd._dct['username'] = [self.get_config_value(self._section_epp_login, 'username', OMIT_ERROR)]
        self._epp_cmd._dct['password'] = [self.get_config_value(self._section_epp_login, 'password', OMIT_ERROR)]
        self.create_login() # connect and get greeting message, than create XML login document
        epp_doc = self._epp_cmd.get_xml()
        if epp_doc and self.is_connected():
            if self._session[VERBOSE] > 1: self.append_note(_T('Login command sent to the server'))
            self.send(epp_doc)          # odeslání dokumentu na server
            answer = self.receive()     # příjem odpovědi
            self.process_answer(answer) # zpracování odpovědi
            if not no_outoupt:
                self.display() # display errors or notes
                self.print_answer() # 2. departure from the rule to print answers
            ok = self._dct_answer.get('code',0) == 1000 and 1 or 0
        else:
            self.append_error(self._epp_cmd.get_errors())
            self.display() # display errors or notes
        return ok
            
        
def make_filepath(filename):
    modul_path,fn = os.path.split(__file__)
    return os.path.join(modul_path, filename)

def load_file(filename):
    'Returs body and error if any occurs.'
    body = error = ''
    try:
        body = open(filename).read()
    except IOError, (errnum, msg):
        error = 'IOError: %d. %s (%s)'%(errnum,msg,filename)
    return body, error

def __make_help_columns__(names,fcols,left_indent,padding=26):
    'Make columns from list of names. Param cols must be float.'
    length = int(math.ceil(len(names)/fcols))
    sep = '\n%s'%(' '*left_indent)
    return '%s%s'%(' '*left_indent, sep.join([''.join(map(lambda s: s.ljust(padding), names[i::length])) for i in range(length)]))


if __name__ == '__main__':
    # Test
    m = ManagerCommand()
    m._session[0]=1 # login simulation
##    command_name, xml, stop = m.create_eppdoc('create_contact reg-id "John Doe" jon@mail.com "New York" US "Example Inc." ("Yellow harbor" "Blueberry hill") VA 20166-6503 +1.7035555555 +1.7035555556 (0 d-name "d org." "street number city" +21321313 +734321 info@buzz.com) vat-test ssn-test notify@here.net')
    # Test na disclose
    disclose = "(n (org fax email))"
    print 'disclose:',disclose
    command_name, xml, stop = m.create_eppdoc("create_contact CID:ID01 'Jan Novak' info@mymail.cz Praha CZ mypassword 'Firma s.r.o.' 'Narodni trida 1230/12' '' 12000 +420.222745111 +420.222745111 %s"%disclose)
    print m.is_epp_valid(xml)
    print xml
    m.display()
