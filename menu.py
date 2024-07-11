# creating menu program files


import os
print("\t\t\tWelcome to Menu Tools")
print("\t\t\t---------------------")

print("""
      press 1: to open notepad
      press 2: to open chrome
      press 3: to open vlc
      press 4: to open whatsapp
      """)
ch=input("Enter your choice: ")
print(ch)
 
if ("notepad" in ch) or ("editor" in ch) and (not("don't" in ch)):
    os.system("notepad")
elif ("chrome" in ch) or ("google" in ch):
    os.system("opera")
elif (ch)==3:
    os.system("vlc")
elif (ch)==4:
    os.system("whatsapp")
else:
    print("please select corect option")



# exp=float(input("Enter your experience:"))
# (exp>2 or print("no job")) and print("will get job")
