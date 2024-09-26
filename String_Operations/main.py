# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import palindromestr as ps
import reverseStr as rs
import findsubst as find




if __name__ == '__main__':
   while(True):
       str = input("Enter a string: ")
       opt = int(input('''Choose what operation you want to perform:
                   1 = Length of string
                   2 = Compare with other string
                   3 = Check for palindrome
                   4 = Find a substring
                   5 = Reverse the string
                   '''))
       if opt<1 or opt>5:
           print("Invalid input")
       elif opt==1:
           print("length of the string is ", len(str))
       elif opt==2:
           str2=input("Enter second string: ")
           if str==str2:
               print("Strings are same")
           else:
               print("Strings are not same")
       elif opt==3:
           ps.palindrstr(str)
       elif opt==4:
           find.substr(str)
       elif opt==5:
           rs.revStr(str)


       cont=int(input("Do you want to continue? Press 1 to continue and 0 to terminate "))
       if cont==0:
           break

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
