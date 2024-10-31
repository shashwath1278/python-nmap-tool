import nmap

scanvar = nmap.PortScanner()

print("Hey there, this is a simple Nmap tool")
print(" ")

ip = input("Enter the IP address you would like to scan: ")
    
response = input("""\nEnter the type of scan you want:
                      1. SYN ACK scan
                      2. UDP scan
                      3. Comprehensive scan
                      4. Casual/Regular scan
                      Choose an option (1/2/3/4): """)
print("Your response is:", response)

if response == '1':
        print("Nmap version:", scanvar.nmap_version())
        scanvar.scan(ip, '1-1024', '-v -sS')
        
        if scanvar[ip].state() == "up":
            print(scanvar.scaninfo())
            print("IP status:", scanvar[ip].state())
            if 'tcp' in scanvar[ip]:
                print("Available Open ports:", scanvar[ip]['tcp'].keys())
            else:
                print("No open TCP ports found.")
        else:
            print("IP status: down")

elif response == '2':
        scanvar.scan(ip, '1-1024', '-v -sU')
        
        if scanvar[ip].state() == "up":
            print(scanvar.scaninfo())
            print("IP status:", scanvar[ip].state())
            if 'udp' in scanvar[ip]:
                print("Available Open UDP ports:", scanvar[ip]['udp'].keys())
            else:
                print("No open UDP ports found.")
        else:
            print("IP status: down")

elif response == '3':
        print("Performing a comprehensive scan...")
        scanvar.scan(ip, '1-65535', '-v -A -sV -sC -A -O')
        
        if scanvar[ip].state() == "up":
            print(scanvar.scaninfo())
            print("IP status:", scanvar[ip].state())
            if 'tcp' in scanvar[ip]:
                print("Available Open ports (TCP):", scanvar[ip]['tcp'].keys())
            else:
                print("No open TCP ports found.")
                
            if 'udp' in scanvar[ip]:
                print("Available Open ports (UDP):", scanvar[ip]['udp'].keys())
            else:
                print("No open UDP ports found.")
        else:
            print("IP status: down")
elif response == '4':
        print("Nmap version:", scanvar.nmap_version())
        print("...loading..Please wait ")
        scanvar.scan(ip, '1-1000', '-v --open')
        if scanvar[ip].state() == "up":
            print(scanvar.scaninfo())
            print("IP status:", scanvar[ip].state())
            print("Available Open ports:", scanvar[ip].values())
        else:
            print("IP status: down")
else:
        print("Invalid option. Please select 1, 2, or 3.")


 