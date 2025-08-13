#!/usr/bin/env python3
import pymysql as my
import numpy as np
import time
obj_con=my.connect(host='localhost',user='sw900b4_janitha',password='janitha123',database='sw900b4_janitha')
obj_cur=obj_con.cursor()
qstr1="""
create table stud(rollno int,name char(10),score int,primary key(rollno));
"""
obj_cur.execute(qstr1)
print("Table created")
qstr2="""
insert into stud values(101,'tom',20),(102,'raj',30),(103,'roy',25),(104,'ann',43),(105,'anu',35)
"""
obj_cur.execute(qstr2)
print("Values Inserted")
obj_con.commit()
print("Committed changes")
time.sleep(5)
#FUNCTION TO FETCH
def fetchtonumpy(stud):
	obj_cur_dict=obj_con.cursor(cursor=my.cursors.DictCursor)
	qstr3="""
	select * from stud
	"""
	obj_cur_dict.execute(qstr3)
	result=obj_cur_dict.fetchall()
	print(result)


	newdtype=[('rollno','i8'),('studname','<U10'),('score','i8')]
	struct_arr=np.array([(r['rollno'],r['name'],r['score']) for r in result],dtype=newdtype)
	rec_arr=struct_arr.view(np.recarray)
	return rec_arr

stud='sw900b4_janitha.stud'
numpyarray=fetchtonumpy(stud)
print("RECORD ARRAY CREATED")
print("Roll no:",numpyarray.rollno)
print("Student Names:",numpyarray.studname)
print("Scores:",numpyarray.score)

obj_con.close()
