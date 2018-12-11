
# Basically this small script retrieves the general information of the web domain from the world wide whois database available.

# module to connect with the whois database to retrieve the domain regarding information.


import whois

data = raw_input("Enter a domain name: ")

w = whois.whois(data)

print w
