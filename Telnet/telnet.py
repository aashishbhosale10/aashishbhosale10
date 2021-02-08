import getpass
import telnetlib
import  time

HOST = "192.168.101.134"
user = input("Enter your Username: ")
password = getpass.getpass()
t1 = time.perf_counter()
tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"en\n")
tn.write(b"cisco\n")
tn.write(b"conf t\n")
tn.write(b"int lo0\n")
tn.write(b"ip add 4.4.4.4  255.255.255.0\n")
tn.write(b"no shut\n")
tn.write(b"end\n")
tn.write(b"show run | sec int\n")
tn.write(b"end\n")
tn.write(b"exit\n")

t2 = time.perf_counter()

print(tn.read_all().decode('ascii'))
print(f'The script finished executing in {round(t2-t1,2)} seconds.')
