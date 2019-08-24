import sys, os, getopt


targetFile=["\"sample data.txt\""]

def main():
	mypath = os.getcwd()
	name="\\record.txt"
	record= "\""+mypath+name+"\""
	print(record)
	for root, dirs, files in os.walk(mypath):
			os.chdir(root)
			fullname=" ".join(targetFile)	
			os.system("del "+fullname)
			
if __name__ == "__main__":
	main()