class Packet:
	def __init__(self, binary_string):
		self.binary_string = binary_string
		self.message = binary_string[0:16]
		self.address = binary_string[16:20]
		self.number = binary_string[20:26]
		self.size = binary_string[26:32]
	
	def getMessage(self):
		return str(binToChars(self.message))
		
	def getAddress(self):
		return str(binToInt(self.address))
		
	def getNumber(self):
		return str(binToInt(self.number))
	
	def getSize(self):
		return str(binToInt(self.size))

def encode(message, address, number, size):
	binary_string = charsToBin(message)
	binary_string += intToBin(address,4)
	binary_string += intToBin(number,6)
	binary_string += intToBin(size,6)
	return binary_string	

def intToBin(num, length):
	b = bin(int(num)).replace("0b","")
	for i in range(0,length-len(b)):
		b = '0'+b
	return b

def binToInt(num):
	return int(num,2)
	
def charsToBin(chars):
        if len(chars) < 1:
                chars = "  "
        if len(chars) == 1:
                chars += ' '
        if len(chars) > 2:
                chars = "  "
        message = ""
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

"""
Tests the creation of one Packet from user input

message = input("Enter a message(2 chars):")
address = input("Enter an address(1-16):"))-1
number = input("Enter the packet number(1-64):"))-1
size = input("Enter the number of packets(1-64):"))-1
test = Packet(encode(message,address,number,size))
print("Encoded: "+test.binary_string)
print("Decoded: "+test.decode())
"""

