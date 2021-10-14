#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
# This program reads a file that the user want to transform (codigo1.txt,
# codigo2.txt, codigo3.txt, codigo4.txt) and returns a tupple with the content of
# the file read
def lectura_archivo():
    import sys #Module that returns a list with all the arguments of a file"

    nombre_archivo = sys.argv #File that we want to read"
    valores = open(nombre_archivo[1])
    lineas = valores.readlines()
    print(len(lineas)) 
    for x in lineas:
        print(x,end='')
    return lineas
if __name__ == "__main__":
    lectura_archivo()

