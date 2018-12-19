
# Basically this small script retrieves the general information of the web domain from the world wide whois database available.

# module to connect with the whois database to retrieve the domain regarding information.

#789sk.gupta@gmail.com 

import whois
import os

import sys

data = raw_input("Enter a domain name: ")

w = whois.whois(data) # whois look-up of website and server ,owwner every basic information of domain.

print w    # prints the information on the unix terminal 

# happy info gathering:))






