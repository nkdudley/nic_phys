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

def nic_receive():
    output = ""
    for i in "000000000000000000000000000000000":
        iin = pi.read(26)
        output = output + str(iin)

    return output
lightsOut()
if pi.wait_for_edge(26, pigpio.FALLING_EDGE, 10):
    lightsOn()
    print("light received")
else:
    print("Timed out - no broadcast packet registered")
