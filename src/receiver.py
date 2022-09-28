from nic import nic_receive

for i in range(0, 10):
  returnval = nic_receive()
  print(returnval)
