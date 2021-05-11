import string

alphabet = string.ascii_lowercase            # importation de l'alphabet en minuscules
alphabet2 = "zydnbmlvskihgarxpjoqtcfeuw"     # alphabet trouvé graçe à la fréquence d'apparition des lettres en français


def dechiffrement(texte, cle):
    message = ""
    for letter in texte:
        if alphabet.find(letter) != -1:
            message += alphabet2[alphabet.find(letter)]
        else:
            message += letter
    return message    
# fonction permettant d'échanger chaque lettre du texte 2 par une autre graçe à "alphabet2"

texte2 = "gx qosvlnkd wkvlkxo xiu vscx qno yd fsu cx qniix cx unkggx kdvsddyx xu vsdukxdu g'kdckvx. gxi gxuuoxi cy fsu cx qniix qxofxuuxdu cx cxvngxo gxi gxuuoxi cy fxiinmx sokmkdng fscygs 26. ixygxi gxi gxuuoxi cx n n a isdu vlkwwoxxi."

print (dechiffrement(texte2, alphabet2))

# Texte initial = gx qosvlnkd wkvlkxo xiu vscx qno yd fsu cx qniix cx unkggx kdvsddyx xu vsdukxdu g'kdckvx. gxi gxuuoxi cy fsu cx qniix qxofxuuxdu cx cxvngxo gxi gxuuoxi cy fxiinmx sokmkdng fscygs 26. ixygxi gxi gxuuoxi cx n n a isdu vlkwwoxxi.
# Texte final = LE PROCHAIN FICHIER EST CODE PAR UN MOT DE PASSE DE TAILLE INCONNUE ET CONTIENT L'INDICE. LES LETTRES DU MOT DE PASSE PERMETTENT DE DECALER LES LETTRES DU MESSAGE ORIGINAL MODULO 26. SEULES LES LETTRES DE A A B SONT CHIFFREES.
