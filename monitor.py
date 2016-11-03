"""
	Created on Oct 28th, 2016
	Last Revised Date on Oct 29th, 2016
	@author: Chih-Chao chang 
"""
import os
import fnmatch
import gzip, bz2
import smtplib
import getpass
import re

def gen_open(filenames):
	for name in filenames:
		if name.endswith(".gz"):
			yield gzip.open(name)
		elif name.endswith(".bz2"):
			yield bz2.BZ2File(name)
		else:
			yield open(name)

def gen_find(filepat,top):
	for path, dirlist, filelist in os.walk(top):
		for name in fnmatch.filter(filelist,filepat):
			yield os.path.join(path,name)

def gen_cat(sources):
	for s in sources:
		for item in s:
			yield item

def gen_grep(pat, lines):
	patc = re.compile(pat)
	for line in lines:
		if patc.search(line): yield line

def lines_from_dir(filepat, dirname):
	names = gen_find(filepat,dirname)
	files = gen_open(names)
	lines = gen_cat(files)
	return lines

def send_email(msg):
	while True:
		from_addr="b95702041@gmail.com"
		# This could ve reset to akuna email address
		subject = "Alert"
		portNumber = "587"
		text = msg
		passwdEmail = getpass.getpass("Please enter the email password for "+ from_addr+"\n")
		smtp_server = "smtp.gmail.com" 
		# I set gmail as default. it could be changed to akuna email smtp server
		try:
			server = smtplib.SMTP(smtp_server, portNumber) 
			server.starttls()
			server.login(from_addr, passwdEmail)
			break
		except:
			print ("failed to connect, please try again")

	to_addr = "cchan113@jhu.edu"
	try:
		msg = "\r\n".join([
		"From: " + from_addr,
		"To: " + to_addr,
		"Subject: "+ subject,
		 "",
		text
		])
		server.sendmail(from_addr, to_addr, msg)
		print ("successfully sent the email to Admin ")
	except:
		print ("failed to send email to Admin")
	server.quit()

if __name__ == '__main__':
	lines=lines_from_dir("*.log","/var/log")
	for line in lines:
		#if "DEBUG" in line:
		#	print (line)
		#	send_email(line)
		if "ERROR" in lines:
			print (line)
			send_email(line)
