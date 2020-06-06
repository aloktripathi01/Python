#f = open("palindrome.py", mode='r', encoding='utf-8')

#f.close()
with open("palindrome.py",'w',encoding = 'utf-8') as f:
   f.write("my first file\n")
   f.write("This file\n\n")
   f.write("contains three lines\n")