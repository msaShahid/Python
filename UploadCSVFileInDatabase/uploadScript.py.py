import pandas as pd
from sqlalchemy import create_engine
from tqdm import tqdm
# pip install pymysql

connection = create_engine('mysql+pymysql://root:@localhost/pythonsql')

files = ['artist','canvas_size','image_link','museum_hours','museum','product_size','subject','work']

try:
    for file in tqdm(files,desc="Processing files"):
        dataFrame = pd.read_csv(f'E:/pythonSQL/sqlTable/{file}.csv')
        dataFrame.to_sql(name=file,con = connection, if_exists="replace",index=False)
        #print(f"Data inserted from {file}.csv successfully !")
except Exception as e:
    print("An error accoured : ", e)
    
    