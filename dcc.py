encoded_message=input("Enter the code\n")
dshift=int(input("Enter the shift\n"))
decoded_message=""
for i in range(len(encoded_message)):
	char=encoded_message[i]
	index_char=ord(char)-dshift
	decoded_message+=chr(index_char)
print(decoded_message)
	


