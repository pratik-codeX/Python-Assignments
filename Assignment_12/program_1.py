'''
1. Write a program which accepts one character and checks whether it is vowel or
consonant.
Input: a
Output: Vowel
'''
###########################################################################
##   	Function Name  	:  CheckVowel
##  	Description    	:  Check Vowel or not
##  	Input          	:  Str
##	    Output         	:  boolean
##	    Date           	:  1/7/2026
##  	Author  		:   Pratik Raut
###########################################################################


def CheckVowel(Ch):
    Flag = False
    if((Ch == 'a' or Ch == 'A') or (Ch == 'e' or Ch == 'E') or (Ch == 'i' or Ch == 'I') or (Ch == 'o' or Ch == 'O') or (Ch == 'u' or Ch =='U' )):
        Flag = True

    return Flag

###########################################################################
##   	Function Name  	:  main
##  	Description    	:  Client 
##  	Input          	:  
##	    Output         	: 
##	    Date           	:   1/7/2026
##  	Author  		:   Pratik Raut
###########################################################################

def main():
    Flag = False
    Vowel = input("Enter the Character :")

    Flag = CheckVowel(Vowel)

    if(Flag == True):
        print("This is Vowel")
    else:
        print("This is not Vowel")
   
if __name__ == "__main__":
    main()