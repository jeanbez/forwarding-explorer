"""
FORGE - I/O Forwarding Explorer.

Generate the hostfile to run in MareNostrum IV.

:param P: Number of MPI processes
:param F: Number of I/O forwarding server nodes
:param C: Number of compute nodes
"""

import sys

P = int(sys.argv[1])
F = int(sys.argv[2])
C = int(sys.argv[3])

forwarding_nodes_path = sys.argv[4]
clients_nodes_path = sys.argv[5]
hostfile_path = sys.argv[6]

output = open(hostfile_path, 'w')

f = open(forwarding_nodes_path, 'r')
c = open(clients_nodes_path, 'r')

forwarders = f.readlines()
clients = c.readlines()

f.close()
c.close()

# Split the selected nodes into the two sets
f_nodes = forwarders[:F]
c_nodes = clients[:C]

for node in f_nodes:
    output.write('{} slots={} max_slots={}\n'.format(node.strip(), 1, 1))

slots = int((P - F) / C)

for node in c_nodes:
    output.write('{} slots={}\n'.format(node.strip(), slots))

output.close()

