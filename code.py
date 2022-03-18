import pandas as pd

import sqlite3
from sqlalchemy import create_engine

file="OnlineRetail.xlsx"
output="output.xlsx"
"""
create database in memory only: access it , get rid of it  
"""
engine= create_engine('sqlite://', echo=False )
# ecel to df 
df=pd.read_excel(file)
# df to sql 
df.to_sql("orders", engine, if_exists="replace", index=False)
#transactions that took place in France
results=engine.execute("select * from orders where Country='France'")

#sql to excel
final=pd.DataFrame(results, columns=df.columns)
final.to_excel(output, index=False)
