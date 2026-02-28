import datetime

comuni = [
    ("Roma", "H501"),
    ("Milano", "F205"),
    ("Napoli", "F839"),
    ("Torino", "L219"),
    ("Palermo", "G273"),
    ("Firenze", "D612"),
    ("Bologna", "A944"),
    ("Venezia", "L736"),
    ("Bari", "A662"),
    ("Catania", "C351"),
]

VALORI_PARI = {
    '0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,
    'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,
    'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,
    'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25
}

VALORI_DISPARI = {
    '0':1,'1':0,'2':5,'3':7,'4':9,'5':13,'6':15,'7':17,'8':19,'9':21,
    'A':1,'B':0,'C':5,'D':7,'E':9,'F':13,'G':15,'H':17,'I':19,'J':21,
    'K':2,'L':4,'M':18,'N':20,'O':11,'P':3,'Q':6,'R':8,'S':12,
    'T':14,'U':16,'V':10,'W':22,'X':25,'Y':24,'Z':23
}

CODICI_MESE = {
    1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'H',
    7:'L', 8:'M', 9:'P', 10:'R', 11:'S', 12:'T'
}

def chiediCognome():
    cognome_valido = False
    while not cognome_valido:
        cognome = input("Cognome: ").strip()
        if cognome != "":
            cognome_valido = True
        else:
            print("Errore: campo obbligatorio.")
    cognome_senza_spazi = ""
    for carattere in cognome:
        if carattere != " ":
            cognome_senza_spazi += carattere
    cognome_maiuscolo = cognome_senza_spazi.upper()
    return cognome_maiuscolo

def chiediDataNascita():
    data_valida = False
    while not data_valida:
        testo_data = input("Data di nascita (gg/mm/aaaa): ").strip()
        parti = testo_data.split("/")
        if len(parti) == 3:
            giorno_str = parti[0]
            mese_str = parti[1]
            anno_str = parti[2]
            if len(giorno_str) == 2 and len(mese_str) == 2 and len(anno_str) == 4:
                if giorno_str.isdigit() and mese_str.isdigit() and anno_str.isdigit():
                    giorno = int(giorno_str)
                    mese = int(mese_str)
                    anno = int(anno_str)
                    try:
                        data = datetime.datetime(anno, mese, giorno)
                        data_valida = True
                    except ValueError:
                        print("Errore: data non valida. Usa gg/mm/aaaa.")
                else:
                    print("Errore: formato non valido. Usa gg/mm/aaaa.")
            else:
                print("Errore: formato non valido. Usa gg/mm/aaaa.")
        else:
            print("Errore: formato non valido. Usa gg/mm/aaaa.")
    return data

def calcolaCodiceComune(comune):
    codice_trovato = ""
    for nome_comune, codice in comuni:
        if nome_comune.upper() == comune.upper():
            codice_trovato = codice
    return codice_trovato


def calcolaCodiceAnno(data):
    anno_completo = str(data.year)
    ultime_due_cifre = anno_completo[2] + anno_completo[3]
    return ultime_due_cifre


def calcolaCodiceCognome(cognome):
    consonanti = []
    vocali = []
    for carattere in cognome:
        if carattere in "AEIOU":
            vocali.append(carattere)
        else:
            consonanti.append(carattere)
    codice = []
    for c in consonanti:
        codice.append(c)
    for v in vocali:
        codice.append(v)
    while len(codice) < 3:
        codice.append('X')
    risultato = codice[0] + codice[1] + codice[2]
    return risultato

