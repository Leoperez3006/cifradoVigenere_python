#Jose Leonardo Perez Gonzalez
#A01424133

#algoritmo de cifrado de vigenere
text = input("introduce el texto a cifrar: ")
text = text.upper() #convertimos todo a mayusculas
value =  input("Introduce la llave: ")
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encrypt(text, key):
  encrypted = []
  key_index = 0
  key = key.upper()

  for char in text:
    num = alphabet.find(char.upper())
    if num != -1:
      num+=alphabet.find(key[key_index])
      num %= len(alphabet)
      encrypted.append(alphabet[num])
      key_index +=1
      if key_index == len(key):
        key_index =0
    else:
      encrypted.append(char)
  return('').join(encrypted)


print(encrypt(text, value).lower())