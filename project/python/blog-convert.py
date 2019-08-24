#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
from subprocess import Popen
import sys

inFile = sys.argv[1]
Popen('jupyter nbconvert '+inFile +' --template basic', shell=True).wait()
newFile = os.path.splitext(inFile)[0]+'.html'

template = open('template.html', 'r').read()

read_navbar = open('navbar.txt', 'r').read()
read_css = open('main_css.txt', 'r').read()
read_gs = open('main_js.txt','r').read()
read_body = open(newFile, 'r').read()
read_mathjax = open('mathjax.txt', 'r').read()

template = template.replace("navbar_block", "\n" + read_navbar + "\n")
template = template.replace("js_block", "\n" + read_gs + "\n")
template = template.replace("css_block", "\n" + read_css + "\n")
template = template.replace("body_block", "\n" + read_body + "\n")
template = template.replace("math_block", "\n" + read_mathjax + "\n")

with open(newFile, 'w') as f:
    f.write(template)


# In[ ]:




