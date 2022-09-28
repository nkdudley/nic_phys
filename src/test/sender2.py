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

#turns all of the transmit lights off
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

def nic_send(message):
    for element in message:
        if element == "1":
            lightsOn()
            time.sleep(0.1)
        else:
            lightsOut()
            time.sleep(0.1)

lightsOut()
broadcastPacket = "10000000000000000000000000000000"
nic_send(broadcastPacket)
signalval = pi.read(26)
if signalval == 1:
    print("signal on")
else:
    print("signal off")
