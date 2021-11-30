# in this code we check if a string is acceptable in Automatas A & B 
# 
# Nov. 2021
# Seyed Nami Modarressi

# Todo :
#  1 ) input String and machines
#  2 ) write accept function
#  3 ) use function for A and B and String 
#  4 ) add an example

alphabet = []
automata_A = []
automata_B = []
input_String = ""


alphabet = input("\n\nEnter alphabet with ',' (exp. :  a,b,c  or  0,1) :")
alphabet = alphabet.split(",")
input_String = input("\nEnter String :")
in_alphabet_flag = 0
for i in input_String:
    for j in alphabet:
        if i == j:
            in_alphabet_flag = 1
            break
    if in_alphabet_flag == 1:
        break
if in_alphabet_flag == 0:
    print("\nInvalid String . Insert String with given alphabet")
else:
    # String is OK
    # now we get machines
    print("\nOK String")

