import sys

ip = sys.argv[1]

# open the file back and read the contents
f = open("interfaces.txt", "r")
cmd = []
# or, readlines reads the individual lines
f1 = f.readlines()
for x in f1:
    cmd.append(x)

cmd[8] = "\taddresses: "
cmd[8] += ip
cmd[8] += "\n"
print(cmd)


open('ss', 'w').close()


with open('ss', 'w') as rsh:
    # rsh.write('''#! /bin/bash''')
    for x in cmd:
        rsh.write(x)

f.close()
# for line in f:
#	copy.write(line)

# if "address" not in line:
#	print(address+"new ip")

# f= open("interfaces.txt","w") #write mode
# f.write(lines)
# print(line)
f.close()










