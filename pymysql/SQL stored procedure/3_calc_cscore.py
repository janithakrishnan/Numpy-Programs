#!/usr/bin/env python3

#CREATING SQL TABLE FOR STORING RESULTS OF PROCEDURE 'cscore'
import pymysql as my
obj_con=my.connect(host='localhost',user='sw900b4_janitha',passwd='janitha123',database='sw900b4_janitha')
obj_cur=obj_con.cursor()
qstr1="""
select name from studsm
"""
obj_cur.execute(qstr1)
res=obj_cur.fetchall()
print("Printing results of select query :name from studsm----\n",res)
names=list(set([r[0] for r in res]))
print("Printing student names---\n",names)

qstr2="""
create table studcscore(name char(20),cscore int)
"""
obj_cur.execute('drop table if exists studcscore')
obj_cur.execute(qstr2)
print("New table studcscore created")
obj_con.commit()


for n in names:
	obj_cur.callproc('cscore',(n,))
	result=obj_cur.fetchall()
	tup=str(result[0])
	qstr='insert into studcscore values'+tup
	obj_cur.execute(qstr)
	obj_con.commit()
print("Printing contents of new table studcscore")
obj_cur.execute('select * from studcscore')
print(obj_cur.fetchall())
obj_con.close()

