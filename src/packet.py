class Packet:
	def __init__(self, size, number, address, message):
		self.size = size
		self.number = number
		self.address = address
		self.message = message

	def getBinString(self):
		return (charsToBin(self.message)+
			intToBin(self.address,3)+
			intToBin(self.number,6)+
			intToBin(self.size,6))

	def getMessage(self):
		return self.message

def intToBin(num, length):
	b = bin(int(num)).replace("0b","")
	for i in range(0,length-len(b)):
		b = '0'+b
	return b
	
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
	input_bytes = input_value.to_bytes(2, "big")
	ASCII_value = input_bytes.decode()
	return ASCII_value

"""
Currently the characters are being represented by 7 bits
and must be represented by 4 bits before being passed to to_bytes()
"""

test = Packet(input("number of packets(1-63):"),
	input("packet number(1-63):"),
	input("address(0-7):"),
	input("message(2 chars):"))
print("binary string:",test.getBinString())
print("message:",test.getMessage())
