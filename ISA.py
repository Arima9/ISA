#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

#INCLUDE MODULES

"""
Main python file.
This file contain the code needed to test the modules from the project.


Team members:
    Jose Leonardo Quiniones.
    Andres Rivera Marquez.
"""

#Test lines for fist commit.
ruta = input("Ingresa el nombre del archivo: ")

f = open("./" + ruta)

print("Este es el contenido de tu archivo")
for line in f:
    print (line, end='')
