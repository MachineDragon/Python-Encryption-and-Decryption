alphabet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567891011"

user_input = input("Enter a secret message: ")

encrypt = ""
decrypt = ""

# To Encrypt
for i in user_input:
    place_holder = alphabet.index(i)
    encrypt += alphabet[place_holder + 5]
print(encrypt)

# To Decrypt
for j in encrypt:
    place_holder = alphabet.index(j)
    decrypt += alphabet[place_holder - 5]
print(decrypt)
