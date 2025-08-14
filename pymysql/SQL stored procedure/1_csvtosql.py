#!/usr/bin/env python3

#INSERTING CONTENTS OF CSV FILE studsm.csv TO NEW SQL TABLE studsm
import sqlalchemy as sa
ae=sa.create_engine("mysql+pymysql://sw900b4_janitha:janitha123@localhost/sw900b4_janitha")
import pandas as pd
sf1=pd.read_csv('studsm.csv')
print(sf1)
sf1.to_sql("studsm",ae)
print("TABLE studsm CREATED")
