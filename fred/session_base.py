# -*- coding: utf8 -*-
#!/usr/bin/env python
import re, time
import sys, os, StringIO
import ConfigParser
import terminal_controler
import translate
import session_config
import internal_variables

# Colored output
colored_output = terminal_controler.TerminalController()

# názvy sloupců pro data sestavené při spojení se serverem
ONLINE, CMD_ID, LANG, POLL_AUTOACK, CONFIRM_SEND_COMMAND, \
   USERNAME, SESSION, HOST, COLORS, VALIDATE, VERBOSE, SORT_BY_COLUMNS, NULL_VALUE, \
   TRANSLATE_ANSWER_COLUMN_NAMES, OUTPUT_TYPE = range(15)
# názvy sloupců pro defaultní hodnoty
DEFS_LENGTH = 4
LANGS,objURI,extURI,PREFIX = range(DEFS_LENGTH)
OMIT_ERROR = 1

OUTPUT_TYPES = ('text','html','php')

class ManagerBase:
    """This class holds buffers with error and note messages.
    Class collects messages and prepares them for output.
    """
    def __init__(self):
        self._notes = [] # upozornění na chybné zadání
        self._errors = [] # chybová hlášení při přenosu, parsování
        self._notes_afrer_errors = [] # hlášení po chybách
        self._sep = '\n' # oddělovač jednotlivých zpráv
        #-----------------------------------------
        # Session data:
        #-----------------------------------------
        self._session = [
                0,      # ONLINE
                0,      # CMD_ID
                'en',   # LANG
                0,      # POLL_AUTOACK
                1,      # CONFIRM_SEND_COMMAND
                '',     # USERNAME (for prompt info)
                '',     # SESSION
                '',     # HOST (for prompt info)
                0,      # COLORS 0/1
                1,      # VALIDATE
                1,      # VERBOSE 1,2,3
                [],     # SORT_BY_COLUMNS - support for sotring received values (used by check_...)
                'NULL', # NULL_VALUE
                1,      # TRANSLATE_ANSWER_COLUMN_NAMES, TEST only
                'text', # OUTPUT_TYPE (text, html)
                ]
        self._external_validator = 'xmllint'
        # defaults
        self.defs = ['']*DEFS_LENGTH
        # Values objURI a extURI are loaded from greeting message.
        self.defs[objURI] = ['http://www.nic.cz/xml/epp/contact-1.0',
                'http://www.nic.cz/xml/epp/domain-1.0',
                'http://www.nic.cz/xml/epp/nsset-1.0']
        self.defs[extURI] = ['http://www.nic.cz/xml/epp/enumval-1.0']
        self.defs[PREFIX] = '' # pro každé sezení nový prefix
        self._conf = None ## <ConfigParser object> from session_config.py
        self._auto_connect = 1 # auto connection during login or hello
        self._options = translate.options # parameters from command line
        if type(self._options) is not dict:
            self._options = {'lang':'en','colors':'off','verbose':'1','user':'','password':'','host':'',}
        self._email_reports_bug = 'fred@nic.cz'
        # Used in detailed help:
        self._ljust = 25      # indent description column from names
        self._indent_left = 2 # indent from left border
        self._section_epp_login = 'epp_login' # section name in config for username and password
        self._config_name = '.fred_client.conf' # name for home folder; for share (etc) is mofified from this name
        self._config_used_files = []

    def get_session(self, offset):
        return self._session[offset]

    def init_from_options(self, section_connect):
        'Init variables from options (after loaded config).'
        # connect
        op = self._options
        if op['host']: self._conf.set(section_connect,'host',op['host'])
        if op['port']: self._conf.set(section_connect,'port',op['port'])
        if op['user']: self._conf.set(section_connect,'username',op['user'])
        if op['password']: self._conf.set(section_connect,'password',op['password'])
        if op['cert']: self._conf.set(section_connect,'ssl_cert',op['cert'])
        if op['privkey']: self._conf.set(section_connect,'ssl_key',op['privkey'])
        if op['nologin']: self._conf.set(section_connect,'nologin','nologin')
        # copy variables for individual commands
        self.copy_default_options(self._section_epp_login, section_connect, 'username')
        self.copy_default_options(self._section_epp_login, section_connect, 'password')
        # selection fo language version
        self._session[LANG] = op['lang']
        if op['verbose']:
            self.parse_verbose_value(op['verbose'])
        key = op['output'].lower()
        if key:
            self._session[OUTPUT_TYPE] = self.get_valid_output(key)
        if op['no_validate']: self._session[VALIDATE] = 0

    def fill_missing_required(self, section_connect):
        'Fill missing required valurs by defaults.'
        for key in ('port','timeout'):
            if self.get_config_value(section_connect,key,OMIT_ERROR) is None:
                self._conf.set(section_connect,key,str(internal_variables.required_defaults[key]))
        
    def get_valid_output(self, key):
        'Get valid output type.'
        if not key in OUTPUT_TYPES:
            self.append_error('%s: (%s)'%(_T('Unknown output type. Valid types are'),', '.join(OUTPUT_TYPES)))
            key = self._session[OUTPUT_TYPE]
        return key
        
    def set_auto_connect(self, switch):
        'Set auto connection ON/OFF. switch = 0/1.'
        self._auto_connect = switch==1 and 1 or 0

    def is_logon(self):
        'Returns 0-offline,1-online.'
        return self._session[ONLINE]

    def get_username_and_host(self):
        'Returns username and host.'
        return self._session[USERNAME], self._session[HOST]
        
    def is_confirm_cmd_name(self, command_name):
        'Returns 0-not conrifmation,1-need conrifmation.'
        return self._session[CONFIRM_SEND_COMMAND] and re.match('(create|update|delete|transfer|renew)',command_name)

    def set_confirm(self, type):
        'Set switch confirm_commands_before_send'
        value = type.upper()
        if value in ('ON','OFF'):
            self._session[CONFIRM_SEND_COMMAND] = value == 'ON' and 1 or 0
            self.append_note('%s ${BOLD}%s${NORMAL}'%(_T('Command confirmation has been set to'),self._session[CONFIRM_SEND_COMMAND] and 'ON' or 'OFF'))
        else:
            self.append_error('%s %s'%(_T('Invalid Command confirmation parametr'),type))
            self._notes_afrer_errors.append(_T("Type 'help confirm' to get more information about confirm commands."))

    def get_errors(self, sep='\n'):
        return sep.join(self._errors)

    def append_error(self, msg, color=''):
        "Join messages if only they are not empty."
        if msg: append_with_colors(self._errors, msg, color)

    def append_note(self, msg, color=''):
        "Join messages if only they are not empty."
        if msg: append_with_colors(self._notes, msg, color)

    def fetch_errors(self, sep='\n'):
        msg = join_unicode(self._errors, sep)
        self._errors = []
        return msg

    def fetch_notes(self, sep='\n'):
        msg = join_unicode(self._notes, sep)
        self._notes = []
        return msg

    def is_error(self):
        "Check if any error occurs."
        return len(self._errors)
        
    def is_note(self):
        "Check if any note is in the stack"
        return len(self._notes)

    def get_init_php(self):
        'Get part of PHP code what have to put as a first into output.'
        return """
$fred_client_notes = array();  // notes occuring during communication
$fred_client_errors = array(); // errors occuring during communication
"""
        
    def display(self):
        "Output all messages to stdout or log file."
        msg = self.get_messages()
        if msg and self._session[VERBOSE]: print msg

    def get_messages(self, sep='\n'):
        'Same as display but returns as local string.'
        #TODO: log file
        msg = []
        is_php = self._session[OUTPUT_TYPE] == 'php'
        if self.is_note():
            # hlášení, poznámka, hodnoty
##            if self._notes[-1] != '': msg.append('') # empty line
            for text in self._notes:
                if is_php:
                    msg.append('$fred_client_notes[] = %s;'%php_string(text))
                else:
                    msg.append(get_ltext(colored_output.render(text)))
            self._notes = []
        if self.is_error():
            # chybová hlášení
##            if len(msg): msg.append('') # empty line - indent errors
            if len(msg) and msg[-1] != '': msg.append('')
            self._errors[-1] += colored_output.render('${NORMAL}')
            if is_php:
                msg.append('$fred_client_errors[] = %s;'%php_string(self._errors[0]))
            else:
                label = _T('ERROR')
                msg.append('%s%s: %s'%(colored_output.render('${RED}${BOLD}'),label, self._errors[0]))
            for text in self._errors[1:]:
                if is_php:
                    msg.append('$fred_client_errors[] = %s;'%php_string(text))
                else:
                    msg.append(get_ltext(text))
            self._errors = []
        if len(self._notes_afrer_errors):
            if is_php: 
                msg.extend(map(lambda s: '$fred_client_notes[] = %s;'%php_string(s), self._notes_afrer_errors))
            else:
                msg.extend(map(get_ltext, self._notes_afrer_errors))
            self._notes_afrer_errors = []
##        if len(msg) and msg[-1] != '': msg.append('') # empty line at the end of all output
        return sep.join(msg)

    def welcome(self):
        "Welcome message."
        return '%s\n%s\n'%(self.version(),_T('Type "help", "license" or "credits" for more information.'))

    def version(self):
        return 'FredClient 1.2.0' # version of the client

    def __next_clTRID__(self):
        """Generate next clTRID value.
        format: [4 random ASCII chars][3 digits of the commands order]#[date and time]
        """
        self._session[CMD_ID]+=1 
        return ('%s%03d#%s'%(self.defs[PREFIX],self._session[CMD_ID],time.strftime('%y-%m-%dat%H:%M:%S')))

    def set_null_value(self, value):
        'Set string what represents NULL value'
        value = value.strip()
        if len(value):
            if re.search('[- \(\)]',value) or value in ('""',"''"):
                self.append_error('%s null_value: %s. %s'%(_T('Invalid format of'),value,_T('See help for more.')), 'RED')
            else:
                self._session[NULL_VALUE] = value
        else:
            self.append_error('null_value %s. %s'%(_T('cannot be empty'),_T('See help for more.')), 'RED')
        
    #---------------------------
    # config
    #---------------------------
    def manage_config(self, param):
        'Display config values or save config.'
        if len(self._config_used_files):
            print_unicode('${BOLD}${YELLOW}%s:${NORMAL}\n\t%s'%(_T('Actual config builded from files'),'\n\t'.join(self._config_used_files)))
        else:
            print_unicode('${BOLD}${RED}%s${NORMAL}'%_T('No configuration file. Defaults used instead it.'))
        if not self._conf:
            print_unicode(_T('No config'))
            return
        selected_section = self.config_get_section_connect()
        for section in self._conf.sections():
            msg = ''
            if section == selected_section:
                msg = '${BOLD}${GREEN}*** %s ***${NORMAL}'%_T('Actual connection HERE')
            print colored_output.render('${BOLD}[%s]${NORMAL} %s'%(section,msg))
            for option in self._conf.options(section):
                print_unicode(colored_output.render('\t${BOLD}%s${NORMAL} = %s'%(option,str(self.get_config_value(section,option)))))

    def copy_default_options(self, section, section_default, option):
        'Copy default options where they missing.'
        value = self.get_config_value(section, option, 1)
        if not value:
            value = self.get_config_value(section_default, option, 1)
            if value:
                if not self._conf.has_section(section): self._conf.add_section(section)
                self._conf.set(section, option, value)

    def __create_default_conf__(self):
        'Create default config file.'
        ok = 0
        modul_path,fn = os.path.split(__file__)
        root_path = os.path.normpath(os.path.join(modul_path,'..'))
        try:
            self._conf.readfp(StringIO.StringIO(internal_variables.config))
            ok = 1
        except ConfigParser.ParsingError, msg:
            self.append_error(msg)
        else:
            # schema = all-1.0.xsd
            seop = ('session','schema')
            name = self.get_config_value(seop[0], seop[1])
            if not name:
                self.append_error(_T('Schema in session missing. This is invalid instalation.'))
                return 0
            self._conf.set(seop[0], seop[1], os.path.join(modul_path,'schemas',name))
            # make copy if need
            new_section = ''
            section = self.config_get_section_connect()
            if section != 'connect':
                new_section = section
                section = 'connect'
            # adjust pathnames
            modul_path,fn = os.path.split(__file__)
            root_path = os.path.normpath(os.path.join(modul_path,'certificates'))
            self._conf.set(section, 'dir', root_path)
            if new_section:
                # copy default values into new connection
                self._conf.add_section(new_section)
                for option in ('host','port','ssl_key','ssl_cert','dir'):
                    self.copy_default_options(new_section, section, option)
        return ok 

    def get_config_value(self, section, option, omit_errors=0):
        'Get value from config and catch exceptions.'
        value=None
        if not self._conf: return value
        try:
            value = self._conf.get(section,option)
        except (ConfigParser.NoSectionError, ConfigParser.NoOptionError, ConfigParser.InterpolationMissingOptionError), msg:
            if not omit_errors: self.append_error('ConfigError: %s (%s, %s)'%(msg,section,option))
        return value

    def config_get_section_connect(self):
        'Set section name "connect" in config.'
        if self._session[SESSION]:
            section = 'connect_%s'%self._session[SESSION]
        else:
            section = 'connect'
        return section

    def load_config(self, options=None):
        "Load config file and init internal variables. Returns 0 if fatal error occured."
        # 1. first load values from config
        # 2. overwrite them by options from command line
        #
        # keep options in Manager instance
        if type(options) is dict: self._options = options
        # Load configuration file:
        self._conf, self._config_used_files, config_errors = session_config.main(self._config_name, self._options)
        # set language version
        translate.install_translation(self._options['lang'])
        if len(self._config_used_files):
            self.append_note('%s %s'%(_T('Using configuration from'), ', '.join(self._config_used_files)))
        if len(config_errors):
            self._errors.extend(config_errors)
            return 0 # Errors occured during parsing config. Error of missing file not included!
        self._session[SESSION] = self._options.get('session','') # API definition of --session parameter.
        # set session variables
        section = 'session'
        if not self._conf.has_section(section):
            if not self.__create_default_conf__():
                self.append_error(_T('Fatal error: Default config create failed.'))
                self.display() # display errors or notes
                return 0 # fatal error
            if self._options['session'] != '':
                self.append_error(_T('Session "%s" without effect. No configuration file.')%self._options['session'])
        # for login with no parameters
        section_connect = self.config_get_section_connect()
        if not self._conf.has_section(section_connect):
            self._conf.add_section(section_connect)
            self.append_error(_T('Configuration file has no section "%s".')%section_connect[8:])
            return 0 # fatal error
        # session
        section = 'session'
        self._session[POLL_AUTOACK] = str(self.get_config_value(section,'poll_autoack',OMIT_ERROR)).lower() == 'on' and 1 or 0
        self._session[CONFIRM_SEND_COMMAND] = self.get_config_value(section,'confirm_send_commands').lower() == 'on' and 1 or 0
        self._session[VALIDATE] = self.get_config_value(section,'validate').lower() == 'on' and 1 or 0
        colors = self.get_config_value(section,'colors',OMIT_ERROR)
        if colors:
            self._session[COLORS] = colors.lower() == 'on' and 1 or 0
            colored_output.set_mode(self._session[COLORS])
        self.parse_verbose_value(self.get_config_value(section,'verbose',OMIT_ERROR))
        # set NULL value
        value = self.get_config_value(section,'null_value',OMIT_ERROR)
        if value: self.set_null_value(value)
        # init from command line options
        self.init_from_options(section_connect)
        self.fill_missing_required(section_connect)
        self.check_validator() # set validator OFF, if not supported.
        return 1 # OK

    def parse_verbose_value(self, verbose):
        'Init verbose mode.'
        if verbose is None: return self._session[VERBOSE]
        nverb = None
        if type(verbose) in (str,unicode):
            try:
                nverb = int(verbose)
            except ValueError, msg:
                self.append_error('%s %s'%(_T('Invalid verbose parametr'),verbose))
                # self.append_error(_T('Valid verbose level is: 1, 2, 3.'))
                self._notes_afrer_errors.append(_T("Type 'help verbose' to get more information about verbose levels."))
                return None
        elif type(verbose) is int: nverb = verbose
        if nverb in (0,1,2,3):
            self._session[VERBOSE] = nverb
        else:
            self.append_error(_T('Verbose level is out of range. Available values are 1, 2, 3.'))
            self._notes_afrer_errors.append(_T("Type 'help verbose' to get more information about verbose levels."))
            nverb = None
        return nverb

    def set_verbose(self, verbose):
        'Set verbose mode.'
        self.parse_verbose_value(verbose)
        return self._session[VERBOSE]
    
    #---------------------------
    # validation
    #---------------------------
    def set_validate(self, value):
        'Set validate mode in session.'
        self._session[VALIDATE] = value
    
    def check_validator(self):
        'Check if exists external validator (xmllint).'
        if not self._session[VALIDATE]: return # validate is set OFF
        ok = 0
        try:
            pipes = os.popen3(self._external_validator)
        except IOError, msg:
            self.append_note(str(msg),('RED','BOLD'))
        standr = pipes[1].read()
        errors = pipes[2].read()
        map(lambda f: f.close(), pipes)
        if len(standr) and not len(errors):
            ok = 1 # OK, support is enabled.
        else:
            try:
                uerr = errors.decode(translate.encoding)
            except UnicodeDecodeError:
                uerr = repr(errors)
            self._session[VALIDATE] = 0 # validator is automaticly switched off
            if self._session[VERBOSE] > 1:
                self.append_note(uerr)
                self.append_note(_T('External validator "%s" not found. XML validation has been disabled.')%self._external_validator)
        return ok
    
    def is_epp_valid(self, message):
        "Check XML EPP by xmllint. OUT: '' - correct; '...' any error occurs."
        if not self._session[VALIDATE]: return '' # validace je vypnutá
        tmpname = os.path.join(os.path.expanduser('~'),'eppdoc_tmp_test_validity.xml')
        try:
            open(tmpname,'w').write(message)
        except IOError, (no, msg):
            try:
                msg = msg.decode(translate.encoding)
            except UnicodeDecodeError, error:
                msg = '(UnicodeDecodeError) '+repr(msg)
            self._session[VALIDATE] = 0 # automatické vypnutí validace
            self.append_note('%s: [%d] %s'%(_T('Temporary file for XML EPP validity verification can not been created. Reason'),no,msg))
            self.append_note(_T("Client-side validation has been disabled. Type '%s' to enable it.")%'${BOLD}validate on${NORMAL}')
            return '' # impossible save xml file needed for validation
        # kontrola validity XML
        schema_path = self.get_config_value('session','schema')
        if not schema_path:
            os.unlink(tmpname)
            return '' # schema path is not set
        command = '%s --noout --schema "%s" "%s"'%(self._external_validator, schema_path, tmpname)
        if self._session[VERBOSE] > 2:
            self.append_note(_T('Client-side validation command:'), 'BOLD')
            self.append_note(get_ltext(command))
        try:
            pipes = os.popen3(command)
        except IOError, msg:
            self.append_note(str(msg),('RED',c))
        errors = pipes[2].read()
        map(lambda f: f.close(), pipes)
        if self._session[VERBOSE] < 3:
            # leave temporary file for test in verbose mode 3
            os.unlink(tmpname)
        if re.search(' validates$', errors):
            errors = '' # it seems be OK...
        else:
            if re.search('command not found',errors) \
                or re.search(u'není názvem vnitřního ani vnějšího příkazu'.encode('cp852'),errors) \
                or re.search('Schemas parser error',errors):
                # schema missing!
                self.append_note(_T('Warning: Client-side validation failed.'))
                if self._session[VERBOSE] > 1: self.append_note(get_ltext(errors))
                self._notes_afrer_errors.append(_T("Client-side validation has been disabled. Type '%s' to enable it.")%'${BOLD}validate on${NORMAL}')
                self._session[VALIDATE] = 0 # automatické vypnutí validace
                errors=''
        return errors

    def __prepare_help__(self,sc):
        'Prepare for help.'
        content = []
        stt,src = [[n.split(',') for n in x.split(';')] for x in sc]
        chn = colored_output.TERM_SHORTCUTS.split('\n')
        for m,o in stt:
            content.extend(['\n'.join([chn[int(p)] for p in src[int(o)]])]*int(m))
        return content
    
    def __do_help__(self,cont):
        'Make help data'
        clr = ('%s%s%s'%(colored_output.BOL,colored_output.CLEAR_EOL,colored_output.UP))*8
        while 1:
            try:
                for c in cont:
                    print c,'\n[Ctrl+C]'
                    time.sleep(0.2)
                    print clr,
            except KeyboardInterrupt:
                break
        print clr,

    def __display_help__(self, cmd):
        if colored_output.CLEAR_EOL and cmd[5:] == colored_output.get_term_vers():
            self.__do_help__(self.__prepare_help__(terminal_controler.supported_versions))


def append_with_colors(list_of_messages, msg, color):
    "Used by Manager::append_error() and Manager::append_note() functions"
    if color:
        if type(color) in (list, tuple):
            c = ''.join(['${%s}'%c for c in color])
        else:
            c = '${%s}'%(color or 'WHITE') # default color
        list_of_messages.append('%s%s${NORMAL}'%(c,msg))
    else:
        list_of_messages.append(msg)

def join_unicode(u_list, sep='\n'):
    'Convert str objects to unicode and catch errors.'
    out=[]
    for row in u_list:
        if type(row) == str:
            try:
                row = row.decode(translate.encoding)
            except UnicodeDecodeError, error:
                row = '(UnicodeDecodeError) '+repr(row)
        out.append(row)
    return sep.join(out)

def get_ltext(text):
    'Encode unicode to string in the local encoding.'
    if type(text) == str:
        ltext = colored_output.render(text)
    else:
        try:
            ltext = text.encode(translate.encoding)
        except UnicodeEncodeError, msg:
            ltext = repr(re.sub('\x1b[^m]*m','',text))
        else:
            ltext = colored_output.render(ltext)
    return ltext

def print_unicode(text):
    'Print text and catch encoding problems with unicode.'
    print get_ltext(text)
        

def get_unicode(text):
    'Convert to unicode and catch problems with conversion.'
    if type(text) == str:
        try:
            text = text.decode(translate.encoding)
        except UnicodeDecodeError:
            text = repr(re.sub('\$\{[A-Z]+\}','',text)) # remove color tags
    return text

def php_string(value):
    'Returns escaped string for place into PHP variable.'
    if type(value) in (str,unicode):
        ret = "'%s'"%re.sub("([^\\\])'","\\1\\'",get_ltext(value)).strip()
    elif type(value) in (list, tuple):
        items=[]
        for n in value:
            items.append(php_string(n))
        ret = 'array(%s)'%', '.join(items)
    else:
        ret = value # int or float
    return ret

    
if __name__ == '__main__':
    mb = ManagerBase()
    mb._conf = ConfigParser.SafeConfigParser()
    mb.__create_default_conf__()
    mb.display()
    for section in mb._conf.sections():
        print '[%s]'%section
        for item in mb._conf.items(section):
            print '\t%s = %s'%item
