'''
Q2) Count Words in a File
Problem Statement:
Write a program which accepts a file name from the user 
and counts the total number of words in that file.
Input:
Demo.txt
Expected Output:
Total number of words in Demo.txt.
'''
import os 

def main():

	FileName = (input("Enter File Name : "))

	if(os.path.exists(FileName) == False):
		print("File is Not present in Directory")
		return

	fobj = open(FileName,"r")
	Count = 0
	
	Data = fobj.read()
	
	for i in Data:
		Count = Count + 1
				
	print(f"Total Words in {FileName} Lines are : ",Count)
    
if __name__ == "__main__":
    main()