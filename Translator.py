#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
This is the module that contains a function that translate the code obtained 
from the file and saves it into a new list.
"""

def translate(list code):
    """
    This function contains the algorithm needed to translate the code.
    """

    #Here are defined some dictionaries that will have the mnemonics and
    #registers with their respective value.
    mnemRegs = {"add": 0, "addi": 1, "and": 2, "andi": 3,
                "beq": 4, "bne": 5, "j": 6, "jal": 7,
                "jr": 10, "lb": 11, "or": 12, "sb": 13, 
                "sll": 14, "srl": 15, "x0": 0,"x1": 1,
                "x2": 2, "x3": 3, "x4": 4, "x5": 5,"x6": 6,
                "x7": 7}
    orderAppend = {"std1" : [2, 3, 1], "std2" : [3, 2, 1], "off1" : [1, 2],
                "off2" : [3, 1], "imm0" : [2, 1]}

    #Dictionary that will contain the labels of the code, if there's any
    labels = {}
    #List that will contain the lines of translated code
    ensa = []
    
    #In this for cycle the program will identify all the labels with their
    #respective memory address
    pc = 0
    for line in code:
        pc += 1
        islabel = line.split(":")
        if (len(islabel) == 2):
            labels[islabel[0]] = pc

    #It's necessary to identify first the labels.
    #In this cycle, the program will iterate the lines of code 
    codet = []
    pc = 0
    for line in code:
        #This part of the code will split the line into arguments.
        #Eliminating the labels
        pc += 1
        instr = line.split(":")
        if (len(instr) == 2):
            instr = instr[1]
        instr = instr.split(",")
        i = 0
        while (i < len(instr) ):
            instr[i] = instr[i].strip()
            i++
        #The list instr now have the instruction arguments individualy

        #Here, the code will process the arguments to create a list
        #with the equivalent values of the arguments
        codet.append( mnemRegs.get( instr[0], "Abscent") )
        
        if (codet[0] == "Abscent"):
            print(f"Error en la linea: {pc}, no se reconoce la operacion")
            return 0

        elif (len(instr) == 2):

            if (codet[0] == 6 or codet[0] == 7):
                codet.append( labels.get( instr[1] ) ) 
            elif (codet[0] == 10):
                codet.append( mnemRegs.get( instr[1] ) ) 
                
            else:
                print(f"Faltan argumentos en la linea {pc}")
                return 0
        
        elif (len(instr) == 4):
            if (codet[0] == 0 or codet[0] == 2 or codet[0] == 12):
                corris = orderAppend("std1")

            elif (codet[0] == 14 or codet[0] == 15):
                corris = orderAppend("std2")

            elif (codet[0] == 4 or codet[0] == 5):
                corris = orderAppend("off1")

            elif (codet[0] == 11 or codet[0] == 13):
                corris = orderAppend("off2")

            elif (codet[0] == 1 or codet[0] == 3):
                corris = orderAppend("imm0")

            else:
                print(f"Se ha cometido un error en la linea {pc}")
                return 0

            for z in corris:
                codet.append( instr[z] )
        elif ():
            print(f"Error: Revise la linea de codigo {pc}")


if __name__ == "__main__":
    #ejecuta funcion

