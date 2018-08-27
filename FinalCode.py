import getpass
import csv
import os
def login():
     os.system('cls')
     username=[]
     password=[]
     name=[]
     loop=True
     attempt=0
     print("~~~LOG IN PAGE~~~")
     with open(r'''PUT PATH WHERE THE FILE.TXT ARE SAVED''') as csv_file:
             csv_reader=csv.reader(csv_file, delimiter=',')
             for row in csv_reader:
                     username.append(row[0])
                     password.append(row[1])
                     name.append(row[2])
             while loop:
                     value=True
                     user=input("Username: ")
                     passw=getpass.getpass()
                     attempt+=1
                     for i in range(len(username)):
                             if user==username[i]:
                                     value=False
                                     if passw==password[i]:
                                              print("Welcome " + name[i])
                                              print("Your username is " + username[i])
                                              print("Your password is " + password[i])
                                              while True:
                                                       choice=input("Would you like to logout? (Y/N): ")
                                                       if choice=='Y'or choice=='y':
                                                                print("Logged out!")
                                                                loop=False
                                                                break
                                                       if choice=='N' or choice=='n':
                                                                print("Okay!")
                                                       else:
                                                                print("Incorrect choice!")
                                     else:
                                             print("Incorrect Password!")
                                             break
                     if value:
                             print("Incorrect Username!")
                     if attempt==5:
                             print("Reached maxed attempts of 5!")
                             break

login()