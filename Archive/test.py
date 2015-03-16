#!/usr/bin/python
# -*- coding: utf-8 -*-

#1st python file. testing reading of hebrew file
import codecs

file = codecs.open("talmud.txt", "r", encoding="UTF-8")
text = file.read()
file.close()
f = codecs.open("talmud2.txt", "w", encoding = "utf-8")
f.write(text)
f.close()
#f = codecs.open("talmud2.txt", "a", encoding="utf-8")
#f.write(content.encode('utf-8'))
#f.write("רפי")
#f.close()
