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
		if i == "\n":
    			Count = Count + 1
				
	print(f"The Total Lines in {FileName} are :{Count}")
    
if __name__ == "__main__":
    main()