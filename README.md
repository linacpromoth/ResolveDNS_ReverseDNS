# ResolveDNS_ReverseDNS
Tool to find IP address from the given domain name and domain name from the given IP address.

One can send multiple ip address and domain names as text file separately and pass it to the tool to get the respective output. It is done using inbuilt python library named socket.

## Requirements
* Python 3.8.2+
* Python Libraries
    * pandas ($ pip install pandas)
    * pyfiglet ($ pip install pyfiglet)
	

## Installation
Clone the git and you get the ball rolling!!!
```
$ git clone https://github.com/linacpromoth/ResolveDNS_ReverseDNS
$ cd ResolveDNS_ReverseDNS
```
Move the **ipaddress / domains file** to the **ResolveDNS_ReverseDNS** directory and then executes the python file. An output .xlsx file will be generated with the file name - **Domain_output.xlsx** and **IP_output.xlsx** respectively. 

  
## Usage
```
$ python3 playWithDNS.py -i <ipaddress.txt> 
$ python3 playWithDNS.py -d <domains.txt> 

usage: playWithDNS.py [-h] [-i IP_ADDRESS] [-d DOMAIN_NAME]

GET IP from Domain and Domain from IP

optional arguments:
  -h, --help            show this help message and exit
  -i IP_ADDRESS, --ip_address IP_ADDRESS
                        Text File containing List of ip addresses to get domain names
  -d DOMAIN_NAME, --domain_name DOMAIN_NAME
                        Text File containing List of domain names to get ip addresses
```

## Example output

For Given IPs
### Input file
![image](https://user-images.githubusercontent.com/98702521/183440659-5d489d30-147f-4aa3-b380-7542eee55aa6.png)
### Execution
![image](https://user-images.githubusercontent.com/98702521/183439308-f7804b60-e03c-42cd-b824-fdfea19320ae.png)
### output
![image](https://user-images.githubusercontent.com/98702521/183440026-67883eb7-75e8-4965-b246-ed8930bf6264.png)

For Given Domains

### Input file
![image](https://user-images.githubusercontent.com/98702521/183441135-246a7c8f-6874-4b39-b159-7a3a56773dd3.png)
### Execution
![image](https://user-images.githubusercontent.com/98702521/183439835-1b8397b3-caa1-4743-8c27-d922abdd9a30.png)
### Output
![image](https://user-images.githubusercontent.com/98702521/183440117-06ef579c-87ee-4a23-9a0a-07900c806c54.png)

