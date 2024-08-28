# *Basic Network Scanner* 

## Per prima cosa dobbiamo definire: *ARP* {Address Resolution Protocol}

### ARP è un protocollo utilizzato per risolvere gli indirizzi IP in indirizzi *MAC*(Media Access Controll) all'interno di una rete locale *LAN*.

*COME FUNZIONA ARP ?*

*ARP REQUEST*
Quando un dispositivo su una rete locale deve inviare un pacchetto ad un altro dispositivo non conoscendo il suo MAC, invia una richiesta ARP (ARP REQUEST).
Questa richiesta è un pacchetto che contiene l'ip di destinazione per cui si richiede il MAC.

    ES: Richiesta per IP 192.168.0.3 --> Risposta con eventuale MAC

*ARP REPLY*
Tutti i dispositivi sulla rete ricevono questa richiesta, ma solo il dispositivo con l'IP specificato nella Request risponde con una Reply.
Questo pacchetto Reply conterrà quindi il MAC del dispositivo.

    ES: Richiesta per IP 192.168.0.3 --> MAC : 00:1A:2B:3C:4D:5E

*CACHING*
Una volta che il dispositivo risponde e quindi si riceve una risposta ARP, le informazioni vengono memorizzate (caché) nella sua tabella ARP per un tempo specificato,
cosicché si eviti di inviare una richiesta ARP ogni volta che si debba comunicare con lo stesso dispositivo.

*BROADCAST*
Le _richieste_ ARP sono inviate come broadcast, ovvero a tutti i dispositivi sulla stessa rete locale.
Le _risposte_ ARP sono inviate come UNICAST, cioè direttamente al dispositivo che ha fatto richiesta.

# **UTILITÀ DI ARP**

## *Risolvere IP in MAC*
ARP è essenziale per il funzionamento della comunicazione all'interno di una LAN, poichè i pacchetti devono essere incapsulati con l'indirizzo MAC corretto per essere trasmessi fisicamente sulla rete

## *Diagnosi della rete*
Strumenti come arp-scan ed arp, permettono di visualizzare e diagnosticare le tabelle ARP risolvendo problemi di rete.

*--------------*

# Andiamo ora ad analizzare il Programma...
In questo programma abbiamo utilizzato la libreria scapy [Scapy Documentation](https://scapy.readthedocs.io/en/latest/)

Questo programma ci permette di eseguire una scansione ARP su una rete locale, potendo quindi mappare gli indirizzi IP con i relativi MAC.

1) Importazioni delle funzioni necessarie:

  *from scapy.layers.l2 import ARP, Ether
   from scapy.all import srp*

ARP: classe utilizzata da scapy per creare pacchetti ARP, usata per risolvere IP in MAC sulla LAN

Ether: classe che rappresenta un frame Ethernet, unità di base di comunicazione sulla rete fisica

srp: "Send and Receive Packets", usata per inviare pacchetti e ricevere risposte in modo _sincrono_ (attendiamo la risposta prima di continuare)

2) Metodo scan(ip):

   *arp_request = ARP(pdst=ip)* --> creazione pacchetto arp con il campo pdst impostato sugli ip da scansionare (forniti come input).
    Qui abbiamo l'ARP Request

    *broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")* --> creazione di un frame Ethernet con destinazione (dst) impostato a ff:ff:ff:ff:ff:ff che è l'indirizzo broadcast.

    *arp_request_broadcast = broadcast / arp_request* --> combinazione dei frame Ethernet con il pacchetto ARP, in scapy "/" viene usato per impilare i livelli del pacchetto, 
    ovvero crea un pacchetto completo che verrà inviato in broadcast alla rete
   
    *answered_list = srp(arp_request_broadcast, timeout=1, verbose=False)[0]*

--> invia il pacchetto combinato ed attende la risposta...
srp : invia il pacchetto e riceve le risposte

timeout=1 : attende un secondo

verbose=False disabilita l'output dettagliato di scapy durante l'esecuzione

[0] : significa che stiamo prendendo solo la lista delle risposte ricevute, ignoriamo i pacchetti che non hanno risposta


3) Elaborazione delle risposte:

    *results = []* --> inizializza una lista vuota

    *for element in answered_list:* -->Itera ciascun pacchetto che ha ricevuto risposta

    *result = {"ip": element[1].psrc, "mac": element[1].hwsrc}* 
   --> Estrae l'_IP sorgente_ (psrc) ed estrae il _MAC sorgente_ (hwsrc) dalla risposta.
    Ogni element[1] contiene la risposta ARP.

    *results.append(result)* -->  Aggiunge ai risultati

    *return results* --> Ritorna la lista

4) Visualizzazione dei Risultati:

    *def display_results(results):* --> Prende la lista di risultati e li stampa in modo leggibile

    *print("IP Address\t\tMAC Address")* --> stampa l'intestazione della tabella

    *print("--------------------------------------")* --> semplice stampa

    *for result in results:
        print(result["ip"] + "\t\t" + result["mac"])* --> itera su ciascun risultato e lo stampa in modo "personalizzato"

5) Esecuzione e dati

   *target_ip = "192.168.0.1/24"* --> Il target per scansionare l'intera sottorete "/24" della rete in questione
 
   *scan_results = scan(target_ip)* --> Chiama la funzione scan passandogli il target e memorizza in scan_result

   *display_results(scan_results)* --> Funzione display_result per la visualizzazione dei risultati
 



#### [Tutorial Python](https://docs.python.org/3/tutorial/)