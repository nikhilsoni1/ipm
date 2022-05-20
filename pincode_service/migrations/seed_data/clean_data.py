import pandas as pd
import os
import requests

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
root = os.path.dirname(os.path.realpath(__file__))
os.chdir(root)
raw_data_csv_path = "indian_pincodes_raw.csv"
dupes_data_csv_path = "indian_pincodes_dupes.csv"
proc_data_csv_path = "indian_pincodes_proc.csv"
csv_export_link = "https://drive.google.com/u/0/uc?id=1M58ZSEBqmLnH0rRCEN5uZfj0FemN6pw3&export=download"

csv_response = requests.get(csv_export_link)
csv_response.raise_for_status()

with open(raw_data_csv_path, "wb") as stream:
    stream.write(csv_response.content)
column_name_map_dict = dict(column_name_map)
df = pd.read_csv(raw_data_csv_path)
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
if df_dupes.shape[0] > 0:
    df_dupes.to_csv(dupes_data_csv_path, index=False)
df_prime.to_csv(proc_data_csv_path, index=False)
