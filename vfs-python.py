
import os
import sys
import shutil

device=raw_input("Enter device name: ")
directory=raw_input("Enter directory name: ")
size=raw_input("Enter size of file system(in mb): ")			#Size of file system required.
size=int(size)*2048
print "Creating file"
os.system("dd if=/dev/zero of="+device+" count="+str(size))
print "Creating ext3 file system"
os.system("mkfs -t ext3 -q "+device)					#To make ext3 file system.
print "Creating directory"
os.system("mkdir "+directory)
print "Mounting file system"
os.system("sudo mount -o loop=/dev/loop0 "+device+" "+directory)	#Mounting loop device
os.chdir(directory)
var = 0
while var!=13:
	print("\n1. Create directory")
	print("2. Print current working directory")
	print("3. Change directory")
	print("4. Remove empty directory")
	print("5. Remove directory recursively")
	print("6. Print contents of directory")
	print("7. Create file")
	print("8. Rename file")
	print("9. Copy file")
	print("10. Read file and display contents")
	print("11. Display status of file or file system")
	print("12. Delete file")
	print("13. Unmount virtual file system and exit")
	var =	raw_input("Enter option: ")
	
	if(var =='1'):
		s=raw_input("Enter directory name: ")
		if not os.path.exists(s):
			os.mkdir(s)
		else:
			print("Directory "+s+" already exists")

	elif(var =='2'):
		print("Current working directory: "+os.getcwd())

	elif(var =='3'):
		s=raw_input("Enter path: ")
		if os.path.exists(s):
			os.chdir(s)
		else:
			print("Path invalid")


	elif( var =='4'):
		s=raw_input("Enter path: ")
		if os.path.exists(s):
			os.rmdir(s)
		else:
			print("Path invalid")

	elif(var =='5'):
		s=raw_input("Enter path: ")
		if os.path.exists(s):
			os.removedirs(s)
		else:
			print("Path invalid")

	elif(var =='6'):
		s=os.listdir(os.getcwd())
		for filename in s:
			print(filename)

	elif( var =='7'):
		s=raw_input("Enter file name: ")
		print("Enter data in file: ")
		w=sys.stdin.read()
		ptr=open(s,"w+")
		ptr.write(w)
		ptr.close()

	elif(var =='8'):
		src=raw_input("Enter source name: ")
		dst=raw_input("Enter new name: ")
		if os.path.isfile(src):
			os.rename(src,dst)
		else:
			print("File not found")

	elif(var =='9'):
		src=raw_input("Enter source path: ")
		dst=raw_input("Enter destination path: ")
		if os.path.isfile(src):
			shutil.copy2(src, dest)
		else:
			print("File not found")

	elif(var =='10'):
		s=raw_input("Enter file name: ")
		if os.path.isfile(s):
			ptr=open(s,"r+")
			print(ptr.read())
		else:
			print("File not found")

	elif( var=='11'):
		s=raw_input("Enter path: ")
		if os.path.isfile(s) or os.path.exists(s):
			info=os.lstat(s)					#Using inode information 
			print("Protection bits: "+str(info.st_mode))
			print("Inode number: "+str(info.st_ino))
			print("Device: "+str(info.st_dev))
			print("Number of hard links: "+str(info.st_nlink))
			print("User ID of owner: "+str(info.st_uid))
			print("Group ID of owner: "+str(info.st_gid))
			print("Size: "+str(info.st_size))
			print("Time of most recent access: "+str(info.st_atime))
			print("Time of most recent content modification: "+str(info.st_mtime))
			print("Time of most recent metadata change: "+str(info.st_ctime))
		else:
			print("Path invalid")

	elif(var =='12'):
		s=raw_input("Enter file name: ")
		if os.path.isfile(s):
			os.remove(s)
		else:
			print("File not found")

	elif(var=='13'):
		os.chdir("/home/satyam/")				# Here give the name of your home directory 
		os.system("sudo umount "+directory)
	else:
		print("Wrong option!")

