import send
import receive
import pigpio
import time

sender = send.send()
receiver = receive.receive()

def initCallback():
    func = receiver.pi.callback(26, pigpio.RISING_EDGE, cbf)
    return func

def cbf(gpio, level, tick):\
    print("cbf triggered")
    global cb1
    cb1.cancel()
    print("cbf cancelled")
    receiver.nic_receive()
    cb1 = initCallback()

#do handshake
sender.lightsOut()
time.sleep(0.01)
sender.lightsOn()

print("looking for the other machine...")
if(receiver.pi.read(26) == 0):
    sender.pi.wait_for_edge(26, pigpio.RISING_EDGE)
print("machine found!")
time.sleep(0.01)
sender.lightsOut()

#start progtam
cb1 = initCallback()
sender.start_send(cb1)
