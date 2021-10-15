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
    mnemos = {"add": 0, "addi": 1, "and": 2, "andi": 3, "beq": 4, "bne": 5,
              "j": 6, "jal": 7, "jr": 10, "lb": 11, "or": 12, "sb": 13, 
              "sll": 14, "srl": 15}
    regs = {"x0": 0,"x1": 1, "x2": 2, "x3": 3, "x4": 4, "x5": 5,"x6": 6,
            "x7": 7, "C2": 0, "zero": 0}
    orderAppend = {"std1" : [2, 3, 1, 4], "std2" : [3, 2, 1, 4], 
            "off1" : [1, 2, 3], "off2" : [3, 1, 2], "imm0" : [2, 1, 3]}
    binformat = {"type1" : [4,3,3,3,5], "type2" : [4,3,3,8]}

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
            labels[islabel[0].strip()] = pc

    #It's necessary to identify first the labels.
    #In this cycle, the program will iterate the lines of code 
    codet = []
    pc = 0
    for line in code:
        #This part of the code will split the line into arguments.
        #Eliminating the labels
        pc += 1
        instr = instr.split(":")
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
        if (instr[0] in mnemos):
            codet.append( mnemos[ instr[0] ] )
        else:
            print(f"Error en la linea: {pc}, no se reconoce la operacion")
            return 0

        if (len(instr) == 2):

            if (codet[0] in [6,7]):
                codet.append(0)
                codet.append(0)
                codet.append( labels.get( instr[1] ) ) 
            elif (codet[0] == 10):
                codet.append( regs.get( instr[1] ) ) 
                codet.append(0)
                codet.append(0)

                
            else:
                print(f"Faltan argumentos en la linea {pc}")
                return 0
        
        elif (len(instr) == 4):
            #If equal to an add, and or or instruction, std1 pattern is added
            if (codet[0] in [0, 2, 12]):
                corris = orderAppend("std1")
                instr.append("zero")

            #If equal to sll or srl instruction, std2 pattern is added.
            elif (codet[0] in [14, 15]):
                corris = orderAppend("std2")
                instr.append("zero")

            #If equal to beq or bne instruction, off1 pattern is added.
            elif (codet[0] in [4, 5]):
                corris = orderAppend("off1")
                regs["C2"] = (-1 * labels.get(instr[3])) & (2**8-1)
                instr[3] = "C2"

            #If equal to lb or sb instruction, off2 pattern is added.
            elif (codet[0] in [11, 13] ):
                corris = orderAppend("off2")
                regs["C2"] = (-1 * labels.get(instr[2])) & (2**8-1)
                instr[2] = "C2"

            #If equal to addi or andi instruction, imm0 pattern is added.
            elif (codet[0] in [1, 3]):
                corris = orderAppend("imm0")
                regs["C2"] = eval(instr[3])
                if regs["C2"] < 0:
                    regs["C2"] = regs["C2"] & (2**8-1)
                instr[3] = "C2"

            else:
                print(f"Se ha cometido un error en la linea {pc}")
                return 0

            for z in corris:
                codet.append( regs.get( instr[z] ) )

            #At this point we have a decoded list with the opcodes and
            #values of registers, labels and constants in decimal base.
            #Now the next part is to transform them into binary code.
            if codet[0] in [0,2,12,14,15]:
                patt = binformat["type1"]
            else codet[0] in [1,3,4,5,6,7,10,11,13]):
                patt = binformat["type2"]

            binarytext = ""
            i = 0
            while (i < len(codet) ):
                binarytext += "{:0{patt[i]}b}".format(codet[i])
                i++

            ensa.append(binarytext)

        else:
            print(f"Error: Revise la linea de codigo {pc}")
    
    return ensa

if __name__ == "__main__":
    codigo_prueba = ["addi,x1,x0,1",
                     "addi,x2,x0,0x02",
                     "addi,x3,x0,0xA0",
                     "addi,x4,x0,-1",
                     "add,x6,x2,x1",
                     "and,x7,x4,x3",
                     "or,x5,x3,x4",
                     "sll,x3,x3,x1",
                     "srl,x3,x3,x1"]
    
    print(translate(codigo_prueba))


