import pigpio
import time


class receive:
    def __init__(self):
        self.pi = pigpio.pi()

        self.pi.set_mode(20, pigpio.INPUT)
        self.pi.set_mode(22, pigpio.INPUT)
        self.pi.set_mode(24, pigpio.INPUT)
        self.pi.set_mode(26, pigpio.INPUT)

    def nic_receive(self, tick):
        time.sleep(tick*1.5)
        output = ""
        for i in range(0, 8):
            bit = self.pi.read(26)
            time.sleep(tick)
            output += str(bit)

        return output

    def start_receive(self, tick):
        while 1 == 1:
            print("waiting")
            self.pi.wait_for_edge(26, pigpio.RISING_EDGE)
            msg = self.nic_receive(tick)
            print(msg)