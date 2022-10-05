import packet

class Message:
        def __init__(self, *args):
                if len(args) == 2:
                        self.message = args[0]
                        self.address = args[1]
                        self.size = (len(args[0])//2)+1
                        self.packets = []
                        for i in range(0, (self.size*2)-2, 2):
                                chars = self.message[i:i+2]
                                self.packets.append(packet.Packet(packet.encode(
                                chars, self.address, i/2, self.size)))
                                
                elif len(args) == 1:
                        self.message = ""
                        self.address = args[0][0].getAddress()
                        self.size = args[0][0].getSize()
                        self.packets = []
                        while len(self.packets) != int(self.size):
                                for x in args[0]:
                                        if int(x.getNumber()) == len(self.packets):
                                                self.packets.append(x)
                                                self.message += x.getMessage()

                else: print("Message() requires 1 or 2 args but "+
                            str(len(args))+" were given")

"""
#Tests the creation of two Messages, one from user input and another from Packets

string = input("Enter a message(128 char max):")
address = input("Enter the address for the message(0-15):")
test1 = Message(string, address)
print("Message 1: "+test1.message)
p1 = packet.Packet(packet.encode("te",1,1,4))
p2 = packet.Packet(packet.encode("st",1,2,4))
p3 = packet.Packet(packet.encode("in",1,3,4))
p4 = packet.Packet(packet.encode("g",1,4,4))
packets = [p4,p1,p3,p2]
test2 = Message(packets)
print("Message 2: "+test2.message)
"""


