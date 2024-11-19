import socket
import pyfiglet
from termcolor import colored
banner = pyfiglet.figlet_format("IP Convertor" ) 

print()
print(colored("*********************** Domain To IP Convertor *************************", 'green'))
print(colored("***********************  Created By AbsFuty7  *************************", 'red'))

print(colored(banner, 'green'))

Domain_Name = input("Enter Domain: ")

ip = socket.gethostbyname(Domain_Name)

print("IP For {} : {}".format(Domain_Name,ip))
