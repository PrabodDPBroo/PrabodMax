import time
import urllib
import sys
import os

os.system('clear')

bar = "\033[1;32;40m\n________________________________________________\n"

name = """\033[1;37;40m
__________________________________________________________
\033[1;33;40m   888b     d888 8888888888 .d8888b.         d8888      8888888b.  888     888 888b    888 
\033[1;37;40m   8888b   d8888 888       d88P  Y88b       d88888      888   Y88b 888     888 8888b   888 
\033[1;33;40m   88888b.d88888 888       888    888      d88P888      888    888 888     888 88888b  888 
\033[1;37;40m   888Y88888P888 8888888   888            d88P 888      888   d88P 888     888 888Y88b 888 
\033[1;33;40m   888 Y888P 888 8888888   888  88888    d88P  888      8888888P"  888     888 888 Y88b888 
\033[1;37;40m   888  Y8P  888 888       888    888   d88P   888      888 T88b   888     888 888  Y88888 
\033[1;33;40m   888       888 888       Y88b  d88P  d8888888888      888  T88b  Y88b. .d88P 888   Y8888 
\033[1;37;40m   888       888 8888888888 "Y8888P88 d88P     888      888   T88b  "Y88888P"  888    Y888                   
\033[1;34;40m        2020 Ｎｅｗ Ｍｅｇａ Ｒｕｎ Ｓｃｒｉｐｔ  
\033[1;32;40m    ...Ａｌｌ Ｍｅｓｓａｇｅ Ｃａｎ Ｂｅ Ｇｅｔ Ｄａｔａ...                                     
\033[1;36;40m       [~] ＴＯＯＬ ＢＹ Ｔｈｉｒｄ Ｅｙｅ Ｔｅａｍ...                        
\033[1;37;40m____________________________________________________________________________________________________________________
"""     
print(name, "")


try:
    f = open("auth.txt", "r")
    auth = f.read()
    f.close 
except:
    wr = str(input("\033[1;0;40mPaste Your Auth here :- "))
    f = open("auth.txt", "w")
    f.write(wr)
    f.close
    f = open("auth.txt", "r")
    auth = f.read()
    f.close

try:
    f = open("url.txt", "r")
    f = open("url.txt", "r")
    url1 = f.read()
    f.close
except:
    wr = str(input("Paste Your URL here :- "))
    f = open("url.txt", "w")
    f.write(wr)
    f.close
    f = open("url.txt", "r")
    url1 = f.read()
    f.close

try:
    import requests


except ImportError:
    print('%s Requests isn\'t installed, installing now.')
    os.system('pip3 install requests')
    print('%s Requests has been installed.')
    os.system('clear')
    import requests


def main():
    os.system("clear")
    print(name,"\n")
    s = int(input("\033[1;0;40mEnter amount of You Want Messages - "))
    header = {"Host": "megarun.dialog.lk",
              "Authorization": auth, "X-Unity-Version": "2018.3.0f2"}
    url = url1
    
    ss = 0
    while s > ss:
        os.system("clear")
        print(name)
        size = 0
        res = requests.get(url, headers=header)
        resp = str(res)
        if resp == '<Response [204]>':
            print(bar)
            print("\n\033[1;32;40m [+] No Data ... [+]")
            print(bar)  
        elif resp == '<Response [200]>':
            print(bar)
            print("\n\033[1;32;40m [+] You Won Check Your Data Balance ... [+]")
            print(bar)
        else:
            print(bar)
            print("\n\033[1;31;40m [+] Check Again, I think You are Blocked User... [+]")
            print(bar)
        

        ss+=1
        print("\033[1;0;40m\n",str(ss), "Please Wait For Next Request",end="")
        for i in range(200):
            
            pr = i/200*100
            print("\033[1;36;40m\n>>> [+]",str(int(pr)) +"% ",end="")
            
            time.sleep(0.5)
            sys.stdout.write("\033[F")
        
    os.system('figlet FINISHED')
    again()


def again():
    again = input('\033[1;0;40m\nDo You want use again (y/n) - ')
    if again == "y" or again == "Y":
        main()
    elif again == "n" or again == "N":
        quit()
    else:
        print('\033[1;31;40mEnter valid letter')
        again()


if __name__ == "__main__":
    main()                                                                                                                                                                           
