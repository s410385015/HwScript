import os,shutil

sourceFile=["data.txt","main.cpp"]

def main():
	mypath = os.getcwd()

	for root, dirs, files in os.walk(mypath):
		for target in files:
			if (".h" in target or
				".cpp" in target or
				".c" in target):
				for source in sourceFile:
					if source not in files:
						shutil.copy(source,root)
				

if __name__ == "__main__":
	main()