import pigpio
import time


class receive:
    def __init__(self):
        self.pi = pigpio.pi()

        self.pi.set_mode(20, pigpio.INPUT)
        self.pi.set_mode(22, pigpio.INPUT)
        self.pi.set_mode(24, pigpio.INPUT)
        self.pi.set_mode(26, pigpio.INPUT)

        self.tick = 0.1

    def nic_receive(self):
        time1 = time.time_ns()
        time.sleep(self.tick*1.5)
        output = ""
        for i in range(0, 8):
            bit = self.pi.read(26)
            output += str(bit)
            time.sleep(self.tick)

        time2 = time.time_ns()
        duration = time2-time1
        print("received: " + output)
        print("time elapsed: "+duration)
        return output
