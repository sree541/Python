#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys;

wfile = open(sys.argv[1], 'r');
fline = wfile.readlines();

#print (fline);
#print (fline[1]);
ofile = open('addsec.txt','a');
for line in fline:
   rline=line;
   line=line.split(' ');
   secline='<e';
   #secline=secline.split(' ');
   #print (secline);#i=0;
   for index in range(len(line)): 
      if (line[index]==secline):
         ofile.write(rline);
         #ofile.write('xxx');
         
         #print (line[index]);
         #for i in range (1,4):
		#ofile.write(line);	
       #  print('loop is okay!');

