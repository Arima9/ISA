#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
""" 
    This module is going to write a file with the content of the module 2 and
    save it with the name given on the command line when running the executable
    main program.
"""
def module3(nombre,parameters):
    f_out = open(nombre, "w")
    for combinacion in range(len(parameters)):
        print(parameters[combinacion])
        f_out.write(parameters[combinacion])

    f_out.close()
    
if __name__ == "__main__":    
    codigo = 'codigo1.txt'
    lista = ["0000101010111", "00010110000100","1101010111000000"] 
    module3(codigo, lista)


