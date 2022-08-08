''' Module which helps in resolving domain names to ip and reverse ip addressess to domain names '''

import argparse
import socket
import sys
import os
import pyfiglet
import pandas as pd



def DNSReverse(IPFile):
    ''' For Given IP address it will get the respective Domain names in an excel file
    '''
    ## Reading the given ip file ##
    f= open(IPFile, 'r')
    d = f.read()
    ips = [i for i in d.split('\n')  if i != '']
    
    ## Getting the domain names and generating Excel ##
    cont = []
    for ip in ips:
        try:
            host = socket.gethostbyaddr(ip)
            val = [ip,host[0]]
        except:
            val = [ip,"DOMAIN NOT FOUND"]
            pass
        cont.append(val)
    df = pd.DataFrame(cont,columns=['IP address', 'Domain'])
    df.to_excel("Domain_output.xlsx",index=False)
    return "Domain_output.xlsx"
    

def DNSResolve(domainFile):
    ''' For Given Domain names it will get the respective IP addresses in an excel file
    '''
    ## Reading the given domain file ##
    f= open(domainFile, 'r')
    d = f.read()
    domains = [i for i in d.split('\n') if i != '']
    
    ## Getting the ip addresses and generating Excel ##
    cont = []
    for domain in domains:
        try:
            ip = socket.gethostbyname_ex(domain)
            val = [domain,ip[-1]]
            #print(val)
        except:
            val = [domain,"IP NOT FOUND"]
            pass
        cont.append(val)
    df = pd.DataFrame(cont,columns=['Domain', 'IP address'])
    df.to_excel("IP_output.xlsx",index=False)
    return "IP_output.xlsx"

def file_checker(file):
    ''' Check whether the file exist in the actual folder
    '''
    if os.path.exists(file):
        if '.txt' in file:
            present = "Yes"
            pass
        else:
            print("Ensure the file ends with '.txt' extension")
            sys.exit()
    else:
        print("File Not Found!!!!\nMake sure the file is Present in the same folder.")
        sys.exit()

def tool_display():
    ''' To Display the Tool logo
    '''
    word = pyfiglet.figlet_format("DNS R 2")
    print(word)
    print("-----------------------------------------------------------------------------------------")
    print("Version : 0.1 - 8th Aug 2022")
    print("Created By: Promoth  https://github.com/linacpromoth")
    print("-----------------------------------------------------------------------------------------")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='GET IP from Domain and Domain from IP')
    parser.add_argument("-i", "--ip_address", help="Text File containing List of ip addresses to get domain names")
    parser.add_argument("-d", "--domain_name", help="Text File containing List of domain names to get ip addresses")
    
    
    args = parser.parse_args()
    ip_addresses = args.ip_address
    domain_names = args.domain_name
    
    if ip_addresses or domain_names:
        tool_display()
        if ip_addresses:
            ## Check presence of files ##
            file_checker(ip_addresses)
            out_file = DNSReverse(ip_addresses)
            print(f"Output file generated: {out_file}")
        if domain_names:
            ## Check presence of files ##
            file_checker(domain_names)
            out_file = DNSResolve(domain_names)
            print(f"Output file generated: {out_file}")
        pass
    else:
        parser.print_help(sys.stderr)
        sys.exit()
    
    
    