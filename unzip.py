import os
from pyunpack import Archive

def GetZipPath():
	mypath = os.getcwd()
	filesList=[]

	for root, dirs, files in os.walk(mypath):
		for filename in files:
			if (".zip" in filename or
				".7z" in filename or
				".rar" in filename):
				filepath = os.path.join(root, filename)
				filesList.append([root,filepath])
			

	return filesList


def main():
	files=GetZipPath()
	for file in files:
		try:
			Archive(file[1]).extractall(file[0])
		except :
			print(file)
			print("----------error---------------")
	print("Done!")
	

if __name__ == "__main__":
	main()