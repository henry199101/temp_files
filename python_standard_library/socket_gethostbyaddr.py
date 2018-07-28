import socket

hostname, aliases, addresses = socket.gethostbyaddr('61.135.169.121')

print 'Hostname	:', hostname
print 'Aliases	:', aliases
print 'Addresses:', addresses
