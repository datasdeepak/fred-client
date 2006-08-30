��    �      t    �        �   	  C  �  �   �  B  �  �  �  �   �  '   �  *   �  P   �     '     8     O     ]     t     �  !   �  )   �      �          -  9   H  4   �  )   �     �     �            
   3     >     P     b  �  z  *   $  5   O     �     �  -   �     �  %   �  &        3     D     U  %   t  ,   �  ,   �     �              '      G   E      �      �   *   �      �   !   �      !     !  
   -!  
   8!  o   C!  #   �!     �!  -   �!  /   "     O"     b"     v"  $   �"  $   �"  "   �"  "   �"  E   #     `#     v#     �#     �#     �#  	   �#     �#     �#     �#  '   $  #   6$  +   Z$  d   �$  	   �$     �$     �$     %  	   0%  %   :%     `%     h%  -   }%     �%  /   �%     �%     &     &     <&  
   Y&     d&     m&  ;   t&  /   �&  M   �&  9   .'  D   h'     �'     �'  D   �'  4   (  H   R(  7   �(  M   �(  M   !)  U   o)  Y   �)  E   *  s   e*  I   �*  M   #+  ;   q+     �+     �+     �+  6   �+  9   	,     C,  C   `,     �,     �,     �,     �,     �,     �,     -     -  2   /-  $   b-     �-     �-  Z   �-     .  ?   *.     j.  %   �.  G   �.     �.     /     /     /      /  
   %/  
   0/     ;/     H/     U/  #   m/     �/     �/     �/     �/  
   �/  '   �/     0  #   0     40     L0     T0     Y0     f0     s0  
   �0     �0     �0     �0     �0     �0  &   �0     �0     1     1  
   $1  
   /1     :1     F1     O1     l1     o1     �1     �1     �1     �1     �1  	   �1     �1  
   �1     �1  	    2     
2  .  2  Q   G3  �   �3  �   p4      5  �  A6  �   �7  :   �8  /   �8  V   9     b9     w9     �9     �9     �9     �9  >   �9  0   (:  3   Y:  $   �:  $   �:  J   �:  /   ";  %   R;     x;  $   �;     �;     �;     �;     �;     <     #<  �  ><  &   �?  3   @  0   ;@     l@  X   r@     �@  !   �@  !   �@     !A     3A  5   EA  +   {A  )   �A  1   �A     B     B  
   %B  =   0B  N   nB  	   �B     �B  K   �B  -   &C     TC     oC     �C     �C  	   �C  �   �C  /   HD     xD  E   �D  1   �D     
E     !E     7E  &   OE  (   vE  &   �E  &   �E  b   �E     PF     kF     �F     �F  
   �F     �F     �F     �F     �F      �F  )   G  ,   GG  k   tG     �G     �G     �G  ,   H  	   BH  &   LH  	   sH     }H  6   �H     �H  7   �H     #I     9I  '   RI     zI  $   �I     �I     �I  Q   �I  1   %J  ^   WJ  H   �J  B   �J  !   BK     dK  P   uK  8   �K  U   �K  5   UL  Q   �L  O   �L  Q   -M  O   M  K   �M  �   N  R   �N  W   O  @   dO     �O  !   �O     �O  9   �O  G   P  %   XP  O   ~P     �P     �P     �P  $   Q  	   @Q     JQ     NQ     lQ  G   �Q  (   �Q  %   �Q     R  ^   4R     �R  ;   �R     �R  -   �R  5   %S     [S  
   rS     }S     �S     �S  
   �S  
   �S     �S  
   �S     �S  &   �S     T  "   T     >T     MT     _T  $   cT  
   �T  4   �T  $   �T     �T     �T     �T     U     U     (U     6U  
   RU     ]U     oU     uU  ,   }U     �U     �U     �U     �U     �U     �U     �U  &   V     /V     5V     EV     KV     YV     lV     �V     �V     �V     �V     �V     �V     �V        P              K   :   �   �       6               `   �           �   �   >   D   �          1          �              h   8       �       �   '   �   �   �   �   J       �   �   ,   �       *   �          �   �       a   &       c   �   %      �      A   <   j   l   o   [   ;                            �               H   _   G   u      d       �   R   �       �       �       �   �   (           E   w          �   p   B   .   ]   \   z   e          �      �   b           Q   �   C   f   t      �   r   �   �   �   �   $   �   W   /   0       ~       �   �   �   �      ?      }   �   X   �   I   g       Y   �       #       �           5               
   	       �       {   m   �   @   k   |   L   �   -   �                  )   S   !           "   �   �   �   �          �   =   �   �           �           �              2   �   s   �   �   N   �   �          �   �           y   �   F      O   �   �   +       M          U   T   �   n   4   �   i           x      3   �   v       �   �   7   ^      q   Z   9   �   �                V    
   The "login" command establishes an ongoing server session that preserves client identity
   and authorization information during the duration of the session. 
   The EPP "check" command is used to determine if an object can be
   provisioned within a repository.  It provides a hint that allows a
   client to anticipate the success or failure of provisioning an object
   using the "create" command as object provisioning requirements are
   ultimately a matter of server policy.
 
   The EPP "create" command is used to create an instance of an object.
   An object can be created for an indefinite period of time, or an
   object can be created for a specific validity period.
 
   The EPP "info" command is used to retrieve information associated
   with an existing object. The elements needed to identify an object
   and the type of information associated with an object are both
   object-specific, so the child elements of the <info> command are
   specified using the EPP extension framework.
 
   The EPP "transfer" command provides a query operation that allows a
   client to determine real-time status of pending and completed
   transfer requests.
   The EPP "transfer" command is used to manage changes in client
   sponsorship of an existing object.  Clients can initiate a transfer
   request, cancel a transfer request, approve a transfer request, and
   reject a transfer request using the "op" command attribute.
    SSN types can be: 
      op       number identity card
      rc       number of birth
      passport number of passport
      mpsv     number of Ministry of Labour and social affairs
      ico      number of company (Value can be a list of max %d values.) (Value can be an unbouded list of values.) -c COMMAND, --command=COMMAND
                   send command to server and exit Actual config is Actual connection HERE Answer source Available EPP commands Available session commands Available values Available verbose modes: 1, 2r 3. Can not create connection. Missing values Can not save config file. Reason Certificate key file not found. Certificate names not set. Certificate not signed by verified certificate authority. Certificates missing. Trying to connect without SSL! Client for communication with EPP server. Colors mode is Command sent to EPP server. Command source Confirm has been set to Confirm is Connection broken Connection closed Connection interrupted. Connection options:
  -?, --help       show this help and exit
  -V, --version    Display program version information

  -l LANGUAGE, --lang=LANGUAGE
                   set user interface language
  -r, --colors     turn on colored output
  -v LEVEL, --verbose=LEVEL
                   set verbose level
                   1 - normal operation
                   2 - print more details
                   3 - print more details and display XML sources
  -h HOSTNAME, --host=HOSTNAME
                   ccReg server to connect 
  -u USERNAME, --user=USERNAME
                   authenticate to server as user
  -p PASSWORD, --password=PASSWORD
                   authenticate to server with password
  -s SESSION, --session=SESSION
                   read session name  used for connect to the EPP server
                   session values are read from config file
  -c CONFIG, --config=CONFIG
                   load config from filename Console for communication with EPP server. Create EPP XML document from command line parameters. Create default config failed. DESCRIPTION Default config file saved. See help for more. Dir list Display XML source of the EPP answer. Display XML source of the EPP command. Display credits. Display license. Display or create config file. Display this help or command details. Do you want send this command to the server? Document has wrong encoding. LookupError: %s EPP document is not valid ERROR EXAMPLES End of interactive input. [press enter] Eventual errors are return in XML format: <errors>... msg ...</errors>. Example Example of input Fatal error: Default config create failed. For list all commands type For more information, see README. For more type Help for command I'm fed up IP address If this client runs under MS Windows and timeout is not zero, it is probably SLL bug! Set timeout back to zero. If you don't fill item press ENTER. Incoming greeting message Interactive input params mode. For BREAK type Internal error: Master node '%s' doesn't exist. Interpreted answer Interpreted command Interrupted by user Invalid XML document. ExpatError: %s Invalid bracket definition (childs). Invalid bracket definition (list). Invalid bracket definition (mode). Invalid bracket. Only value or simple list allowed in key definition. Invalid input format. Invalid parameter index Invalid response code It's boring LIST of DNS Load file Login command sent to server Login failed Logout command sent to server Missing result in the response message. Missing values. Required minimum is Module for sending files to the EPP server. Names what are not included into disclose list are set to opposite value of the disclose flag value. No config No data No help available for No response from EPP server. Not found Not in registry: Object is available. OPTIONS Opened connection to Parameter MUST be a value from following list Private key file not found. Quit the client. Same effect has "q" or "exit". Report bugs to SSL connection initiated SSN (Security social number) SSN (Social security number) SSN number SSN type SYNTAX Same as help. For command details type "help command-name". Send "poll ack" straight away after "poll req". Send any file to the server. If filename missing command shows actual folder. Server configuration is not valid. Contact administrator. Server didn't return Greeting message. Contact server administrator. Server reply is not valid! Session started Set on/off confirmation for sending editable commands to the server. Set on/off external validation of the XML documents. Set verbose mode: 1 - brief (default); 2 - full; 3 - full & XML sources. Start the interactive mode of the input command params. Temporary file for XML EPP validity verification can not been created. Reason The EPP "delete" command is used to remove an instance of an existing object. The EPP "hello" request a "greeting" response message from an EPP server at any time. The EPP "list" command is used to list all ID of an existing object owning by registrant. The EPP "logout" command is used to end a session with an EPP server. The EPP "poll" command is used to discover and retrieve service messages queued by a server for individual clients. The EPP "renew" command is used to extend validity of an existing object. The EPP "update" command is used to update an instance of an existing object. This program requires Python 2.4 or higher. Your version is Try Turn on/off colored output. Type Type "help command" to get help on particular command. Type "help", "license" or "credits" for more information. Type %s to disable validator Unknown EPP command. Select one from EPP commands list (Type help). Unknown command Unknown parameter name Unknown response type Unknown server response Usage VAT VAT (Value-added tax) Validation process is Validator has been disabled. Type %s to enable it. Value "%s" is not allowed. Valid is: Value is required. MUST be set: Verbose mode is Warning: Command line history disabled (readline module not present). For more see README. You are logged already. You are not connected! Type login for connection to the server. You are not connected. You are not logged. First type login. You are not logged. You must call login() before working on the server. accepts only values add part address change part city contact ID contact id contact name country code current expiration date data for with is set the flag value disclose disclose flag (default y) domain name example inserted fax number index of message, required with op=ack! list of DNS list of values overflow. Maximum is list with max %d items. missing name new password notify email nsset address nsset name number of months or years optional organisation name password period period unit (y year(default), m month) poll ack is postal code postal informations query type registrant remove part required required only if part is set sp state or province street tech contact technical contact unbounded list voice (phone number) your city your contact ID your email your login name your name your password Project-Id-Version: 1.0
Report-Msgid-Bugs-To: 
POT-Creation-Date: 2006-08-30 16:05+0200
PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE
Last-Translator: Zdeněk Böhm <zdenek.bohm@nic.cz>
Language-Team: CS <info@nic.cz>
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
 
EPP příkaz "login" identifikuje uživatele a zahájí spojení s EPP serverem. 
   EPP Příkaz "check" se používá ke zjištění jestli se daný objekt
   v repozitáři nachází. To umožňuje řídit spouštění příkazu "create"
   a poté vyhodnotit jestli příkaz uspěl nebo ne.
 
   EPP příkaz "create" se používá pro vytvoření instance objektu.
   Objekt může být vytvořen na neučitý časový úsek nebo na přesně
   definované období.
 
   EPP příkaz "info" se používá ke zjištění informací spojených
   s vybraným objektem. Způsob identifikace objektu a typu
   navrácených informací spojených s objektem závisí na konkrétním
   typu info příkazu a případném použití EPP extension rozšíření.
 
   EPP příkaz "transfer" umožňuje zjišťovat aktuální stav
   nevyřízených anebo dokončených požadavků na transfer.
   Příkaz "transfer" se používá k ovládání změn
   na vybraném objektu. Klient může vyvolat požadavek
   na transfer. Nebo může požadovat zrušení požadavku, potvrzení
   požadavku a nebo odebrání požadavku. To vše pomocí atributu "op".
    SSN typ může být: 
      op       číslo občanského průkazu
      rc       rodné číslo
      passport číslo pasu
      mpsv     číslo Ministerstva práce a sociálních věcí
      ico      IČO (Hodnota může být seznam o max. velikosti %d položek.) (Hodnota může být libovolně velký seznam.) -c COMMAND, --command=COMMAND
                   odeslat příkaz na server a skončit Aktuální config je Aktuální spojení ZDE Zdrojová odpověď Dostupné EPP příkazy Dostupné session příkazy Povolené hodnoty Mód výstupu může být nastaven jen na hodnoty 1, 2 nebo 3. Není možné vytvořit spojení. Chybí hodnoty Není možné uložit konfigurační soubor. Důvod Soubor s certifikátem nebyl nalezen Jména certifikátů nejsou zadána. Použitý certifikát není podepsán uznávanou certifikační autoritou. Certifikát chybí. Zkouším spojení bez SSL! Klient pro komunikaci s EPP serverem. Mód barevnosti je Příkaz byl odeslán na EPP server. Zdrojový příkaz Potvrzení bylo nastaveno na Potvrzení je nastaveno na Spojení přerušeno Spojení uzavřeno Spojení bylo přerušeno. Parametry spojení:
  -?, --help       zobrazit tuto nápovědu a skončit
  -V, --version    zobrazit verzi programu

  -l LANGUAGE, --lang=LANGUAGE
                   nastavení jazykové verze
  -r, --colors     zapnout barevný výstiup
  -v LEVEL, --verbose=LEVEL
                   nastavení módu výpisu
                   1 - normální výstup
                   2 - zobrazit více detailů
                   3 - zobrazit více detailů a XML zdroje
  -h HOSTNAME, --host=HOSTNAME
                   ccReg server, na který se má navázat spojení
  -u USERNAME, --user=USERNAME
                   přihlašovací jméno
  -p PASSWORD, --password=PASSWORD
                   přihlašovací heslo
  -s SESSION, --session=SESSION
                   kolekce přihlašovacích hodnot z vybrané sekce v konfiguračním souboru
  -c CONFIG, --config=CONFIG
                   načtení konfiguračního soboru ze souboru Konzole pro komunikaci s EPP serverem. Vytvoří EPP XML dokument ze zadaných parametrů. Vytvoření defaultního config souboru selhalo. POPIS Defaultní konfigurační soubor byl uložen. Další informace naleznete v nápovědě. Výpis adresáře Zobrazit XML zdroj EPP odpovědi. Zobrazit XML zdroj EPP příkazu. Zobrazit credits. Zobrazit licenci. Zobrazení nebo vytvoření konfiguračního souboru. Zobrazit tento help nebo detaily příkazu. Chcete odeslat tento poříkaz na server? Dokument má chybné kódování. LookupError: %s EPP dokument není validní CHYBA PŘÍKLADY Konec interaktivního zadání parametrů. [stiskněte enter] Případné chyby jsou vráceny ve formátu XML: <errors>... msg ...</errors>. Příklad Příklad zadání Fatální chyba: Vytvoření defaultního konfiguračního souboru selhalo. Pro výpis celého seznamu příkazů zadejte Více informací v README. Pro více informací zadejte Nápověda pro příkaz Mám toho dost IP adresa Jestliže tento klient běží v MS Windows a timeout není nula, tak se pravděpodobně jedná o SSL bug! Nastavte timeout zpět na nulu. Pokud nechcete položku zadat stiskněte ENTER. Přišla Greeting zpráva Mód interaktivního zadávání parametrů. Pro přerušení zadejte Interní chyba: Nadřazený uzel '%s' neexistuje. Přeložená odpověď Přeložený příkaz Přerušeno uživatelem Neplatný XML dokument. ExpatError: %s Nesprávné použití závorek (childs). Nesprávné použití závorek (list). Nesprávné použití závorek (mode). Neplatná závorka. V zadání hodnoty klíčem je povolena jen jedna hodnota nebo prostý seznam. Neplatný vstupní formát Neplatný index parametru Neplatný kód odpovědi Už mě to nudí Seznam DNS Načíst soubor Odeslán login Login se nezdařil Odeslán logout V odpovědi chybí část result Chybí parametry. Požadované minimum je Modul pro odeslání souborů na EPP server. Jména která nejsou uvedena v seznamu disclose, jsou nastavena na opačnou hodnotu než má disclose flag. Žádný config Žádná data Help nebyl nalezen pro Žádná odpověď. EPP server neodpovídá. Nenalezen Není v registru: Objekt je dostupný. PARAMETRY Navázáno spojení na Parametr MUSÍ být hodnota z následujícího seznamu Privátní klíč nebyl nalezen Ukončit klienta. Stený význam má i "q" nebo "exit". Poruchy zasílejte na Aktivováno SSL spojení SSN (číslo sociálního pojištění) SSN číslo dokladu SSN číslo (Security social number) SSN typ čísla dokladu SYNTAXE Stejné jako help. Pro zobrazení detailů příkazu zadejte "help command-name". Poslat "poll ack" ihned po odeslání "poll req". Odeslat soubor na server. Pokud jméno souboru není zadáno zobrazí se aktuální adresář. Server není správně nakonfigurován. Obraťte se na správce serveru. Server nevrátil Greeting odpověď. Kontaktujte správce serveru. Odpověď serveru není validní! Relace zahájena Zapnout/vypnout potvrzení procesu odeslání editačních příkazů na server. Zapnutí/vypnutí externího validátoru XML dokumentů. Nastavení módu výpisu: 1 - stručný (default); 2 - plný; 3 - plný & XML zdroje. Start režimu interaktivního vkládání parametrů. Dočasný soubor pro ověření XML EPP validity se nepodařilo vytvořit. Důvod EPP příkaz "delete" se používá pro odebrání instance vybraného objektu. EPP příkazem "hello" si lze kdykoliv vyžádat od serveru odpověď "greeting". EPP příkaz "delete" se používá pro odebrání instance vybraného objektu. EPP příkaz "logout" se používá pro ukončení spojení s EPP serverem. EPP příkaz "poll" se používá k odběru servisních zpráv pro přihlášeného uživatele a ke zjištění počtu těchto zpráv uložených ve frontě. EPP příkaz "renew" se používá pro prodloužení platnosti vybraného objektu. EPP příkaz "update" se používá pro aktualizaci hodnot instance vybraného objektu. Tento program vyžaduje Python 2.4 nebo vyšší. Vaše verze je Zkuste Zapnout/vypnout barevný výstup. Zadejte Zadejte "help command" pro zobrazení detailů příkazu. Zadejte "help", "license" or "credits" pro zobrazení více informací. Pro deaktivaci validátoru zadejte %s Neznámý EPP příkaz. Vyberte jeden ze seznamu EPP příkazů (zadejte help). Neznámý příkaz Neznámé jméno parametru Neznámý typ části response Odpověď serveru nebyla rozpoznána Použití DPH VAT (daňový identifikátor) Validace je nastavena na Validátor byl deaktivován. Opětná aktivace se provede zadáním %s. Hodnota "%s" není povolena. Platná je: Údaj je povinný. MUSÍ být zadán: Mód rozsahu výpisu je Readline modul chybí, historie příkazů deaktivována. Více informací naleznete v README. Jste již zalogován Nejste připojeni! Pro připojení k serveru zadejte login. Nejste připojeni. Nejste zalogováni. Nejdříve zadejte login. Nejste zalogováni. Nejdříve musíte zadat login(). povoleny pouze hodnoty část add adresa část change město kontakt ID kontakt id jméno kontaktu kód země aktuální datum expirace data, pro které se nastaví příznak nezveřejňovat přepínač zveřejnit (default y) jméno domény vložen příklad fax index zprávy, povinné při op=ack! seznam DNS Počet položek v seznamu je překročen. Maximum je seznam o maximálně %d položkách. chybí jméno nové heslo oznámení na email nsset adresa jméno nssetu počet měsíců nebo roků nepovinný název organizace heslo období jednotka období (y rok(default), m měsíc) poll ack je PSČ poštovní informace typ požadavku vlastník domény část remove povinný povinný jen je-li tato část zadána č.p. stát nebo kraj ulice tech. kontakt technický kontakt libovolně velký seznam telefon město vaše kontaktní ID váš email vaše login jméno vaše jméno vaše heslo 