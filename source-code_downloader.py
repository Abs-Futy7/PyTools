import turtle 
import urllib.request as u
import pyfiglet 
from termcolor import colored

banner = pyfiglet.figlet_format("SourceCode Getter" ) 

border = "*" * 70
print(colored(border, 'green'))
print(colored(banner, 'green'))
print(colored(border, 'green'))
print(colored("***********************  Created By AbsFuty7  *************************", 'red'))
print()

website_Domain = turtle.textinput("Domain Name ","Enter the full URL (e.g., https://example.com):")

source_code = u.urlopen(website_Domain)
source_code_read = source_code.read()


print(source_code_read) 