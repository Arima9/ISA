#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
    This is the main File, where the algorythm works, to produce the output that
    the user wants. Here, the 3 modules created before do their work and finally
    give the user a new file in a specific format with the new information.
"""
import argparse
from Reading_file import lectura_archivo
from translator   import translate
from Saving_file  import module3


def main():
    #These lines are to ask for some specific information in the command line of
    #the Linux terminal

    parser = argparse.ArgumentParser(description = 'Main file to obtain an txt or a bin file')
    parser.add_argument('-i','-ifile', type=str, dest = 'ifile', 
                        help = 'Please introduce the name of the input file')
    parser.add_argument('-o','-ofile', type=str, dest = 'ofile',
                        help = 'Please introduce the name you wish for the new file')
    parser.add_argument('-t','-tfile', type=str, 
                        choices = ['binario', 'bin', 'texto', 'txt'], 
                        dest = 'tfile', default = 'texto', required = False,
                        help = 'Choose what kind of file you want, text file (txt or                         texto) or binary file (binario, bin)')
    
    args = parser.parse_args()
    if (args.tfile == 'txt' or args.tfile == 'texto'):
        new_file = args.ofile + '.txt'
    else:
        new_file = args.ofile + '.bin'

    print('Archivo que quieres leer:',args.ifile)
    print('\nNombre del archivo que quieres crear:',args.ofile)
    print('\nArchivo que se creará:',new_file)

    #We call the modules that we have created before in the order we want
    info = lectura_archivo(args.ifile) 
    print('Lo que contiene el archivo:\n',info)
    #print(type(info))
    binary = translate(info)
    print('Lo que se obtiene al aplicar el algoritmo:\n',binary)
    #print(type(binary))
    module3(new_file, binary)
    print('\nSe ha creado su archivo, por favor revise en su directorio actual')




if __name__ == '__main__':
    main()


