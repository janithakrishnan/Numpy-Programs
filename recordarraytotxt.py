#!/usr/bin/env python3

#CREATE RECORD ARRAY AND SAVE TO TXT FILE
import numpy as np
import pandas as pd
from pandas import DataFrame as f
ndt=np.dtype([('rollno','i8'),('name','<U15'),('totalmarks','i8')])
a1=np.empty((0,),ndt)
total=0
for _ in range(int(input('Enter the no:of students:'))):
	roll=int(input('Enter the roll no:'))
	name=input('Enter the name:')
	marks=int(input('Enter the marks:'))
	newrow=np.array([(roll,name,marks)],dtype=ndt)
	a1=np.concatenate((a1,newrow))
	total=total+marks
lastrow=np.array([(0,'GrandTotal',total)],dtype=ndt)
a1=np.concatenate((a1,lastrow))
np.savetxt('student.txt',a1,fmt='%s',delimiter=',')
