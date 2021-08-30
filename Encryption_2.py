alphabet = "abcdefghijklmnopqrstuvwxyz"
encryption = ""
decryption = ""
user_input = input("Enter a message to be encrypted: ")
# miko

for i in user_input:
    place_holder1 = alphabet.find(i)
                   # m alphabet[12]
                   # i alphabet[8]
                   # k alphabet[10]
                   # o alphabet[14]
    encryption += alphabet[place_holder1 + 2]
print("encryption code:", encryption)

for j in encryption:
    place_holder2 = alphabet.find(j)
                   # o alphabet[14]
    decryption += alphabet[place_holder2 - 2]

print("decrypted code:", decryption)
