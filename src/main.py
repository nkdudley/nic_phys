import send
import receive
import pigpio
import time
import threading

sender = send.send()
receiver = receive.receive()

#do handshake
sender.lightsOn()
if(receiver.pi.read(26) == 0):
    sender.pi.wait_for_edge(26, pigpio.RISING_EDGE)

thread1 = threading.Thread(target=sender.start_send, args=[0.01])
thread2 = threading.Thread(target=receiver.start_receive, args=[0.01])

thread1.start()
thread2.start()


