plaintext = 'attackatdawn'
key = 'lemon'

def encrypt(text, key):
  upperptext = text.upper()
  upperkey = key.upper()
  keylen = len(key)
  code = ''
  for i in range(len(text)):
   if upperptext[i] == " ":
    code = code + upperptext[i] 
   elif not upperptext[i].isalpha(): 
     code = code + upperptext[i]
   else:  
    value = (ord(upperptext[i]) + ord(upperkey[i % keylen])) % 26
    code += chr(value + 65)
  return code.lower()

def decrypt(etext, key):
  upperptext = etext.upper()
  upperkey = key.upper()
  keylen = len(key)
  code = ''
  for i in range(len(etext)):
   if upperptext[i] == " ":
    code = code + upperptext[i] 
   elif not upperptext[i].isalpha(): 
     code = code + upperptext[i]
   else:  
    value = (ord(upperptext[i]) - ord(upperkey[i % keylen])) % 26
    code += chr(value + 65)
  return code.lower()

ecode = encrypt(plaintext , key)
print("Original Text:")
print(plaintext)
print(" ")
print("Encoded Text:")
print(ecode)
print(" ")
print("Decoded Text:")
print(decrypt(ecode , key))
print(" ")
