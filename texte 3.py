import string

alphabet = "zabcdefghijklmnopqrstuvwxy"                 # importation de l'alphabet en minuscules
key = "xova"                                            # clé trouvé grace à la Cryptanalyse du chiffre de Vigenère

def dechiffrement(texte, cle):
    message = ""
    i = 0
    for letter in texte:
        if alphabet.find(letter) != -1:
            message += alphabet[(alphabet.find(letter) + alphabet.find(key[i])) % 26]
            print(alphabet.find(letter), alphabet.find(key[i]))
        else: 
            message += letter
        i = (i + 1)%len(key)
    return message 
#code permettant d'aditionner la position des lettres du texte 3 avec la clé(ici key)

texte3 = "dceuq e n'ehfp cg p'kyhhep uqfw cgiy citudm c gzudiq ni ezhd px c jhptv ep cggsht. kg hdtymdt xdzei gdx rzyq wir mvzxpw, cifcchdb znwd ccyw wy lkcsht, dp isgd uqfw wy ?"

print(dechiffrement(texte3, key))

# Message initial = dceuq e n'ehfp cg p'kyhhep uqfw cgiy citudm c gzudiq ni ezhd px c jhptv ep cggsht. kg hdtymdt xdzei gdx rzyq wir mvzxpw, cifcchdb znwd ccyw wy lkcsht, dp isgd uqfw wy ?
# Clé = xova
# Message final = bravo a l'aide de l'indice vous avez reussi a casser ce code et a finir ce devoir. le dernier texte est pour les braves, regardez vous dans un miroir, en etes vous un ?