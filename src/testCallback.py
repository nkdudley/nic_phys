import pigpio
import receive
import time



receive = receive.receive()
pi = pigpio.pi()
pi.set_mode(26, pigpio.INPUT)

def initCallback():
    func = pi.callback(26, pigpio.RISING_EDGE, cbf)
    return func

def reinitCallback(callback):
    callback = initCallback()

def cbf(gpio, level, tick):
    global cb1
    cb1.cancel()
    time.sleep(.1)
    receive.nic_receive(.1)
    cb1 = initCallback()

cb1 = initCallback()
time.sleep(60)
cb1.cancel()
