import send
import receive
import pigpio
import time
import threading

sender = send.send()
receiver = receive.receive()


#do handshake
sender.lightsOn()
time.sleep(0.1)
sender.lightsOut()
time.sleep(0.1)
sender.lightsOn()

print("looking for the other machine...")
if(receiver.pi.read(26) == 0):
    sender.pi.wait_for_edge(26, pigpio.RISING_EDGE)
print("machine found!")

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