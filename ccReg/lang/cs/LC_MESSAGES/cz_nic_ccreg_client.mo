��    �                   �   !  C  �  �     B  �  �    �   �  '   �  *   �     �     �          $     ?     P     c     �  .   �     �     �     �       
   #     .     @     R     p  -   |     �  %   �  &   �                "  %   A  ,   g  ,   �     �     �     �  '   �            *   +     V     q     �     �     �  
   �  o   �  #   A  <   e  #   �     �  -   �  /        8     K     _  $   s  $   �  "   �  "   �  J        N     d     |     �  	   �     �  8   �  '   �  #     d   :  	   �     �     �  '   �  	   �  %   �          '  $   ?     d  /   �     �     �  
   �     �     �  ;   �  /   3   M   c      �      �   E   �   D   !  4   d!  H   �!     �!  7   �!  F   )"  M   p"  U   �"  Y   #  E   n#  s   �#  I   ($  M   r$  H   �$  8   	%     B%     F%     b%  6   g%  C   �%     �%     �%     	&     &  
  7&  �  B)  @   �+     $,     (,     >,  ,   T,  &   �,  ,   �,     �,  @   �,     &-  <   >-  ?   {-     �-  G   �-     .     5.     H.     Q.  I   Y.     �.     �.  
   �.  
   �.     �.     �.     �.  #   �.      /     )/     C/  
   O/  '   Z/     �/  #   �/     �/     �/     �/     �/     �/     �/  
   �/     
0     $0     -0     ?0     H0  &   O0     v0     �0     �0  
   �0  0   �0  
   �0     �0     �0     �0     1     1     01     71     D1     V1     e1  	   z1     �1  
   �1     �1  	   �1     �1  .  �1  Q   �2  �   H3  �   4     �4  �  �5  �   z7  :   O8  /   �8     �8     �8     �8     �8     9     )9  $   D9  $   i9  /   �9     �9     �9  $   �9     	:     &:     A:     V:  0   i:     �:  J   �:     �:  !   �:  !   ;     A;     S;  5   e;  +   �;  )   �;  1   �;     #<     ?<  
   E<  =   P<  	   �<     �<  @   �<  "   �<  -   =     ==     Z=     t=  	   �=  �   �=  /   >  F   K>  +   �>     �>  E   �>  1   ?     O?     f?     |?  &   �?  (   �?  &   �?  &   @  b   2@     �@     �@     �@  
   �@     �@     �@  ?   A      QA  )   rA  k   �A     B     B     &B  ,   =B  	   jB  &   tB  	   �B     �B  6   �B     �B  7   C     PC     fC  $   zC     �C     �C  Q   �C  1   D  ^   CD     �D  !   �D  B   �D  P   E  8   hE  U   �E     �E  5   	F  Q   ?F  O   �F  Q   �F  O   3G  K   �G  �   �G  R   mH  W   �H  H   I  @   aI     �I  !   �I     �I  9   �I  O   J     ]J     pJ     �J  $   �J  )  �J  �  �M  J   �P     �P      Q     Q  C   7Q  (   {Q  >   �Q     �Q  7   �Q     3R  =   HR  ;   �R     �R  Q   �R     'S     @S  
   WS     bS  W   iS     �S     �S  
   �S  
   �S     �S  
   �S     T  &   !T     HT  "   XT     {T     �T  $   �T  
   �T  4   �T  $   �T     U     U     &U     2U     FU     SU     aU  
   }U     �U     �U     �U  ,   �U     �U     �U     �U     �U  <   
V     GV     YV     gV  &   pV     �V     �V     �V     �V     �V     �V     �V     �V     �V     W     W     /W     <W            =       (   S   O       �   z   \   0   �   �   M   6   �       �       
      7           '       R          Z   �   I   P   `       -          �      3           {   �   y   c   m      @   �      k   F   #      �   �   �   �   q   ?   �       �      �           |       g   �   �   G      W   !          �       d   �   �      �      .   �       U   	   +   �         4       >       b   i   ^      �   �   L   �       �   �   &           �   t          u   K           o           /   ,   �   �               �   n       j      )   ;       �   :   �       �   1       ~   a   �   �      B           N       �             $   e   �   h   �   �   T   s   �           p           H   �   E   D              [           _   ]   J   �          l   %   w   r   �   �   �   }   �   �              Y       V   �   v      �           �           A   C   �   �   �       �   X       �   9   �   �       �   �          5      Q   �         f       "   8   <           *           2   �   �   x    
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
      ico      number of company (Value can be a list of max %d values.) (Value can be an unbouded list of values.) Actual config is Answer source Available EPP commands Available session commands Available values Broken connection. Certificate key file not found. Certificate names not set. Certificates missing. Try connect without SSL! Colors mode is Command source Command was sent to EPP server. Confirm has been set to Confirm is Connection broken Connection closed Create default config failed. DESCRIPTION Default config file saved. For more see help. Dir list Display XML source of the EPP answer. Display XML source of the EPP command. Display credits. Display license. Display or create config file. Display this help or command details. Do you want send this command to the server? Document has wrong encoding. LookupError: %s EPP document is not valid ERROR EXAMPLES End of interactive input. [press enter] Example Example of input Fatal error: Create default config failed. For disable validator type For list all commands type For more type Greeting message incomming Help for command IP address If this script runs under MS Windows and timeout is not zero, it is probably SLL bug! Set timeout back to zero. If you don't fill item press ENTER. Impossible create connection. Required config values missing Impossible saving conf file. Reason Init SSL connection Interactive input params mode. For BREAK type Internal Error: Master node '%s' doesn't exist. Interpreted answer Interpreted command Interrupt from user Invalid XML document. ExpatError: %s Invalid bracket definition (childs). Invalid bracket definition (list). Invalid bracket definition (mode). Invalid bracket. In key definition is only allowed a value or simple list. Invalid input format. Invalid parameter index Invalid response code LIST of DNS Load file Login failed Make connection between client and server without login. Missing result in the response message. Missing values. Required minimum is Names what are not included into disclose list are set to opposite value of the disclose flag value. No config No data No help available for No response. EPP Server doesn't answer. Not found Not in registry: Object is available. OPTIONS Open connection on host Param MUST be a value from this list Private key file not found. Quit the client. Same effect has "q" or "exit". Report bugs to SSN (Security social number) SSN number SSN type SYNTAX Same as help. For command details type "help command-name". Send "poll ack" straight away after "poll req". Send any file to the server. If filename missing command shows actual folder. Send logout Server answer is not valid! Server doesn't return Greeting message. Contact server administrator. Set on/off confirmation for sending editable commands to the server. Set on/off external validation of the XML documents. Set verbose mode: 1 - brief (default); 2 - full; 3 - full & XML sources. Start session! Start the interactive mode of the input command params. Temporary file for verify XML EPP validity cannot been created. Reason The EPP "delete" command is used to remove an instance of an existing object. The EPP "hello" request a "greeting" response message from an EPP server at any time. The EPP "list" command is used to list all ID of an existing object owning by registrant. The EPP "logout" command is used to end a session with an EPP server. The EPP "poll" command is used to discover and retrieve service messages queued by a server for individual clients. The EPP "renew" command is used to extend validity of an existing object. The EPP "update" command is used to update an instance of an existing object. The server configuration is not valid. Contact the server administrator. This program needs Python 2.4 or higher. Your version is Try Turn on/off colored output. Type Type "help command" to get help on particular command. Unknown EPP command. Select one from EPP commands list (Type help). Unknown command Unknown parameter name Unknown response type Unknown server response Usage: python ccreg_client.py [OPTIONS]
Client for communication with EPP server.

OPTIONS with values:
    -s --session  name of session used for connect to the EPP server
                  session values are read from config file
    -h --host     host name (overwrite config value)
    -u --user     user name (overwrite config value)
    -p --password (overwrite config value)
    -l --lang     language of session
    -v --verbose  display modes: 1,2,3; default: 1
                  1 - essensial values
                  2 - all returned values
                  3 - display XML sources
    -c --command  send command to the EPP server
                  example: --command='info_domain nic.cz'

OPTIONS:
    -r --colors   set on colored output
    -? --help     this help
 Usage: python ccreg_console.py [OPTIONS]
Console for communication with EPP server.

OPTIONS with values:
    -s --session  name of session used for connect to the EPP server
                  session values are read from config file
    -h --host     host name (overwrite config value)
    -u --user     user name (overwrite config value)
    -p --password (overwrite config value)
    -l --lang     language of session
    -v --verbose  display modes: 1,2,3; default: 1
                  1 - essensial values
                  2 - all returned values
                  3 - display XML sources
OPTIONS:
    -r --colors   set on colored output
    -? --help     this help
 Used certificat is not signed by verified certificate authority. VAT VAT (Value-added tax) Validation process is Validator has been disabled. For enable type Value "%s" is not allowed here. Valid: Verbose mode can be set only to 1 or 2 or 3. Verbose mode is You are connected already. Type disconnect for close connection. You are logged already. You are not connected! For connection type: connect or login You are not connected! Type login for connection to the server. You are not connected. You are not logged. You must call login() before working on the server. You has been disconnected. accept only values add part address ccRegClient 1.1
Type "help", "license" or "credits" for more information. change part city contact ID contact id contact name country code current expiration date data for with is set the flag value disclose disclose flag (default y) domain name fax number index of message, required with op=ack! list of DNS list of values overflow. Maximum is list with max %d items. missing name new password notify email nsset address nsset name number of months or years optional organisation name password period period unit (y year(default), m month) poll ack is postal code postal informations query type readline module missing - cmd history is diabled registrant remove part required required only if part is set sp state or province street tech contact technical contact unbounded list voice (phone number) your city your contact ID your email your login name your name your password Project-Id-Version: 1.0
Report-Msgid-Bugs-To: 
POT-Creation-Date: 2006-08-29 12:26+0200
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
      ico      IČO (Hodnota může být seznam o max. velikosti %d položek.) (Hodnota může být libovolně velký seznam.) Aktuální config je Zdrojová odpověď Dostupné EPP příkazy Dostupné session příkazy Povolené hodnoty Spojení bylo přerušeno. Soubor s certifikátem nebyl nalezen Jména certifikátů nejsou zadána  Certifikát chybí. Zkouším spojení bez SSL! Mód barevnosti je Zdrojový příkaz Příkaz byl odeslán na EPP server. Potvrzení bylo nastaveno na Potvrzení je nastaveno na Spojení přerušeno Spojení uzavřeno Vytvoření defaultního config souboru selhalo. POPIS Defaultní config soubor byl uložen. Další informace naleznete v helpu. Výpis adresáře Zobrazit XML zdroj EPP odpovědi. Zobrazit XML zdroj EPP příkazu. Zobrazit credits. Zobrazit licenci. Zobrazení nebo vytvoření konfiguračního souboru. Zobrazit tento help nebo detaily příkazu. Chcete odeslat tento poříkaz na server? Dokument má chybné kódování. LookupError: %s EPP dokument není validní CHYBA PŘÍKLADY Konec interaktivního zadání parametrů. [stiskněte enter] Příklad Příklad zadání Fatální chyba: Vytvoření defaultních config hodnot selhalo. Pro deaktivaci validátoru zadejte Pro výpis celého seznamu příkazů zadejte Pro více informací zadejte Přišla Greeting zpráva Help pro příkaz IP adresa Jestliže tento skript běží v MS Windows a timeout není nula, tak se pravděpodobně jedná o SSL bug! Nastavte timeout zpět na nulu. Pokud nechcete položku zadat stiskněte ENTER. Není možné vytvořit spojení. Požadované hodnoty z config chybí Není možné uložit config soubor. Důvod Aktivováno SSL spojení Mód interaktivního zadávání parametrů. Pro přerušení zadejte Interní chyba: Nadřazený uzel '%s' neexistuje. Přeložená odpověď Přeložený příkaz Přerušeno uživatelem Neplatný XML dokument. ExpatError: %s Nesprávné použití závorek (childs). Nesprávné použití závorek (list). Nesprávné použití závorek (mode). Neplatná závorka. V zadání hodnoty klíčem je povolena jen jedna hodnota nebo prostý seznam. Neplatný vstupní formát Neplatný index parametru Neplatný kód odpovědi Seznam DNS Načíst soubor Login se nezdařil Navázání spojení mezi klientem a serverem bez zalogování. V odpovědi chybí část result Chybí parametry. Požadované minimum je Jména která nejsou uvedena v seznamu disclose, jsou nastavena na opačnou hodnotu než má disclose flag. Žádný config Žádná data Help nebyl nalezen pro Žádná odpověď. EPP server neodpovídá. Nenalezen Není v registru: Objekt je dostupný. PARAMETRY Navázáno spojení na host Parametr MUSÍ být hodnota z následujícího seznamu Privátní klíč nebyl nalezen Ukončit klienta. Stený význam má i "q" nebo "exit". Poruchy zasílejte na SSN číslo dokladu SSN číslo (Security social number) SSN typ čísla dokladu SYNTAXE Stejné jako help. Pro zobrazení detailů příkazu zadejte "help command-name". Poslat "poll ack" ihned po odeslání "poll req". Odeslat soubor na server. Pokud jméno souboru není zadáno zobrazí se aktuální adresář. Odeslán logout Odpověď serveru není validní! Server nevrátil Greeting odpověď. Kontaktujte správce serveru. Zapnout/vypnout potvrzení procesu odeslání editačních příkazů na server. Zapnutí/vypnutí externího validátoru XML dokumentů. Nastavení módu výpisu: 1 - stručný (default); 2 - plný; 3 - plný & XML zdroje. Relace zahájena! Start režimu interaktivního vkládání parametrů. Dočasný soubor pro ověření XML EPP validity se nepodařilo vytvořit. Důvod EPP příkaz "delete" se používá pro odebrání instance vybraného objektu. EPP příkazem "hello" si lze kdykoliv vyžádat od serveru odpověď "greeting". EPP příkaz "delete" se používá pro odebrání instance vybraného objektu. EPP příkaz "logout" se používá pro ukončení spojení s EPP serverem. EPP příkaz "poll" se používá k odběru servisních zpráv pro přihlášeného uživatele a ke zjištění počtu těchto zpráv uložených ve frontě. EPP příkaz "renew" se používá pro prodloužení platnosti vybraného objektu. EPP příkaz "update" se používá pro aktualizaci hodnot instance vybraného objektu. Server není správně nakonfigurován. Obraťte se na správce serveru. Tento program vyžaduje Python 2.4 nebo vyšší. Vaše verze je Zkuste Zapnout/vypnout barevný výstup. Zadejte Zadejte "help command" pro zobrazení detailů příkazu. Neznámý EPP příkaz. Vyberte jeden ze seznamu EPP příkazů (zadejte help). Neznámý příkaz Neznámé jméno parametru Neznámý typ části response Odpověď serveru nebyla rozpoznána Použití: python ccreg_console.py [OPTIONS]
Konzole pro komunikace s EPP serverem.

OPTIONS s hodnotami:
    -s --session  název session, který se má použít pro spojení s EPP serverem
                  session hodnoty jsou načteny z config souboru
    -h --host     jméno host (přepíše config hodnotu)
    -u --user     jméno user (přepíše config hodnotu)
    -p --password heslo (přepíše config hodnotu)
    -l --lang     jazyková verze
    -v --verbose  mód výpisu: 1,2,3; default: 1
                  1 - zkrácený
                  2 - plný
                  3 - plný & XML zdroje
    -c --command  odeslání příkatu na EPP server
                  příklad: --command='info_domain nic.cz'

OPTIONS:
    -r --colors   zapnutí barevného výstupu
    -? --help     tento help
 Použití: python ccreg_console.py [OPTIONS]
Konzole pro komunikace s EPP serverem.

OPTIONS s hodnotami:
    -s --session  název session, který se má použít pro spojení s EPP serverem
                  session hodnoty jsou načteny z config souboru
    -h --host     jméno host (přepíše config hodnotu)
    -u --user     jméno user (přepíše config hodnotu)
    -p --password heslo (přepíše config hodnotu)
    -l --lang     jazyková verze
    -v --verbose  mód výpisu: 1,2,3; default: 1
                  1 - zkrácený
                  2 - plný
                  3 - plný & XML zdroje
OPTIONS:
    -r --colors   zapnutí barevného výstupu
    -? --help     tento help
 Použitý certifikát není podepsán uznávanou certifikační autoritou. DPH VAT (daňový identifikátor) Validace je nastavena na Validátor byl deaktivován. Opětná aktivace se provede zadáním Hodnota "%s" není povolena. Platná je: Mód výstupu může být nastaven jen na hodnoty 1, 2 nebo 3. Mód rozsahu výpisu je Již jste připojeni. Pro odpojení zadejte disconnect. Jste již zalogován Nejste připojeni! Po připojení zadejte: connect nebo login Nejste připojeni! Pro připojení k serveru zadejte login. Nejste připojeni. Nejste zalogováni. Před samotnou prací na serveru musíte volat funkci login() Spojení bylo ukončeno. povoleny pouze hodnoty část add adresa ccRegClient 1.1
Zadejte "help", "license" or "credits" pro zobrazení více informací. část change město kontakt ID kontakt id jméno kontaktu kód země aktuální datum expirace data, pro které se nastaví příznak nezveřejňovat přepínač zveřejnit (default y) jméno domény fax index zprávy, povinné při op=ack! seznam DNS Počet položek v seznamu je překročen. Maximum je seznam o maximálně %d položkách. chybí jméno nové heslo oznámení na email nsset adresa jméno nssetu počet měsíců nebo roků nepovinný název organizace heslo období jednotka období (y rok(default), m měsíc) poll ack je PSČ poštovní informace typ požadavku readline modul chybí - historie příkazů je deaktivována vlastník domény část remove povinný povinný jen je-li tato část zadána č.p. stát nebo kraj ulice tech. kontakt technický kontakt libovolně velký seznam telefon město vaše kontaktní ID váš email vaše login jméno vaše jméno vaše heslo 