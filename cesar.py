def chiffrement_cesar(text, number):
    text_chiffre = ""
    for car in text :
        if 'a' <= car <= 'z' :
            text_chiffre += chr((ord(car) - ord('a') + number) % 26 + ord('a'))
        elif 'A' <= car <= 'Z' :
            text_chiffre += chr((ord(car) - ord('a') + number) % 26 + ord('a'))
        else :
            text_chiffre += car

    return text_chiffre

def dechiffrement_cesar(chiffre, number):
    text = ""
    for car in chiffre :
        if 'a' <= car <= 'z' :
            text += chr((ord(car) - ord('a') - number) % 26 + ord('a'))
        elif 'A' <= car <= 'Z' :
            text += chr((ord(car) - ord('a') - number) % 26 + ord('a'))
        else :
            text += car

    return text
