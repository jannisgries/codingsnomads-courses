lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
secret = "I hear the gooseberries are doing well this year, and so are the mangoes."
cipher = int(input("Which cipher would you like to have? (right-rotated) "))
encrypted_secret = ""

#estimate the breaking letter for alphabet of chosen cypher
breaking_lowercase = 122 - cipher
breaking_uppercase = 90 - cipher

#encrypt
for letter in secret:
    ord_of_current_letter = ord(letter)
    if ord_of_current_letter >= 65 and ord_of_current_letter <= 90:
        # Uppercase 
        if ord_of_current_letter <= breaking_uppercase:
            ord_of_crypted_letter = ord_of_current_letter + cipher
        else:
            ord_of_crypted_letter = ord_of_current_letter - (26 - cipher)
        
    elif ord_of_current_letter >= 97 and ord_of_current_letter <= 122:
        # Lowercase 
        if ord_of_current_letter <= breaking_lowercase:
            ord_of_crypted_letter = ord_of_current_letter + cipher
        else:
            ord_of_crypted_letter = ord_of_current_letter - (26 - cipher)

    if letter.isalpha() == True:
        encrypted_secret += chr(ord_of_crypted_letter)
    else:
        encrypted_secret += letter

print(encrypted_secret)

#decrypt

answer = "no"
while answer == "no":
    decrypt_cipher = int(input("How is the cipher to decrypt? "))
    secret = ""
    breaking_lowercase_decrypt = 97 + decrypt_cipher
    breaking_uppercase_decrypt = 65 + decrypt_cipher
    for letter in encrypted_secret:
        ord_of_current_letter = ord(letter)
        if ord_of_current_letter >= 65 and ord_of_current_letter <= 90:
            # Uppercase 
            if ord_of_current_letter >= breaking_uppercase_decrypt:
                ord_of_crypted_letter = ord_of_current_letter - decrypt_cipher
            else:
                ord_of_crypted_letter = ord_of_current_letter + (26 - decrypt_cipher)
            
        elif ord_of_current_letter >= 97 and ord_of_current_letter <= 122:
            # Lowercase 
            if ord_of_current_letter >= breaking_lowercase_decrypt:
                ord_of_crypted_letter = ord_of_current_letter - decrypt_cipher
            else:
                ord_of_crypted_letter = ord_of_current_letter + (26 - decrypt_cipher)

        if letter.isalpha() == True:
            secret += chr(ord_of_crypted_letter)
        else:
            secret += letter
    print(secret)
    answer = input("Does the sentence make sense (yes / no) ")
else: 
    print("successfully decrypted")