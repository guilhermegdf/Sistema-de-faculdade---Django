import datetime
import difflib

def calculaMediaFinal(ac, prova):
    if (ac < 10 or prova < 10 or ac < 0 or prova < 0):
        media = 0.6 * ac + 0.4 * prova
        return media
    else:
        return None

def geraNumeroRA(ultimoRA):
    if (len(str(ultimoRA))== 7 or (format(ultimoRA/100000, '.0f') == datetime.datetime.now().strftime('%y'))):
        ultimoRA=ultimoRA+1
        return ultimoRA
    elif(len(format(str(ultimoRA)[2:]))!=5):
        return (datetime.datetime.now().strftime('%y') + '{:0>5}'.format(str(ultimoRA)[-4:]))
    else:
        return "Error"
    
def calculaMedia(listaNotas):
    total = 0
    for e in listaNotas:
        total += e
    return(total/ len(listaNotas))

def desconta(nota, porcentagem):
    return nota*(porcentagem/100)

def varificaCopia(texto1, texto2):
    s = SequenceMatcher(none, texto1, texto2)
    if(0.8 < round(s.ratio(), 3)):
        return False
    else:
        return True





