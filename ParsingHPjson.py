import json
import sys,os
from operator import itemgetter
data=[]
IP_list= []
dict={}
dicAttackIP={}
dicVictimIP={}
json_list_dicAttackIP= [] 
json_list_dicVictimIP=[]
dic_connectionType={}

def InputFunc():
	while True:
		try:
			print "1.IP address"
			print "2.Hashes"
			print "3.Domains"
			print "4.URLs"
			print "5.Files"
			print "6.Port number"
			TypeNum= int(raw_input("Please enter your data type: "))
			if (1<=TypeNum <=6):
				return TypeNum
		except ValueError:
			print "Please try again!"
# InputFunc() ask user what type of data they use to search				
#The argument could be a single or multiple hashes, domains, URLs, files, IP address, port, source

def yes_or_no(cont):
    while True:
        cont = cont.strip().lower()  # remove whitespace and make it lowercase
        if cont == 'y':
            return True
        if cont == 'n':
            return False
        print 'Please try again.'
#To know whether the user want to know the detail data
				
def VictimIPFunc():	
	print "<==================Processing==================>"
	for x in data:
		try:
			if (json.loads(x["payload"])["victimIP"] == Input):
				IP_list.append(x)
				ct=json.loads(x["payload"])["connectionType"]
				if ct not in dic_connectionType:
					dic_connectionType[ct]=[0]
				if ct in dic_connectionType:
					dic_connectionType[ct][0]=dic_connectionType[ct][0]+1
				# Store the connection type
				TimeDate=x["timestamp"]["$date"].split('T')
				if TimeDate[0] not in dict:
					dict[TimeDate[0]]=[0]
				if TimeDate[0] in dict:
					dict[TimeDate[0]][0]=dict[TimeDate[0]][0]+1
				#Split the timestamp and store them into dictionary to know when the victim IP attack.
				if 	json.loads(x["payload"])["attackerIP"] not in dicAttackIP:
					dicAttackIP[json.loads(x["payload"])["attackerIP"]]=[0]
					json_list_dicAttackIP.append(x)
				if json.loads(x["payload"])["attackerIP"] in dicAttackIP:
					dicAttackIP[json.loads(x["payload"])["attackerIP"]][0]=dicAttackIP[json.loads(x["payload"])["attackerIP"]][0]+1
				#To know the victim IP attacked by how many different IP addresses	
		except KeyError: 
			pass
	print "(Connection Type, Frequence)"
	for key in dic_connectionType.iteritems():
		print (key)
	print "Source:", "Honeypot"		
	print "The total number of attack on victim IP "+ Input+" is :",(len(IP_list)) 
	print "The attacks happended on ",len(dict)," days"
	print "The victim was attacked by ",len(json_list_dicAttackIP)," different IP address"
	#Tell user connetction type, source, attack IP address.
	while True:
		try:
			cont = raw_input('Do you want to display the attacked time in detail?(y/n)')
			if(yes_or_no(cont)):
				print "(Date,Frequence)"
				for key, value in sorted(dict.iteritems(), key=lambda x:x[1],reverse=True):
				#print the time in deceding order
					print (key,value)
			break
		except:	
			cont = ''  # not yes and not no, so it'll loop again.
			print "Please try again!"			
	while True:
		try:
			cont = raw_input('Do you want to display the attacked IP in detail?(y/n)')
			if(yes_or_no(cont)):
				for key, value in sorted(dicAttackIP.iteritems()):
					print (key)
			break
		except:
			cont = '' 
			print "Please try again!"
	#Provide the detail 
	
def attackerIPFunc():
	print "<==================Processing==================>"
	for x in data:
		try:
			if (json.loads(x["payload"])["attackerIP"] == Input):
				IP_list.append(x)
				ct=json.loads(x["payload"])["connectionType"]
				if ct not in dic_connectionType:
					dic_connectionType[ct]=[0]
				if ct in dic_connectionType:
					dic_connectionType[ct][0]=dic_connectionType[ct][0]+1
				# Store the connection type
				TimeDate=x["timestamp"]["$date"].split('T')
				if TimeDate[0] not in dict:
					dict[TimeDate[0]]=[0]
				if TimeDate[0] in dict:
					dict[TimeDate[0]][0]=dict[TimeDate[0]][0]+1
				#Split the timestamp and store them into dictionary to know when the victim IP attack.
				if 	json.loads(x["payload"])["victimIP"] not in dicVictimIP:
					dicVictimIP[json.loads(x["payload"])["victimIP"]]=[0]
					json_list_dicVictimIP.append(x)
				if json.loads(x["payload"])["victimIP"] in dicVictimIP:
					dicVictimIP[json.loads(x["payload"])["victimIP"]][0]=dicVictimIP[json.loads(x["payload"])["attackerIP"]][0]+1
				#To know the victim IP attacked by how many different IP addresses	
		except KeyError: 
			pass
	print "(Connection Type, Frequence)"
	for key in dic_connectionType.iteritems():
		print (key) 	
	print "Source:", "Honeypot"	
	print "The total number of attack IP "+ Input+" is :",(len(IP_list)) 
	print "The total number of victim on attack IP "+ Input+" is :",(len(dicVictimIP)) 
	print "The attacks happended on ",len(dict)," days"
	while True:
		try:
			cont = raw_input('Do you want to display the attacked time in detail?(y/n)')
			if(yes_or_no(cont)):
				print "(Date,Frequence)"
				for key, value in sorted(dict.iteritems(), key=lambda x:x[1],reverse=True):
					print (key,value)
			break
		except:	
			cont = ''  # not yes and not no, so it'll loop again.
			print "Please try again!"	
	while True:
		try:
			cont = raw_input('Do you want to display the victim IP in detail?(y/n)')
			if(yes_or_no(cont)):
				for key, value in sorted(dicVictimIP.iteritems()):
					print (key)
			break
		except:
			cont = '' 
			print "Please try again!"
	#Provide the detail 
	
def VictimPortFunc():	
	for x in data:
		try:
			if (json.loads(x["payload"])["victimPort"] == Input):
				IP_list.append(x)
				ct=json.loads(x["payload"])["connectionType"]
				if ct not in dic_connectionType:
					dic_connectionType[ct]=[0]
				if ct in dic_connectionType:
					dic_connectionType[ct][0]=dic_connectionType[ct][0]+1
				# Store the connection type
				TimeDate=x["timestamp"]["$date"].split('T')
				if TimeDate[0] not in dict:
					dict[TimeDate[0]]=[0]
				if TimeDate[0] in dict:
					dict[TimeDate[0]][0]=dict[TimeDate[0]][0]+1
				#Split the timestamp and store them into dictionary to know when the victim IP attack.
				if 	json.loads(x["payload"])["attackerIP"] not in dicAttackIP:
					dicAttackIP[json.loads(x["payload"])["attackerIP"]]=[0]
					json_list_dicAttackIP.append(x)
				if json.loads(x["payload"])["attackerIP"] in dicAttackIP:
					dicAttackIP[json.loads(x["payload"])["attackerIP"]][0]=dicAttackIP[json.loads(x["payload"])["attackerIP"]][0]+1		
				if 	json.loads(x["payload"])["victimIP"] not in dicVictimIP:
					dicVictimIP[json.loads(x["payload"])["victimIP"]]=[0]
					json_list_dicVictimIP.append(x)
				if json.loads(x["payload"])["victimIP"] in dicVictimIP:
					dicVictimIP[json.loads(x["payload"])["victimIP"]][0]=dicVictimIP[json.loads(x["payload"])["attackerIP"]][0]+1
				#To know the victim IP attacked by how many different IP addresses	
		except KeyError: 
			pass
	print "(Connection Type, Frequence)"
	for key in dic_connectionType.iteritems():
		print (key) 		
	print "Source:", "Honeypot"		
	print "The total number of attack on victim Port ", Input," is :",(len(IP_list)) 
	print "The attacks happended on ",len(dict)," days"
	while True:
		try:
			cont = raw_input('Do you want to display the attacked time in detail?(y/n)')
			if(yes_or_no(cont)):
				print "(Date,Frequence)"
				for key, value in sorted(dict.iteritems(), key=lambda x:x[1],reverse=True):
					print (key,value)
			break
		except:	
			cont = ''  
			print "Please try again!"	
	while True:
		try:
			cont = raw_input('Do you want to display the attacked IP in detail?(y/n)')
			if(yes_or_no(cont)):
				for key, value in sorted(dicAttackIP.iteritems()):
					print (key)
			break
		except:
			cont = '' 
			print "Please try again!"	
	while True:
		try:
			cont = raw_input('Do you want to display the victim IP in detail?(y/n)')
			if(yes_or_no(cont)):
				for key, value in sorted(dicVictimIP.iteritems()):
					print (key)
			break
		except:
			cont = '' 
			print "Please try again!"	
							
def AttackPortFunc():	
	for x in data:
		try:
			if (json.loads(x["payload"])["attackerPort"] == Input):
				IP_list.append(x)
				ct=json.loads(x["payload"])["connectionType"]
				if ct not in dic_connectionType:
					dic_connectionType[ct]=[0]
				if ct in dic_connectionType:
					dic_connectionType[ct][0]=dic_connectionType[ct][0]+1
				# Store the connection type
				TimeDate=x["timestamp"]["$date"].split('T')
				if TimeDate[0] not in dict:
					dict[TimeDate[0]]=[0]
				if TimeDate[0] in dict:
					dict[TimeDate[0]][0]=dict[TimeDate[0]][0]+1
				#Split the timestamp and store them into dictionary to know when the victim IP attack.
				if 	json.loads(x["payload"])["attackerIP"] not in dicAttackIP:
					dicAttackIP[json.loads(x["payload"])["attackerIP"]]=[0]
					json_list_dicAttackIP.append(x)
				if json.loads(x["payload"])["attackerIP"] in dicAttackIP:
					dicAttackIP[json.loads(x["payload"])["attackerIP"]][0]=dicAttackIP[json.loads(x["payload"])["attackerIP"]][0]+1		
				if 	json.loads(x["payload"])["victimIP"] not in dicVictimIP:
					dicVictimIP[json.loads(x["payload"])["victimIP"]]=[0]
					json_list_dicVictimIP.append(x)
				if json.loads(x["payload"])["victimIP"] in dicVictimIP:
					dicVictimIP[json.loads(x["payload"])["victimIP"]][0]=dicVictimIP[json.loads(x["payload"])["attackerIP"]][0]+1
				#To know the victim IP attacked by how many different IP addresses	
		except KeyError: 
			pass
	print "(Connection Type, Frequence)"
	for key in dic_connectionType.iteritems():
		print (key) 		
		print "Source:", "Honeypot"		
	print "The total number of attack on victim Port ", Input," is :",(len(IP_list)) 
	print "The attacks happended on ",len(dict)," days"
	while True:
		try:
			cont = raw_input('Do you want to display the attacked time in detail?(y/n)')
			if(yes_or_no(cont)):
				print "(Date,Frequence)"
				for key, value in sorted(dict.iteritems(), key=lambda x:x[1],reverse=True):
					print (key,value)
			break
		except:	
			cont = ''  # not yes and not no, so it'll loop again.
			print "Please try again!"	
	while True:
		try:
			cont = raw_input('Do you want to display the attacked IP in detail?(y/n)')
			if(yes_or_no(cont)):
				for key, value in sorted(dicAttackIP.iteritems()):
					print (key)
			break
		except:
			cont = '' 
			print "Please try again!"	
	while True:
		try:
			cont = raw_input('Do you want to display the victim IP in detail?(y/n)')
			if(yes_or_no(cont)):
				for key, value in sorted(dicVictimIP.iteritems()):
					print (key)
			break
		except:
			cont = '' 
			print "Please try again!"	
			
InputType=InputFunc()

with open('honeypot.json') as data_file:   
	for line in data_file:
		data.append(json.loads(line))

if (InputType == 1):
	print "1.Attack IP"
	print "2.Victim IP"
	while True:
		try:
			TypeInput= int(raw_input("Please enter the IP type:"))
			if TypeInput ==1:
				Input= raw_input("Please enter the attack IP address:")
				attackerIPFunc()
				break
			elif TypeInput ==2:
				Input= raw_input("Please enter the victim IP address:")
				VictimIPFunc()
				break
		except ValueError:
			print "Please try again"
# It handles IP part		
elif (InputType == 2):	
	while True:
		try:
			Input= raw_input("Please enter the domain:")
			print "Developing..."
		except ValueError:
			print "Please try again"

elif (InputType == 3):	
	while True:
		try:
			Input= raw_input("Please enter the domain:")
			print "Developing..."
		except ValueError:
			print "Please try again"
			
elif (InputType == 4):	
	while True:
		try:
			Input= raw_input("Please enter the domain:")
			print "Developing..."
		except ValueError:
			print "Please try again"

elif (InputType == 5):
	while True:
		try:
			Input= raw_input("Please enter the domain:")
			print "Developing..."
		except ValueError:
			print "Please try again"
	
elif (InputType == 6):
	print "1.Attacker Port"
	print "2.Victim Port"
	while True:
		try:
			TypeInput= int(raw_input("Please enter the port type:"))
			if TypeInput ==1:
				Input= int(raw_input("Please enter the attack port:"))
				AttackPortFunc()
				break
			elif TypeInput ==2:
				Input= int(raw_input("Please enter the victim port:"))
				VictimPortFunc()
				break
		except ValueError:
			print "Please try again"
# It handles port part		






