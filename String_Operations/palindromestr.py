def palindrstr(str):
   count=0
   upperst= str.upper()
   for i in range(len(upperst)):
       if upperst[i]!=upperst[len(upperst)-i-1]:
           count += 1
           break

   if count == 0:
       print("Palindrome")
   else:
       print("Not Palindrome")

