# CAESAR CIPHER ENCRYPTION AND DECRYPTION CODE

#  CAESAR CIPHER ENCRYPTION TIME
def encrypt():
    # Ask user for the message they want to encrypt
    textToEncrypt1 = input("What would you like your message to be? ")

    # Ask user for key they want to use to encrypt the text
    key = int(input("Select your encryption key: "))

    # Initialize output variable
    EncryptedText = ""
    # Initialize variable to store each text value received from the input in the for loop
    caesarLetter = ''
    # Initialize the variable used to change each text value to its number form in the utf-8 table
    caesarNumber1 = 0
    # Initialize the variable used to store the new characters equivalent in its number depending on the users key
    caesarNumber2 = 0

    # letters ="abcdefghijklmnopqrstuvwxyz"

    # Variable for initializing the text without any space
    textToEncrypt12 = textToEncrypt1.replace(" ", "")

    # Final form of text to Encrypt (In lower case)
    textToEncrypt2 = textToEncrypt12.lower();

    for x in range(0, len(textToEncrypt2)):

        # Code to get each value in the text using the loop index
        eachLetter = textToEncrypt2[x]
        # Code to change the current values to their numerical equivalent in the utf-8 table
        caesarNumber1 = ord(eachLetter)

        # code to check if the encrypted value may pass the alphabets in the utf-8 table and bring it back within the alphabets
        if caesarNumber1 + key > 122:
            # 120 + 4 -26 =
            caesarNumber2 = caesarNumber1 + key - 26
        else:
            caesarNumber2 = caesarNumber1 + key

        # code to concantenate each encrypted value to form the encrypted text
        caesarEachLetter = chr(caesarNumber2)
        EncryptedText = EncryptedText + caesarEachLetter

    print(EncryptedText)
    cont()


def decrypt():
    # CAESER CIPHER Decryption TIME

    # take message to decrypt

    textToDecrypt1 = input("What would you like your message to be? ")
    # Ask user for the key to decrypt their message
    key = int(input("Select your decryption key: "))

    textToDecrypt1 = textToDecrypt1.lower().replace(" ", "")

    # Initialize values for decrypting text code
    decryptedText = ""

    textToDecrypt2 = ""
    DcaesarLetter = ''

    DcaesarNumber1 = 0
    DcaesarNumber2 = 0

    # For loop to loop through each value in the text and turn it back to its original form after
    # using the key the user entered at the beginning
    for x in range(0, len(textToDecrypt1)):

        DeachLetter = textToDecrypt1[x]
        DcaesarNumber1 = ord(DeachLetter)

        if DcaesarNumber1 - key < 97:
            # 120 + 4 -26 =
            DcaesarNumber2 = DcaesarNumber1 - key + 26
        else:
            DcaesarNumber2 = DcaesarNumber1 - key

        DcaesarEachLetter = chr(DcaesarNumber2)
        decryptedText = decryptedText + DcaesarEachLetter
    print(decryptedText)
    cont()


def guess():
    # take message to decrypt
    textToDecrypt1 = input("What would you like your message to be? ")

    textToDecrypt1 = textToDecrypt1.lower().replace(" ", "")

    # Initialize values for decrypting text code
    decryptedText = ""

    textToDecrypt2 = ""
    DcaesarLetter = ''

    DcaesarNumber1 = 0
    DcaesarNumber2 = 0

    for key in range(0, 26):
        decryptedText = ""
        for x in range(0, len(textToDecrypt1)):

            DeachLetter = textToDecrypt1[x]
            DcaesarNumber1 = ord(DeachLetter)

            if DcaesarNumber1 - key < 97:
                # 120 + 4 -26 =
                DcaesarNumber2 = DcaesarNumber1 - key + 26
            else:
                DcaesarNumber2 = DcaesarNumber1 - key

            DcaesarEachLetter = chr(DcaesarNumber2)
            decryptedText = decryptedText + DcaesarEachLetter
        print("key", key, "guess is:")
        print(decryptedText)
        cont()


def begin():
    WhatTODO = input("What do you want to do ENCRYPT/DECRYPT/GUESS:")
    if WhatTODO.lower().strip() == "encrypt":
        encrypt()
    elif WhatTODO.lower().strip() == "decrypt":
        decrypt()
    elif WhatTODO.lower().strip() == "guess":
        guess()
    else:
        print("Check your spelling")
        begin()


def cont():
    contval = input("Would you like to do anything else, enter C to continue and Q to quit")
    if contval.lower().strip() == "c":
        begin()
    else:
        print("See you later!")


begin()
