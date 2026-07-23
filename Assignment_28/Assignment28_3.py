'''
Q3) Display File Line by Line
Problem Statement:
Write a program which accepts a le name from 
the user and displays the contents of the le line by line on the
screen.
Input:
Demo.txt
Expected Output:
Display each line of Demo.txt one by one.
'''
import os 

def main():

	FileName = (input("Enter File Name : "))

	if(os.path.exists(FileName) == False):
		print("File is Not present in Directory")
		return

	fobj = open(FileName,"r")
	Count = 0
	
	print(fobj.read())
	
    
if __name__ == "__main__":
    main()