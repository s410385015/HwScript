import sys, os, getopt

def main():
	mypath = os.getcwd()
	name="\\record.txt"
	record= "\""+mypath+name+"\""
	print(record)
	for root, dirs, files in os.walk(mypath):
			os.system("echo -------------- >> "+record)
			os.system("echo "+root+" >> "+record)
			cppList=[]
			for file in files:
				if(".cpp" in file):
					cppList.append(file)
			if(len(cppList)!=0):
				os.chdir(root)
				fullname=" ".join(cppList)
				if os.system("g++ "+fullname+" -std=c++11") == 0:
					os.system("a.exe >> "+record)
					print (root+"-done!")
				else:
					print(root)
					os.system("echo error >> "+record)
if __name__ == "__main__":
	main()