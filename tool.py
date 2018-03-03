import os,commands,time,sys

username = commands.getstatusoutput("whoami")[1] #taking the name of current user

files =  os.listdir("/home/" + username + "/Desktop") #list of all the file/folers on desktop

print "moving files.."

for file in files:
	if file.rfind(".")>=0:
		extension = file[file.rfind(".")+1:].upper() #check if the filename has an extension 

		if not os.path.isdir("/home/" + username + "/Documents/DesktopFiles/" + extension):
			os.makedirs("/home/" + username + "/Documents/DesktopFiles/" + extension) #make directory with the name of extension if not present
		src = os.path.join("/home/" + username + "/Desktop", file)
		dest = os.path.join("/home/" + username + "/Documents/DesktopFiles", extension)
		f = 'mv ' + src +" " + dest #move the file fron desktop to Documents
		try:
			commands.getstatusoutput(f)
		except:
			""
print "\nAll files moved from Desktop to 'DesktopFiles' in Documnets"
print "\n***********************************************************************************\n\nPrintng top 10 files"

'''
***********all files moved.Script below lists the top 10 biggest file in '/home'*********
'''


top_10= [{0.0 : "hello"}]*10; #cearting a list of 10 items which will store 10 largest files
#current_user = commands.getstatusoutput("whoami") #taking the name of current user
#dir = "/home/" + current_user[1] + "/" #directory to search recursively
print "\nLet me explore your files...please wait....It may take time...\n\n"

for dirpath, dirs, files in os.walk("/home/"): #accessing all folders recursively
	for file_name in files:
		file_path = os.path.join(dirpath,file_name) #to get absolute path of the file 
		try:						#to handle Errors especially "OSError: [Errno 2] No such file or directory"
			file_size = float(os.path.getsize(file_path))/(1024**2) #converting file sizes from bytes to MBs
			if(file_size > (top_10[0].keys())[0]): #comparing if size of present file lies in present top 10
				index = 10    #it will keep track of index to insert the new file
				for x in reversed(top_10):  #comparision starts from largest element
					if file_size>x.keys()[0]:
						top_10.insert(index,{file_size:file_path}) #inserting present file at right place  
						top_10.pop(0)			#popping the file with smallest size
						break
					index=index-1
		except :				#if error occurs "do nothing just skip the file"
			""
print "Top 10 file are:\n\n"
x = "SIZE\t\tFILE_NAME\n\n"
for top in reversed(top_10):  #print the size of top 10 files with its absolute path
	x = x + str(round(top.keys()[0],2)) + " MB \t\t" + top[top.keys()[0]] + "\n"
#	print str(round(top.keys()[0],2)) + " MB \t" + top[top.keys()[0]]

print x

