import openpyxl
import pandas as pd
from sqlalchemy import create_engine
import psycopg2

engine = create_engine ('postgresql+psycopg2://postgres:941iB573@localhost:5432/my_database')
cols = [2,3,5,6,7,8,9,10,11,12,13,14]
with pd.ExcelFile('SpaceNK_20181222 2.0 (1).xlsx') as xlsx:
    df = pd.read_excel(xlsx, sheet_name=0, skiprows=5, skipfooter=1, usecols = cols)
    #df.to_sql(name='my_table', con=engine, if_exists='append', index=False)
    print (df.head)