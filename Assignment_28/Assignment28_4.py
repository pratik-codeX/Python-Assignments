'''
Q4) Copy File Contents into Another File
Problem Statement:
Write a program which accepts two le names from the user.
•First le is an existing le
•Second le is a new le
Copy all contents from the rst le into the second le.
Input:
ABC.txt Demo.txt
'''
import os 

def main():

	FileName1 = (input("Enter Existing File Name : "))
	FileName2 = (input("Enter New File Name : "))

	fobj1 = open(FileName1,"r")
	fobj2 = open(FileName2,"w")


	if(os.path.exists(FileName1) == False):
		print("File is Not present in Directory")
		return
	
	for text in fobj1:
		fobj2.write(text)
		

	
    
if __name__ == "__main__":
    main()