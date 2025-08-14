#!/usr/bin/env python3

#CREATING STORED PROCEDURE 'cscore' FOR CALCULATING CSCORE OF STUDENT FROM SQL TABLE studsm
#Constraint: if score of retrieved semester<50 then cscore=0

import pymysql as my
obj_con=my.connect(host='localhost',user='sw900b4_janitha',passwd='janitha123',database='sw900b4_janitha')
obj_cur=obj_con.cursor()
qsp="""
create procedure cscore(pname char(20))
begin
declare v_score int;
declare v_cscore int default 0;
declare done int default 0;
declare studcur CURSOR FOR SELECT score from studsm where name=pname;
declare continue handler for not found set done=1;
open studcur;
studloop:LOOP
fetch studcur into v_score;
if done=1
then
leave studloop;
end if;
if v_score<50
then
set v_cscore=0;
else
set v_cscore=v_cscore+v_score;
end if;
end loop;
close studcur;
select pname,v_cscore;
end
"""
obj_cur.execute('drop procedure if exists cscore')
obj_cur.execute(qsp)
obj_con.commit()
print("Printing cscore of student tom")
obj_cur.callproc('cscore',('tom',))
res=obj_cur.fetchall()
print(res)
obj_cur.close()
obj_con.close()
