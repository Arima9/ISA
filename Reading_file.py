#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
""" 
    This program reads a file that the user want to transform (codigo1.txt,
    codigo2.txt, codigo3.txt, codigo4.txt) and returns a tupple with the 
    content of  the file read.
"""
def lectura_archivo(nombre):
    #Module that returns a list with all the arguments of a file"

    nombre_archivo = nombre      #File that we want to read"
    valores = open(nombre_archivo)
    lineas = valores.readlines()
    lineas = list(map(lambda l: l.rstrip('\n'), lineas))
    return lineas

if __name__ == "__main__":

    print(lectura_archivo("codigo1.txt"))

