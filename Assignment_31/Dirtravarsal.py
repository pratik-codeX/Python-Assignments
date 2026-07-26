import os 

Num = 0
subNum = 0
for FolderName,Subfolder,FileName in os.walk("Hello"):
    print("Scanned :",FolderName)
    print("Folder Name is : ",FolderName)
    for Fname in FileName:
        Num = Num + 1
        Fname = os.path.join(FolderName,Fname)
        print("FileName is : ",Fname)

print("Sub Directories : ",subNum)
print("File count are  : ",Num)