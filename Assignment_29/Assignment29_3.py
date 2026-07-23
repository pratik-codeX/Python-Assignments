import io
import sys

def main():
    

    try:
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("Run Application as : python Filename.py File1.txt File2.txt")
            return
        FileName1 = sys.argv[1]
        FileName2 = sys.argv[2]
        fobj1 = open(FileName1,"r")
        print("File Present")
        fobj2 = open(FileName2,"w")
  
    except IndexError as iobj:
        print("Enter Command Line Argument")
        print("Enter : --h for help")
        return
    except FileNotFoundError as fobj:
        print("File Not Found in Current Folder")
    except Exception as eobj:
        print("Error :",eobj)

    offset = fobj1.seek(0,2)

    fobj1.seek(0,0)

    while(offset > 0):
        Buffer = fobj1.read(io.DEFAULT_BUFFER_SIZE)
        fobj2.write(Buffer)
        offset = offset - 1

    fobj1.close()
    fobj2.close()



if __name__ == "__main__":
    main()