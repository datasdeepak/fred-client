#!/usr/bin/env python
# -*- coding: utf8 -*-
#
# $Id$
#
# Tento modul bude zpracovávat příkazy ze souboru,
# nebo z příkazové řádky.
import epplib.client_session

def main():
    client = epplib.client_session.Manager()
    #---------------------------------------------------
    if 1:
        # automatické připojení k serveru
        if not client.connect():
            # když se spojení nepodařilo navázat
            print '[batch] NOTES:\n',client.fetch_notes()
            print '[batch] ERRORS:\n',client.fetch_errors()
            return
        print client.fetch_notes() # zobrazit poznámky
    else:
        print u"Pro spojení se serverem zadeje: connect"
    #---------------------------------------------------
    print "[BATCH: START LOOP prompt]"
    while 1:
        command = raw_input("> (?-help, q-quit): ")
        if command in ('q','quit','exit','konec'):
            client.send_logout()
            break
        epp_doc = client.create_eppdoc_TEST(command)
        if epp_doc and epplib.client_session.is_epp_valid(epp_doc):
            epplib.client_session.debug_label('client command',epp_doc)
            if client.is_connected():
                client.send(epp_doc)          # odeslání dokumentu na server
                answer = client.receive()     # příjem odpovědi
                client.process_answer(answer) # zpracování odpovědi
            else:
                print "You are not connected! For connection type command: connect"
        if client.is_note():  print '[batch] NOTES:\n',client.fetch_notes()
        if client.is_error(): print '[batch] ERRORS:\n',client.fetch_errors()
    print "[BATCH: END LOOP prompt]"
    client.close()
    print "[END BATCH]"


if __name__ == '__main__':
    main()
