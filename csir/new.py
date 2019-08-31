import sys
import subprocess

if not sys.argv[1] == "dhcp":
    parameters = {'ip': sys.argv[1], 'gateway': sys.argv[2]}
temp = open('temp', 'wb')

with open("aa", "r") as f:
    lines = f.readlines()

    for i, line in enumerate(lines):
        if line.startswith("iface enp19s0 inet"):
            lines = lines[:i]
            if not sys.argv[1] == "dhcp":
                lines.append("\niface enp19s0 inet static")
                lines.append("\n\taddresses: " + parameters['ip'])
                lines.append("\n\tgateway: " + parameters['gateway'])
            else:
                lines.append("\niface enp19s0 inet dhcp")
    f.close()
    print(lines)
with open("aa","w+") as f:
   for line in lines:
       f.write(line)

# sys.os("ifdown enp19s0; ifup enp19s0")

bashCommand = "ifconfig enp19s0 " + parameters['ip'] + " netmask " + parameters['gateway']
subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)