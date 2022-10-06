import send
import receive
import pigpio
import time
import threading

sender = send.send()
receiver = receive.receive()

<<<<<<< HEAD
=======
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
>>>>>>> 28fff426e5ee9af7f139d1c9312513c3ee0370f1

#do handshake
sender.lightsOut()
time.sleep(0.01)
sender.lightsOn()

print("looking for the other machine...")
if(receiver.pi.read(26) == 0):
    sender.pi.wait_for_edge(26, pigpio.RISING_EDGE)
print("machine found!")
<<<<<<< HEAD

time.sleep(1)
sender.lightsOut()

thread1 = threading.Thread(target=receiver.start_receive())
thread2 = threading.Thread(target=sender.start_send())

thread1.start()
thread2.start()



# #start progtam
# cb1 = initCallback()
# sender.start_send()
# cb1.cancel()
=======
time.sleep(0.01)
sender.lightsOut()

#start progtam
cb1 = initCallback()
sender.start_send(cb1)
>>>>>>> 28fff426e5ee9af7f139d1c9312513c3ee0370f1
