# Project 8: Substitution Cipher,Apply encryption and decryption algorithms to implement a substituiton cipher.

alphabet_keys = "abcdefghijklmnopqrstuvwxyz"
# print(len(alphabet_keys))

secret_keys = "zxcvbnmlkjhgfdsaqwertyuiop"
# print(len(secret_keys))

user_message = input("Enter Your Message (Use text only): ").lower()

encrypted_message = ""

print()

for check in user_message:
    
    if check in alphabet_keys:
        position = alphabet_keys.index(check)

        encrypted_message += secret_keys[position]
    else:

        encrypted_message += check

print(f"Encrypted Message: {encrypted_message}")

print()

print("---What You Want To Do?---\n\n 1.Keep The Secret Message.\n 2.Decrypt The Message.\n 3.Quit!!\n\n !! Please choose 1-3 only !!")

print()

choice = int(input("Enter Your Choice: "))

print()

if choice < 1 or choice > 3:
    print("!! Invalid Choice, Please Choose Right Number.")

elif choice == 1:
    print("-- Thanks For Using Message Encrpyter. --")

elif choice == 2:
    decrypted_message = ""
    for decipher in encrypted_message:
        if decipher in secret_keys:
            position = secret_keys.index(decipher)
            decrypted_message += alphabet_keys[position]
        else:
            decrypted_message += decipher
    print(f"Decrypted Message: {decrypted_message} \n\n -- Thanks For Using --")

else: 
    print("-- Quited. Thank You! --")










