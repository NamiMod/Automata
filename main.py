# in this code we check if a string is acceptable in Automatas A & B 
# 
# Nov. 2021
# Seyed Nami Modarressi

import numpy as np

def accept(automata , automata_finals , alphabet ,alphabet_size , input_string):
    # in this function we insert input_string in automata and get result
    # result :
    # 1 ==> input string is acceptable
    # 0 ==> input string is not acceptable
    counter = 0 
    state = 0 # ==> We start from node 0
    while counter < len(input_string):
        action = input_string[counter]
        action_number = 0
        flag = 0
        for i in range(0,alphabet_size):
            if action == alphabet[i]:
                action_number = i
                flag = 1
                break
        if flag == 0:
            return 0
        state = int(automata[state][action_number])
        counter = counter + 1

    for i in automata_finals:
        if state == int(i):
            return 1
    return 0

# main program 
alphabet = []
automata_A = []
automata_A_size = 0
automata_A_finals = []
automata_B = []
automata_B_size = 0
automata_B_finals = []
input_String = ""

alphabet = input("\n\nEnter alphabet with ',' (exp. :  a,b,c  or  0,1) :")
alphabet = alphabet.split(",")
input_String = input("\nEnter string :")
in_alphabet_flag = 0
for i in input_String:
    for j in alphabet:
        if i == j:
            in_alphabet_flag = 1
            break
    if in_alphabet_flag == 1:
        break
if in_alphabet_flag == 0:
    print("\nInvalid string . Enter string with given alphabet")
else:
# String is OK
# now we get machine A
    automata_A_size = int(input("\nEnter number of nodes(states) for first machine :"))
    automata_A = input("\nEnter transition table for first machine (from [0,0] to [size,size] with ',' like alphabet) :")
    automata_A = automata_A.split(",")
    temp = np.reshape(automata_A , (automata_A_size,len(alphabet)))
    automata_A = temp
    print("\nFirst Machine : \n")
    print("       ",end="")
    for i in alphabet:
        print(i , end="  ")
    print("\n",end="")
    print("------"*len(alphabet))
    for i in range(0 , automata_A_size):
        print("Q",end="")
        print(i,end="")
        print(" |   ",end="")
        for j in range(0 , len(alphabet)):
            print(automata_A[i][j] , end="  ")
        print("\n")
    automata_A_finals = input("\nEnter 'Goal' nodes for first machine(without 'Q' - with ',' like alphabet) :")
    automata_A_finals = automata_A_finals.split(",")
    # now we get machine B
    automata_B_size = int(input("\nEnter number of nodes(states) for second machine :"))
    automata_B = input("\nEnter transition table for first machine (from [0,0] to [size,size] with ',' like alphabet) :")
    automata_B = automata_B.split(",")
    temp = np.reshape(automata_B , (automata_B_size,len(alphabet)))
    automata_B = temp
    print("\nSecond Machine : \n")
    print("       ",end="")
    for i in alphabet:
        print(i , end="  ")
    print("\n",end="")
    print("------"*len(alphabet))
    for i in range(0 , automata_B_size):
        print("P",end="")
        print(i,end="")
        print(" |   ",end="")
        for j in range(0 , len(alphabet)):
            print(automata_B[i][j] , end="  ")
        print("\n")
    automata_B_finals = input("\nEnter 'Goal' nodes for second machine(without 'P' - with ',' like alphabet) :")
    automata_B_finals = automata_B_finals.split(",")
    # now we check input_string in machines
    result_A = accept(automata_A,automata_A_finals,alphabet,len(alphabet),input_String)
    result_B = accept(automata_B,automata_B_finals,alphabet,len(alphabet),input_String)
    if result_A == 1 and result_B == 1:
        print("\nAnswer : input String is acceptable in both machines\n")
    elif result_A == 1 and result_B == 0:
        print("\nAnswer : input String is acceptable in first machine but it's not acceptable in second one\n")
    elif result_A == 0 and result_B == 1:
        print("\nAnswer : input String is acceptable in second machine but it's not acceptable in first one\n")
    elif result_A == 0 and result_B == 0:
        print("\nAnswer : input String is not acceptable in machines\n")