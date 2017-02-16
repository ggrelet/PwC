#!/usr/bin/python2.7
#-*- coding: utf-8 -*-
import sys, xlrd	


if sys.argv[1][-4:] != "xlsx":
	raise Exception("N'est pas un fichier excel")
else:
	f = xlrd.open_workbook(sys.argv[1])

print(f[:])