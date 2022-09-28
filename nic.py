import pigpio
import time

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

#sends a 4 bit binary message
def nic_send(message):
    for element in message:
        if element == "1":
            lightsOn()
            time.sleep(0.1)
        else:
            lightsOut()
            time.sleep(0.1)

#reads a 4 bit binary message as it is being sent
def nic_receive():
    output = ""
    for i in "0000":
        iin = pi.read(26)
        output = output + iin

    return output


## to test this 2 devices are needed. One to send information and one to receive.
## run the programs at the same time and watch the receiver print the messages sent from the sender
## using a loop or multiple calls of both nic_send() and nic_receive() will be useful so that more than 1 4 bit
## sequence can be read at once

