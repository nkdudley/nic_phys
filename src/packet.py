class Packet:
	def __init__(self, binary_string):
		self.binary_string = binary_string
		self.message = binary_string[0:16]
		self.address = binary_string[16:20]
		self.number = binary_string[20:26]
		self.size = binary_string[26:32]
	
	def decode(self):
		message = str(binToChars(self.message))
		address = str(binToInt(self.address))
		number = str(binToInt(self.number))
		size = str(binToInt(self.size))
		return message+" "+address+" "+number+" "+size

def encode(message, address, number, size):
	binary_string = charsToBin(message)
	binary_string += intToBin(address,4)
	binary_string += intToBin(number,6)
	binary_string += intToBin(size,6)
	return binary_string	

def intToBin(num, length):
	b = bin(num).replace("0b","")
	for i in range(0,length-len(b)):
		b = '0'+b
	return b

def binToInt(num):
	return int(num,2)
	
def charsToBin(chars):
	message=""
	a1 = ord(chars[0])
	a2 = ord(chars[1])
	b1 = bin(a1).replace("0b","")
	b2 = bin(a2).replace("0b","")
	for i in range(0,8-len(b1)):
		message += '0'
	message += b1
	for i in range(0,8-len(b2)):
		message += '0'
	message += b2
	return message

def binToChars(binary):
	input_value = int(binary,2)
	total_bytes = (input_value.bit_length()+7)//8
	input_bytes = input_value.to_bytes(total_bytes, "big")
	ASCII_value = input_bytes.decode()
	return ASCII_value

message = input("Enter a message(2 chars):")
address = int(input("Enter an address(1-16):"))-1
number = int(input("Enter the packet number(1-64):"))-1
size = int(input("Enter the number of packets(1-64):"))-1
test = Packet(encode(message,address,number,size))
print("Encoded: "+test.binary_string)
print("Decoded: "+test.decode())
