# A script that feeds a list of subnets into nmap to scan for up hosts
# started off as a tool to validate changes

# import the 'subprocess' module so we can excecute the nmap commands
import subprocess

# open the file called 'subnets' and read each line separately
# the subnets file should be in the same directory, and populated with the list of subnets to scan
# see subnets.example for file format

with open('subnets') as f:
    subnets_to_scan = f.read().splitlines()

# loop over each subnet in the file, and scan using the HOST DISCOVERY -sn: Ping Scan option
for subnet in subnets_to_scan:
    print("Scanning " + subnet)
    subprocess.check_call(['nmap','-sn', subnet])
    print("-"*80)