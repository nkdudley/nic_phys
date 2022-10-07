import pigpio
import time


class send:

    def __init__(self):
        self.pi = pigpio.pi()

        self.pi.set_mode(21, pigpio.OUTPUT)
        self.pi.set_mode(23, pigpio.OUTPUT)
        self.pi.set_mode(25, pigpio.OUTPUT)
        self.pi.set_mode(27, pigpio.OUTPUT)

        self.tick = 0.07

    #turns all the transmitting lights off
    def lightsOut(self):
        self.pi.write(21, pigpio.LOW)
        self.pi.write(23, pigpio.LOW)
        self.pi.write(25, pigpio.LOW)
        self.pi.write(27, pigpio.LOW)

    #turns all the transmitting leds on
    def lightsOn(self):
        self.pi.write(21, pigpio.HIGH)
        self.pi.write(23, pigpio.HIGH)
        self.pi.write(25, pigpio.HIGH)
        self.pi.write(27, pigpio.HIGH)

    def nic_send(self, msg):
        print("sending: " + msg)
        self.lightsOut()
        time.sleep(self.tick)
        self.lightsOn()
        time.sleep(self.tick)
        self.lightsOut()
        time.sleep(self.tick)
        for element in msg:
            if element == "1":
                self.lightsOn()
                time.sleep(self.tick)
            else:
                self.lightsOut()
                time.sleep(self.tick)

        self.lightsOut()

    def start_send(self):
        num = input("enter a number 0 - 255 or quit to exit: ")
        while num != "quit":
            binmsg = bin(int(num))
            msg = binmsg.replace("0b", "")

            #moves bits to the right
            for _ in range(0, 8-len(msg)):
                msg = "0" + msg

            self.nic_send(msg)
            time.sleep(self.tick)
            num = input("enter a number 0 - 255 or quit to exit: ")
        print("exiting...")
        exit(1)

