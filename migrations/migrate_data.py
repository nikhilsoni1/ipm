import pandas as pd
import os
import requests
from sqlalchemy import create_engine
from io import BytesIO


DATABASE_URI = os.getenv("DATABASE_URI")
engine = create_engine(DATABASE_URI)
column_name_map = [
    ("officename", "officename"),
    ("pincode", "pincode"),
    ("officeType", "officetype"),
    ("Deliverystatus", "deliverystatus"),
    ("divisionname", "divisionname"),
    ("regionname", "regionname"),
    ("circlename", "circlename"),
    ("Taluk", "taluk"),
    ("Districtname", "districtname"),
    ("statename", "statename"),
    ("Telephone", "telephone"),
    ("Related Suboffice", "relatedsuboffice"),
    ("Related Headoffice", "relatedheadoffice"),
    ("longitude", "longitude"),
    ("latitude", "latitude"),
]
csv_export_link = os.getenv("CSV_EXPORT_URI")
csv_response = requests.get(csv_export_link)
csv_response.raise_for_status()
column_name_map_dict = dict(column_name_map)
df = pd.read_csv(BytesIO(csv_response.content))
df = df.sort_values(by=["pincode"]).reset_index(drop=True)
dupes = df.duplicated(
    subset=[
        "officename",
        "pincode",
        "Taluk",
        "Districtname",
        "Telephone",
        "Deliverystatus",
    ],
    keep=False,
)
# These columns are part of compound PK but can have null values.
# Hence, replace null values with NA to obey SQL rules of PK != NULL
null_pk_columns = {"Taluk": "-NA-", "Districtname": "-NA-", "Telephone": "-NA-"}
df_dupes = df[dupes].reset_index(drop=True)
df_dupes = df_dupes.rename(columns=column_name_map_dict)
df_prime = df.copy()
df_prime = df_prime.fillna(null_pk_columns)
df_prime = df_prime.rename(columns=column_name_map_dict)
df_prime.to_sql("pincode", con=engine, if_exists="append", index=False)
