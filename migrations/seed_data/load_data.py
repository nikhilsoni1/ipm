import pandas as pd
import os
from sqlalchemy import create_engine

DATABASE_URI = os.getenv("DATABASE_URI")
engine = create_engine(DATABASE_URI)
root = os.path.dirname(os.path.realpath(__file__))
os.chdir(root)
data_path = "indian_pincodes_proc.csv"
if not os.path.exists(data_path):
    print("ERROR: DATA NOT FOUND")
else:
    pass
df = pd.read_csv(data_path)
df.to_sql("pincode", con=engine, if_exists="append", index=False)
