import paramiko
import os,time,sys

os.system("cls")

serverslist = []

Firewall = input("How many Firewall VPS do you have ? : ")

count = int(Firewall)

for x in range(1, (count + 1)):
	v = "vps{}".format(x)
	data = os.environ.get('{}'.format(v))
	serverslist.append(data)
	x+=1

usr = "ubuntu"
ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
while True:
	command = input("\nEnter the command to run : ")
	command = str(command)
	if " | " in command:
		command = command.replace(" | ", ";")


	if command.startswith('!out-'):
		prefix , arg = command.split('-', 1)
		if "nano" in arg:
			for machine in serverslist:
				machine = str(machine)
				if "none" in machine.lower():
					pass
				else:
					pass
		else:
			try:
				os.system('{}'.format(arg))
			except:
				pass
	else:
		for machine in serverslist:
			machine = str(machine)
			if "none" in machine.lower():
				pass
			else:
				ip,pswd = machine.split(':')
				ssh.connect(ip, username=usr, password=pswd,look_for_keys=False)
				ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("{}".format(command),bufsize=-1,timeout=None)
				output = ssh_stdout.readlines()
				error = ssh_stderr.readlines()
				try:
					print("{0}-OUTPUT : \n {1}".format(ip,output))
				except:
					print("{0}-OUTPUT : \n {1}".format(ip,error))


ssh.close()
