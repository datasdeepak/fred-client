��    �      �  �         �  �   �  C  S  �   �  B  ^  �  �    P  �   k  �   F  '   �  *   �          0     >     U     h     �  .   �     �     �     �       
   (     3     E     W     u  -   �     �  ,   �  ,   �          ,  '   5     ]     e  *   v     �     �  T   �          :  
   K  o   V  <   �  #        '  3   ;  /   o     �     �     �  $   �  $   �  "   $   "   G   J   j      �      �      �      �   	   !     !  '   !  #   D!  d   h!  	   �!     �!  '   �!  	   "     "     "  $   1"     V"     r"  
   �"     �"     �"     �"     �"  E   �"     #  F   '#  M   n#  U   �#  Y   $  E   l$  s   �$  I   &%  M   p%  H   �%  8   &  X   @&     �&     �&  H   �&  C   �&     /'     H'     X'     i'     �'     �'  
  �'  �  �*  @   Z-     �-     �-     �-  ,   �-  &   �-  ,   .     L.  @   \.     �.  <   �.  ?   �.     2/  G   I/     �/     �/     �/     �/  R   �/     #0     /0     40  
   <0  
   G0     R0     _0     l0  #   �0     �0     �0     �0  
   �0  '   �0     
1  #   1     :1     R1     Z1     _1     l1     y1  
   �1     �1     �1     �1     �1     �1  &   �1     �1     
2     2  
   *2  0   52  
   f2     q2     }2     �2     �2     �2     �2     �2     �2     �2     �2  	   3     3  
   3     '3  	   73     A3  .  O3  Q   ~4  �   �4  �   �5     W6  �  x7  x  9  �   {?  �   P@  :   �@  /   4A     dA     yA     �A     �A  $   �A  $   �A  /   
B     :B     MB  $   `B     �B     �B     �B     �B  0   �B     C  J   C     gC  )   yC  1   �C     �C  
   �C  =   �C  	   :D     DD  @   WD  "   �D     �D  �   �D     bE     |E  	   �E  �   �E  F   #F  +   jF     �F  ;   �F  1   �F     G     4G     JG  &   bG  (   �G  &   �G  &   �G  b    H     cH     ~H     �H  
   �H     �H     �H      �H  )    I  k   *I     �I     �I  ,   �I  	   �I  	   �I     �I  6   J     HJ     hJ  $   |J     �J     �J     �J  !   �J  B   �J     6K  Q   HK  O   �K  Q   �K  O   <L  K   �L  �   �L  R   vM  W   �M  H   !N  @   jN  [   �N     O     O  b   O  O   yO     �O     �O     �O     P     'P  $   FP  )  kP  �  �S  J   MV     �V     �V     �V  C   �V  (   W  >   @W     W  7   �W     �W  =   �W  ;   "X     ^X  Q   qX     �X     �X  
   �X     �X  `   Y     fY     tY     {Y  
   �Y  
   �Y     �Y  
   �Y     �Y  &   �Y     �Y  "   Z     (Z     7Z  $   ;Z  
   `Z  4   kZ  $   �Z     �Z     �Z     �Z     �Z     �Z      [     [  
   *[     5[     G[     M[  ,   U[     �[     �[     �[     �[  <   �[     �[     \     \  &   \     D\     J\     Z\     `\     n\     �\     �\     �\     �\     �\     �\     �\     �\     W   u   8   @           �   �               c      �   >   x          �   �       m   h   n   e   $   5       �   �       o                 F       	   �   :   �   �   %   N          p   
   d   ?   i   �   �      Y       �   b   r   +           �   y      [   �   4       v   q   k          �   �   2           A   `   �       I                �   �       V   X                L   !   �       ,   O   M   '   \   ;       -              �   ]       }       �   �   <   6   Z   �                �   �   ~   7      9   �   �   Q   �   �   G          &              l       ^   H   �      C   D      �   /       �       s   �          t   )   {           J       _   P   �   a   �   R       �      �       �       �   #   B      (   �          U   �   |              =   w       K       z           1           T   g   �   E   .          �       �   *   �   "   f   �       0       S   3   j            
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
 
${BOLD}Session commands:${NORMAL}
${BOLD}q${NORMAL} (or ${BOLD}quit${NORMAL}, ${BOLD}exit${NORMAL}) # quit this application
${BOLD}help${NORMAL} (or ${BOLD}h${NORMAL}, ${BOLD}?${NORMAL})  # display this help
${BOLD}license${NORMAL} # display license
${BOLD}credits${NORMAL} # display credits
${BOLD}connect${NORMAL} (or directly login) # connect to the server (for test only)
${BOLD}validate${NORMAL} [on/off] # set validation or display actual setting
${BOLD}poll-ack${NORMAL} [on/off] # send "poll ack" straight away after "poll req"
${BOLD}raw-c${NORMAL}[ommand] [xml]/${BOLD}d${NORMAL}[ict] # display raw command (instead of raw you can also type ${BOLD}src${NORMAL})
${BOLD}raw-a${NORMAL}[nswer] [xml]/${BOLD}d${NORMAL}[ict]  # display raw answer
${BOLD}confirm${NORMAL} ${BOLD}on${NORMAL}/[off] # confirm editable commands befor sending to the server
${BOLD}config${NORMAL} # display actual config
${BOLD}config${NORMAL} ${BOLD}create${NORMAL} # create default config file in user home folder.
${BOLD}send${NORMAL} [filename] # send selected file to the server (for test only). If param is not valid file the command shows folder.
${BOLD}colors${NORMAL} [on/off] # turn on/off colored output
${BOLD}verbose${NORMAL} [number] # set verbose mode: 1 - brief (default); 2 - full; 3 - full & XML sources
    SSN types can be: 
      op       number identity card
      rc       number of birth
      passport number of passport
      mpsv     number of Ministry of Labour and social affairs
      ico      number of company ${BOLD}${YELLOW}Start interactive input of params. To break type: ${NORMAL}${BOLD}!${NORMAL}[!!...] (one ${BOLD}!${NORMAL} for scope) (Value can be a list of max %d values.) (Value can be an unbouded list of values.) Actual config is Answer source Available EPP commands Broken connection. Certificate key file not found. Certificate names not set. Certificates missing. Try connect without SSL! Colors mode is Command source Command was sent to EPP server. Confirm has been set to Confirm is Connection broken Connection closed Create default config failed. DESCRIPTION Default config file saved. For more see help. Dir list Do you want send this command to the server? Document has wrong encoding. LookupError: %s EPP document is not valid EXAMPLES End of interactive input. [press enter] Example Example of input Fatal error: Create default config failed. For disable validator type For more type For stop interactive input type ! instead of value (or more "!" for leave sub-scope) Greeting message incomming Help for command IP address If this script runs under MS Windows and timeout is not zero, it is probably SLL bug! Set timeout back to zero. Impossible create connection. Required config values missing Impossible saving conf file. Reason Init SSL connection Instead "command" Select one from this list bellow: Internal Error: Master node '%s' doesn't exist. Interpreted answer Interpreted command Interrupt from user Invalid XML document. ExpatError: %s Invalid bracket definition (childs). Invalid bracket definition (list). Invalid bracket definition (mode). Invalid bracket. In key definition is only allowed a value or simple list. Invalid input format. Invalid parameter index Invalid response code LIST of DNS Load file Login failed Missing result in the response message. Missing values. Required minimum is Names what are not included into disclose list are set to opposite value of the disclose flag value. No config No data No response. EPP Server doesn't answer. Not found OPTIONS Open connection on host Param MUST be a value from this list Private key file not found. SSN (Security social number) SSN number SSN type SYNTAX Send logout Server answer is not valid! Server doesn't return Greeting message. Contact server administrator. Start session! Temporary file for verify XML EPP validity cannot been created. Reason The EPP "delete" command is used to remove an instance of an existing object. The EPP "hello" request a "greeting" response message from an EPP server at any time. The EPP "list" command is used to list all ID of an existing object owning by registrant. The EPP "logout" command is used to end a session with an EPP server. The EPP "poll" command is used to discover and retrieve service messages queued by a server for individual clients. The EPP "renew" command is used to extend validity of an existing object. The EPP "update" command is used to update an instance of an existing object. The server configuration is not valid. Contact the server administrator. This program needs Python 2.4 or higher. Your version is To start the interactive mode of input the command params type: ${BOLD}!command${NORMAL} Try Type Type "?command" (or "h(elp) command") for mode details about parameters. Unknown EPP command. Select one from EPP commands list (Type help). Unknown EPP command: %s. Unknown command Unknown command! Unknown parameter name Unknown response type Unknown server response Usage: python ccreg_client.py [OPTIONS]
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
                  example: --command='info-domain nic.cz'

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
 Used certificat is not signed by verified certificate authority. VAT VAT (Value-added tax) Validation process is Validator has been disabled. For enable type Value "%s" is not allowed here. Valid: Verbose mode can be set only to 1 or 2 or 3. Verbose mode is You are connected already. Type disconnect for close connection. You are logged already. You are not connected! For connection type: connect or login You are not connected! Type login for connection to the server. You are not connected. You are not logged. You must call login() before working on the server. You has been disconnected. accept only values add part address ccReg client version 1.1 Type "help", "license" or "credits" for more information. change part city contact contact ID contact id contact name country code current expiration date data for with is set the flag value disclose disclose flag (default y) domain name fax number index of message, required with op=ack! list of DNS list of values overflow. Maximum is list with max %d items. missing name new password notify email nsset address nsset name number of months or years optional organisation name password period period unit (y year(default), m month) poll ack is postal code postal informations query type readline module missing - cmd history is diabled registrant remove part required required only if part is set sp state or province street tech contact technical contact unbounded list voice (phone number) your city your contact ID your email your login name your name your password Project-Id-Version: 1.0
Report-Msgid-Bugs-To: 
POT-Creation-Date: 2006-08-16 16:08+0200
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
 
${BOLD}${GREEN}Příkazy relace (session):${NORMAL}
${BOLD}q${NORMAL} (nebo ${BOLD}quit${NORMAL}, ${BOLD}exit${NORMAL}) # ukončit tuto aplikaci
${BOLD}help${NORMAL} (or ${BOLD}h${NORMAL}, ${BOLD}?${NORMAL})  # zobrazit tento help
${BOLD}license${NORMAL} # zobrazit licenci
${BOLD}credits${NORMAL} # zobrazit credits
${BOLD}connect${NORMAL} (nebo přímo login) ${CYAN}# připojení k serveru(jen pro testování)${NORMAL}
${NORMAL}
${BOLD}validate${NORMAL} [on/off] ${CYAN}# nastavení validace nebo zjištění aktuálního stavu${NORMAL}
${BOLD}poll-ack${NORMAL} [on/off] ${CYAN}# pošle "poll ack" hned za příkazem "poll req"${NORMAL}
${BOLD}raw-c${NORMAL}[ommand] [xml]/${BOLD}d${NORMAL}[ict] ${CYAN}# zobrazit zdrojový tvar příkazu${NORMAL} (místo raw můžete zadat také ${BOLD}src${NORMAL})
${BOLD}raw-a${NORMAL}[nswer] [xml]/${BOLD}d${NORMAL}[ict]  ${CYAN}# zobrazit zdrojový tvar odpovědi${NORMAL}
${BOLD}confirm${NORMAL} ${BOLD}on${NORMAL}/[off]  ${CYAN}# potvrzení editačních příkazů před odesláním na server${NORMAL}
${BOLD}config${NORMAL} ${CYAN}# zobrazení aktuálních hodnot v config souboru (nebo defaultu)${NORMAL}
${BOLD}config${NORMAL} ${BOLD}create${NORMAL} ${CYAN}# vytvoření defaultního config souboru v adresáři uživatele (/home/user).${NORMAL}
${BOLD}send${NORMAL} [jméno] ${CYAN}# odešle soubor daného jména na server (jen testování). Pokud jméno není platný soubor, tak příkaz zobrazuje adresář.${NORMAL}
${BOLD}colors${NORMAL} [on/off] # zapnout/vypnout barevný výstup
${BOLD}verbose${NORMAL} [number] # nastavit mód výpisu: 1 - stručný (default); 2 - plný; 3 - plný & XML zdroje
    SSN typ může být: 
      op       číslo občanského průkazu
      rc       rodné číslo
      passport číslo pasu
      mpsv     číslo Ministerstva práce a sociálních věcí
      ico      IČO ${BOLD}${YELLOW}Start interaktivního zadávání parametrů. Pro ukončení zadejte: ${NORMAL}${BOLD}!${NORMAL}[!!...] (jeden ${BOLD}!${NORMAL} pro každou podskupinu) (Hodnota může být seznam o max. velikosti %d položek.) (Hodnota může být libovolně velký seznam.) Aktuální config je Zdrojová odpověď Dostupné EPP příkazy Spojení bylo přerušeno. Soubor s certifikátem nebyl nalezen Jména certifikátů nejsou zadána  Certifikát chybí. Zkouším spojení bez SSL! Mód barevnosti je Zdrojový příkaz Příkaz byl odeslán na EPP server. Potvrzení bylo nastaveno na Potvrzení je nastaveno na Spojení přerušeno Spojení uzavřeno Vytvoření defaultního config souboru selhalo. POPIS Defaultní config soubor byl uložen. Další informace naleznete v helpu. Výpis adresáře Chcete odeslat tento poříkaz na server? Dokument má chybné kódování. LookupError: %s EPP dokument není validní PŘÍKLADY Konec interaktivního zadání parametrů. [stiskněte enter] Příklad Příklad zadání Fatální chyba: Vytvoření defaultních config hodnot selhalo. Pro deaktivaci validátoru zadejte Pro více informací zadejte Interaktivní zadávání parametrů se přeruší zadáním "!" (nebo vícevykřičníků najednou, když jste v podskupině parametrů) Přišla Greeting zpráva Help pro příkaz IP adresa Jestliže tento skript běží v MS Windows a timeout není nula, tak se pravděpodobně jedná o SSL bug! Nastavte timeout zpět na nulu. Není možné vytvořit spojení. Požadované hodnoty z config chybí Není možné uložit config soubor. Důvod Aktivováno SSL spojení Místo "příkaz" vyberte jeden z následujícího seznamu: Interní chyba: Nadřazený uzel '%s' neexistuje. Přeložená odpověď Přeložený příkaz Přerušeno uživatelem Neplatný XML dokument. ExpatError: %s Nesprávné použití závorek (childs). Nesprávné použití závorek (list). Nesprávné použití závorek (mode). Neplatná závorka. V zadání hodnoty klíčem je povolena jen jedna hodnota nebo prostý seznam. Neplatný vstupní formát Neplatný index parametru Neplatný kód odpovědi Seznam DNS Načíst soubor Login se nezdařil V odpovědi chybí část result Chybí parametry. Požadované minimum je Jména která nejsou uvedena v seznamu disclose, jsou nastavena na opačnou hodnotu než má disclose flag. Žádný config Žádná data Žádná odpověď. EPP server neodpovídá. Nenalezen PARAMETRY Navázáno spojení na host Parametr MUSÍ být hodnota z následujícího seznamu Privátní klíč nebyl nalezen SSN číslo dokladu SSN číslo (Security social number) SSN typ čísla dokladu SYNTAXE Odeslán logout Odpověď serveru není validní! Server nevrátil Greeting odpověď. Kontaktujte správce serveru. Relace zahájena! Dočasný soubor pro ověření XML EPP validity se nepodařilo vytvořit. Důvod EPP příkaz "delete" se používá pro odebrání instance vybraného objektu. EPP příkazem "hello" si lze kdykoliv vyžádat od serveru odpověď "greeting". EPP příkaz "delete" se používá pro odebrání instance vybraného objektu. EPP příkaz "logout" se používá pro ukončení spojení s EPP serverem. EPP příkaz "poll" se používá k odběru servisních zpráv pro přihlášeného uživatele a ke zjištění počtu těchto zpráv uložených ve frontě. EPP příkaz "renew" se používá pro prodloužení platnosti vybraného objektu. EPP příkaz "update" se používá pro aktualizaci hodnot instance vybraného objektu. Server není správně nakonfigurován. Obraťte se na správce serveru. Tento program vyžaduje Python 2.4 nebo vyšší. Vaše verze je Interaktivní režim zadávání parametrů příkazu se spustí: ${BOLD}!příkaz${NORMAL} Zkuste Zadejte Více informací o parametrech příkazu získáte zadáním "?příkaz" (nebo "h(elp) příkaz"). Neznámý EPP příkaz. Vyberte jeden ze seznamu EPP příkazů (zadejte help). Neznámý EPP příkaz: %s. Neznámý příkaz Neznámý příkaz! Neznámé jméno parametru Neznámý typ části response Odpověď serveru nebyla rozpoznána Použití: python ccreg_console.py [OPTIONS]
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
                  příklad: --command='info-domain nic.cz'

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
 Použitý certifikát není podepsán uznávanou certifikační autoritou. DPH VAT (daňový identifikátor) Validace je nastavena na Validátor byl deaktivován. Opětná aktivace se provede zadáním Hodnota "%s" není povolena. Platná je: Mód výstupu může být nastaven jen na hodnoty 1, 2 nebo 3. Mód rozsahu výpisu je Již jste připojeni. Pro odpojení zadejte disconnect. Jste již zalogován Nejste připojeni! Po připojení zadejte: connect nebo login Nejste připojeni! Pro připojení k serveru zadejte login. Nejste připojeni. Nejste zalogováni. Před samotnou prací na serveru musíte volat funkci login() Spojení bylo ukončeno. povoleny pouze hodnoty část add adresa ccReg client verze 1.1 Zadejte "help", "license" nebo "credits" pro zobrazení více informací. část change město kontakt kontakt ID kontakt id jméno kontaktu kód země aktuální datum expirace data, pro které se nastaví příznak nezveřejňovat přepínač zveřejnit (default y) jméno domény fax index zprávy, povinné při op=ack! seznam DNS Počet položek v seznamu je překročen. Maximum je seznam o maximálně %d položkách. chybí jméno nové heslo oznámení na email nsset adresa jméno nssetu počet měsíců nebo roků nepovinný název organizace heslo období jednotka období (y rok(default), m měsíc) poll ack je PSČ poštovní informace typ požadavku readline modul chybí - historie příkazů je deaktivována vlastník domény část remove povinný povinný jen je-li tato část zadána č.p. stát nebo kraj ulice tech. kontakt technický kontakt libovolně velký seznam telefon město vaše kontaktní ID váš email vaše login jméno vaše jméno vaše heslo 