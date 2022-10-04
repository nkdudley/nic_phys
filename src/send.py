import pigpio
import time


class send:

    def __init__(self):
        self.pi = pigpio.pi()

        self.pi.set_mode(21, pigpio.OUTPUT)
        self.pi.set_mode(23, pigpio.OUTPUT)
        self.pi.set_mode(25, pigpio.OUTPUT)
        self.pi.set_mode(27, pigpio.OUTPUT)

    #turns all of the transmit lights off
    def lightsOut(self):
        self.pi.write(21, pigpio.LOW)
        self.pi.write(23, pigpio.LOW)
        self.pi.write(25, pigpio.LOW)
        self.pi.write(27, pigpio.LOW)

    #turns all the transmit leds on
    def lightsOn(self):
        self.pi.write(21, pigpio.HIGH)
        self.pi.write(23, pigpio.HIGH)
        self.pi.write(25, pigpio.HIGH)
        self.pi.write(27, pigpio.HIGH)

    def nic_send(self, msg, tick):
        self.lightsOn()
        time.sleep(tick)
        for element in msg:
            if element == "1":
                self.lightsOn()
                time.sleep(tick)
            else:
                self.lightsOut()
                time.sleep(tick)
        self.lightsOut()

    def start_send(self, tick):
        num = input("enter a number 0 - 255 or quit to exit: ")
        while num != "quit":
            binmsg = bin(int(num))
            msg = binmsg.replace("0b", "")
            self.nic_send(msg, tick)
            num = input("enter a number 0 - 255 or quit to exit: ")
        print("exiting...")
        exit(1)