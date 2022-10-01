class Packet:
	def __init__(self, size, number, address, message):
		self.size = intToBin(size,6)
		self.number = intToBin(number,6)
		self.address = intToBin(address,3)
		self.message = charsToBin(message)
	
	def getBinString(self):
		return self.message+self.address+self.number+self.size
	
	def getMessage(self):
		return(binToChars(self.message))

def intToBin(num, length):
	binNum = int(bin(num).replace("0b",""))
	zeros = ""
	for i in range(0,length):
		zeros += '0'
	zeros = int(zeros)
	return zeros | binNum
	
def charsToBin(chars):
	a1 = ord(chars[0])
	print(a1)
	a2 = ord(chars[1])
	print(a2)
	b1 = bin(a1).replace("0b","")
	print(b1)
	b2 = bin(a2).replace("0b","")
	print(b2)
	print(b1+b2)
	return b1+b2	

def binToChars(binary):
	input_value = int(binary)
	input_bytes = input_value.to_bytes(4, "big")
	ASCII_value = input_bytes.decode()
	return ASCII_value

"""
Currently the characters are being represented by 7 bits
and must be represented by 4 bits before being passed to to_bytes()
"""

test = Packet(1,1,1,"ab")
print(test.message)
print(test.getMessage())
