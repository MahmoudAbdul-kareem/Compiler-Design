"""
Created on Sun Dec 22 21:15:31 2024
"""

import re
rules = []
grammer = {}
dreviation = "S"
def get_grammer():
    r=input("Enter first rule of non-terminal S -> ")
    rules.append(r)
    r=input("Enter second rule of non-terminal S -> ")
    rules.append(r)
    r=input("Enter first rule of non-terminal B -> ")
    rules.append(r)
    r=input("Enter second rule of non-terminal B -> ")
    rules.append(r)
def validate_grammer():
    for rule in rules:
        if not re.fullmatch(r"[a-z][a-zSB]*",rule):
            return False
    if rules[0][0]==rules[1][0] or rules[2][0]==rules[3][0]:
        return False;
    return True;
def get_input():
    string = input("Enter string to check :")
    if re.fullmatch(r"[a-z]+",string):
        return string
def parse(string:str):
    dreviation = "S"
    while dreviation != string:
        if re.search("S",dreviation):
            index = dreviation.index("S")
            dreviation=dreviation.replace("S",grammer[('S',string[index])])
            #re.sub('S',grammer[('S',string[index])],dreviation,count=1)
        elif re.search("B",dreviation):
            index = dreviation.index("B")
            re.sub(r'B',grammer[('B',string[index])],dreviation,count=1)
        else : break
    if dreviation != string: 
        return False
    else : 
        return True

while True:
    choice = int(input("Enter choice :"))
    if choice == 1 :
        get_grammer()
        if not validate_grammer():
            print("The Grammer isn't simple.")
        grammer = {('S',rules[0][0]):rules[0],
                   ('S',rules[1][0]):rules[1],
                   ('B',rules[2][0]):rules[2],
                   ('B',rules[3][0]):rules[3]
                  }
        input_string=get_input()
        if parse(input_string):
            print("Accepted")
        else:
            print("Rejected")
    elif choice==2:
        input_string=get_input()
        if parse(input_string):
            print("Accepted")
        else:
            print("Rejected")
    else :
        break