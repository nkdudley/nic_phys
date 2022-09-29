import pigpio
import time

import sender

class Packet:
	def __init__(self, size, number, address, message):
		self.size = size
		self.number = number
		self.address = address
		self.message = message
	
	def printBinary(self):
		print('Size: '+self.size+'\nNumber: '+self.number+
			'\nAddress: '+self.address+'\nMessage: '+self.message)

	def printDecimal(self):
		size = str(int(self.size,2))
		number = str(int(self.number,2))
		address = str(int(self.address,2))
		message = str(int(self.message,2))
		print('Size: '+size+'\nNumber: '+number+'\nAddress: '+address+'\nMessage: '+message)

	
pi = pigpio.pi()
pi.set_mode(21, pigpio.OUTPUT)
pi.set_mode(23, pigpio.OUTPUT)
pi.set_mode(25, pigpio.OUTPUT)
pi.set_mode(27, pigpio.OUTPUT)

pi.set_mode(20, pigpio.INPUT)
pi.set_mode(22, pigpio.INPUT)
pi.set_mode(24, pigpio.INPUT)
pi.set_mode(26, pigpio.INPUT)

#turns all the transmit leds off
def lightsOut():
    pi.write(21, pigpio.LOW)
    pi.write(23, pigpio.LOW)
    pi.write(25, pigpio.LOW)
    pi.write(27, pigpio.LOW)

#turns all the transmit leds on
def lightsOn():
    pi.write(21, pigpio.HIGH)
    pi.write(23, pigpio.HIGH)
    pi.write(25, pigpio.HIGH)
    pi.write(27, pigpio.HIGH)

#sends a 32 bit binary message
def nic_send(message):
    for element in message:
        if element == "1":
            lightsOn()
            time.sleep(0.1)
        else:
            lightsOut()
            time.sleep(0.1)

#reads a 31 bit binary message as it is being sent
def nic_receive():
    output = ""
    for i in range(0,31):
        iin = pi.read(26)
        output = output + iin

    return output


new_packet = Packet("000001", "000001", "010", "1010101010101010")
new_packet.printBinary()
new_packet.printDecimal()

## to test this 2 devices are needed. One to send information and one to receive.
## run the programs at the same time and watch the receiver print the messages sent from the sender
## using a loop or multiple calls of both nic_send() and nic_receive() will be useful so that more than 1 4 bit
## sequence can be read at once

