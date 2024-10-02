message = input("Enter the message\n")
shift = int(input("Enter the shift\n"))

encrypted_message = ""

for i in range(len(message)):
    char = message[i]  # Get the character at position i
    if char.isalpha():  # Only shift alphabetic characters
        shifted = ord(char) + shift
        
        # Handle wrapping around for lowercase and uppercase letters
        if char.islower():
            if shifted > ord('z'):
                shifted -= 26
        elif char.isupper():
            if shifted > ord('Z'):
                shifted -= 26
        
        encrypted_message += chr(shifted)
    else:
        encrypted_message += char  # Keep non-alphabet characters unchanged

print("Encrypted message:", encrypted_message)


