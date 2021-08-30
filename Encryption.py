


message = input("enter a message to encrypt: ")
alphabet = "abcdefghijklmnopqrstuvwxyz"
key = 5
encrypt = ""
decrypt = ""

for i in message:
    position = alphabet.find(i)
    new_position = (position + 5) % 26
    encrypt += alphabet[new_position]
print("encrypted message: ", encrypt)

for i in encrypt:
    pos = alphabet.find(i)
    new_pos = (pos - 5) % 26
    decrypt += alphabet[new_pos]
print("decrypted message: ", decrypt)