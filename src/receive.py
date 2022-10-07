import pigpio
import time


class receive:
    def __init__(self):
        self.pi = pigpio.pi()

        self.pi.set_mode(20, pigpio.INPUT)
        self.pi.set_mode(22, pigpio.INPUT)
        self.pi.set_mode(24, pigpio.INPUT)
        self.pi.set_mode(26, pigpio.INPUT)

        self.tick = 0.07

    def initCallback(self):
        func = self.pi.callback(26, pigpio.FALLING_EDGE, self.cbf)
        return func

    def cbf(self, gpio, level, tick):
        global cb1
        cb1.cancel()
        print("cancelled")
        self.nic_receive()


    def nic_receive(self):
        time.sleep(self.tick*1.5)
        output = ""
        for i in range(0, 8):
            bit = self.pi.read(26)
            time.sleep(self.tick)
            output += str(bit)
        print("received: " + output)
        return output

    def start_receive(self):
        while True:
            self.pi.wait_for_edge(26, pigpio.RISING_EDGE)
            cp1 = self.initCallback()
            time.sleep(self.tick*40)
