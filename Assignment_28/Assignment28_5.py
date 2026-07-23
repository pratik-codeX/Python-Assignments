'''
Q5) Search a Word in File
Problem Statement:
Write a program which accepts a file name and a 
word from the user and checks whether that word is present in
the le or not.
Input:
Demo.txt Marvellous
Expected Output:
Display whether the word Marvellous is found in Demo.txt or not.
'''
import os 

def main():

	FileName = input("Enter Existing File Name : ")
	word = input("Enter Word : ")
	CompStr = ""

	fobj = open(FileName,"r")

	if(os.path.exists(FileName) == False):
		print("File is Not present in Directory")
		return

	Buffer = fobj.read()

	for i in Buffer :
		if i == " ":
			CompStr = ""
		else:
			CompStr = CompStr + i
			if word == CompStr:
				print("Found")
				break
				
	'''ret = Buffer.find(word)

	if ret > 0:
		print("word is present")
	else:
		print("word is not present")'''
					
if __name__ == "__main__":
    main()