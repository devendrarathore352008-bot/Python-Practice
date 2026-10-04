alphabet_keys  = "abcdefghijklmnopqrstuvwxyz"
secret_keys = "zxcvbnmasdfghjklpoiuytrewq"

# Welcome message
print("---------        WELCOME TO THE PROGRAM     ----------")
print(" --- Substitution Cipher, What's The Secret! ---")
print()

while True:
    # Starting Point , Taking message
    user_message = input("Enter Your Message: ").lower()
    print()

    # --- Question Set 1 ---
    print("--- What You Want To Do ?? ---")
    print(" 1. Encrypt The Message.")
    print(" 2. Try Different Message.")
    print(" 3. Exit.")
    print()
    
    choice1 = int(input("Enter Your Choice: "))
    print()

    if choice1 == 2:
        continue # Skip everthing and start from the starting point
    elif choice1 == 3:
        print("--- THANKS FOR USING SUBSTITUTION CIPHER ---")
        break # It will end program
    elif choice1 == 1:
        # Encrypt the message
        encrypted_message = ""
        for check in user_message:
            if check in alphabet_keys:
                position = alphabet_keys.index(check)
                encrypted_message += secret_keys[position]
            else:
                encrypted_message += check
        print(f"Encrypted Message: {encrypted_message} \n")
    else:
        print("!! Invalid Choice !! Restarting...\n")
        continue

    # --- Question set 2 (Only appears if they successfully encrypted) ---
    print("--- Now What You Want To Do ?? ---")
    print(" 1. Decrypt The Message.")
    print(" 2. Try Different Message.")
    print(" 3. Exit.")
    print()

    choice2 = int(input("Enter Your Choice: "))
    print()

    if choice2 == 2:
        continue # Skip everthing and start from the starting point
    elif choice2 == 3:
        print("--- THANKS FOR USING SUBSTITUTION CIPHER ---")
        break
    elif choice2 == 1:
        # Decrypt the message
        decrypted_message = ""
        for decipher in encrypted_message:
            if decipher in secret_keys:
                position = secret_keys.index(decipher)
                decrypted_message += alphabet_keys[position]
            else:
                decrypted_message += decipher
        print(f"Decrypted Message: {decrypted_message} \n")
    else:
        print("!! Invalid Choice !! Restarting...\n")
        continue

    # --- Question set 3 (Only appears if they successfully decrypted) ---
    print(" 1. Try New Message.")
    print(" 2. Exit.")
    print()

    choice3 = int(input("Enter Your Choice: "))
    print()

    if choice3 == 1:
        continue # Skip everthing and start from the starting point
    elif choice3 == 2:
        print("---- THANKS FOR USING THE SUBSTITUTION CIPHER ----")
        print(" ---  Hope You Will Come Again  ---")
        break
    else:
        print("!! Invalid Choice !! Exiting...\n")
        continue