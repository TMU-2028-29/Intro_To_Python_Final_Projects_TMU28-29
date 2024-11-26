"""
Python project - Vigenere Cipher encoder/decoder
For my project I have chosen to create a program that helps the user 
encode and decode messages using the Vigenere Cipher. The Vigenere
Cipher is also known as the "unbreakable cipher" due to the difficulty
associated with attempting to break the code without the correct key. 
To use the cipher, one starts by creating a grid with each letter of 
the alphabet heading its own column and row. Each row and column of the
grid contains the alphabet in its entirety, shifted one letter with
each new row/column. For example, if the alphabet consisted only of 
the letters A through E, the grid would look like the following:
    
    A  B  C  D  E

A   A  B  C  D  E
B   B  C  D  E  A
C   C  D  E  A  B
D   D  E  A  B  C
E   E  A  B  C  D

Using this grid, we can encode a message using a key. If "BADE CAB"
is our message and "BAD" is what we use as our key, our next step is
to align the message with our key like so, repeating the key as needed:
    BADE CAB
    BADB ADB
Then, to get our encoded message, we take the letter where the column
headed by our original message and the row headed by the corresponding
key letter intersect. In our example, this will give us the encrypted
message:
    CABA CDC
When given the encoded message and the key, we can also work backwards
to determine the original message by looking at the row of the key
letter, finding the encoded letter in that row, and recording the column
it was found under.

My project works by taking a user's input in either the form of a string
or text file upload, depending on the user's choice, and encoding or
decoding the message for them using the Vigenere Cipher. The result is 
then output in the same format as the input. If the user had a file to 
upload, they will receive a new file with the encoded or decoded text. 
If they chose to input a string, their output message will be printed to 
the console.
"""

# This function is for when the user wants to read text from a file
def get_file_text(filename):
    # We find their file and extract the text to later perform our encoding/decoding
    with open(filename, 'r') as f:
        file_text = f.read()
    return file_text


# This function is for if the user wants to save the results to look at later
def create_output_file(filename, text):
    # We write the output to the new file.
    # If a file with the same name already exists, it is overwritten.
    with open(filename, 'w') as f:
        new_file = f.write(text)
    return new_file


# This is the function we use to encode the user's text using the Vigenere Cipher
def encode_text(text, key):
    # We have a string containing the alphabet, to use in place of the aforementioned grid
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    newstring = ""
    # "key_letter" is an int variable that we'll use to cycle through the characters in the key
    key_letter = 0
    # We use "new_letter_index" to store the value of each encoded character
    new_letter_index = 0
    
    # Cycling through each character, we start by checking if it's a letter
    for i in text.upper():
        if i in alphabet:
            
            # Instead of making an alphabetic grid and finding the intersection, we accomplish 
            # the same task by adding the indexes of the original character and that of the key
            # character together. This gives us the index of the encoded character
            index_i = alphabet.index(i)
            index_key = alphabet.index(key[key_letter])
            new_letter_index = index_i + index_key
            
            # In the case that the new index is out of bounds, we subtract 26 to loop back around
            # and find the appropriate letter
            if new_letter_index > 25:
                new_letter_index -= 26
                
            # Add the encoded letter to the encoded message
            newstring += alphabet[new_letter_index]
            
            # If the key is shorter than the message, we're bound to run out of characters.
            # To handle this we just restart from the beginning of the key
            if key_letter == len(key) - 1:
                key_letter = 0
            else:
                key_letter += 1               
                
        # If not a letter, don't encode it and simply add it to the message as is
        else:
            newstring += i
    return newstring


# This is the function we use to decode some text previously encoded using the Vigenere Cipher
def decode_text(text, key):
    # Just like when encoding, we have a string containing the alphabet for reference,
    # as well as variables for indexing
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    newstring = ""
    key_letter = 0
    new_letter_index = 0
    
    # Cycling through each character, we start by checking if it's a letter
    for i in text.upper():
        if i in alphabet:
            # Instead of adding the indexes together like when generating the encrypted text,
            # to decode it we work backwards and subtract the key index from that of the
            # encoded letter to find the original character
            index_i = alphabet.index(i)
            index_key = alphabet.index(key[key_letter])
            new_letter_index = index_i - index_key
            
            # In this case, an out of bounds index would be negative due to the subtraction
            # so we add 26 to loop around this time instead
            if new_letter_index < 0:
                new_letter_index += 26
                
            # Add the encoded letter to the encoded message
            newstring += alphabet[new_letter_index]
            
            # Restart from the beginning of the key as needed
            if key_letter == len(key) - 1:
                key_letter = 0
            else:
                key_letter += 1
        else:
            newstring += i
    return newstring

# Print a title and menu for a user-friendly interface.
print("\nVigenere Cipher Encoder/Decoder")
while True:
    # The user has the option to either encode or decode a message, or exit the program entirely
    print("---------------\nWould you like to: \n1 - Encode a message \n2 - Decode a message \n3 - Exit\n---------------")
    choice = int(input())
    
    if choice == 1:
        print("You have chosen 1 - encode a message")
        # If the user wants to encode a message, they can either extract text 
        # from a file or write their own
        choice = input("Do you have a file to upload? Y/N\n")
        if choice.upper() == "Y":
            message = get_file_text(input("Enter the file name: "))
        if choice.upper() == "N":
            message = input("Please enter the message to encode: ")
        
        # Get the key to use for encoding the user's message
        key = input("Now enter your key: ")
        text = encode_text(message, key.upper())
        
        # After encoding the text and printing the results, we give the user the option
        # to save for future reference or to share their encrypted message
        print(text)
        save = input("Would you like to save the output? Y/N\n")
        if save.upper() == "Y":
            filename = input("enter a name for the save file: ")
            create_output_file(filename, text)        
            
    elif choice == 2:
        print("You have chosen 2 - decode a file")
        # If the user wants to decode a message, they can either extract text 
        # from a file or type their own
        choice = input("Do you have a file to upload? Y/N\n")        
        if choice.upper() == "Y":
            message = get_file_text(input("Enter the file name: "))
        if choice.upper() == "N":
            message = input("Please enter the message to decode: ")
            
        # Get the key to use to decode the user's message
        key = input("Now enter your key: ")
        text = decode_text(message, key.upper())
        
        # After decoding the text and printing the results, we give the user the option
        # to save their final message
        print(text)
        save = input("Would you like to save the output? Y/N\n")
        if save.upper() == "Y":
            filename = input("enter a name for the save file: ")
            create_output_file(filename, text)
            
    # Exit the program
    elif choice == 3:
        print("Goodbye!")
        break
    
    # If the user enters a choice not on the menu, loop the main program again
    else:
        print("Sorry, that's not a valid input. Please try again")