#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import with_statement
import os


def help():
	import textwrap
	print textwrap.dedent("""\
		ChangeFilename  - script para troca de trechos dos nomes de arquivos
		Uso: python ChangeFilename  trecho_a_ser_trocado  trecho_a_ser_trocado  /caminho/para/os/arquivos
		""")


def  change(old, new, basedir):
 	# caminhar pelas pastas
 	for root, dirs, files in os.walk(basedir):
 		for name in files:
 			newname = name.replace(old,new)
 			# print newname
 			os.rename(name,newname)

# tudo começa aqui
if __name__ == '__main__':
	import sys
	if len(sys.argv) < 3:
		help()
	else:
		change(sys.argv[1],sys.argv[2],sys.argv[3])