"""I load data directly to Bronze using Python"""

from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine
import os

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = Path("/Users/talia/Desktop/datawarehouse_project")

DB_URL = os.getenv("DB_URL")
if DB_URL is None:
    raise ValueError("DB_URL environment variable is not set.")

engine = create_engine(DB_URL)

SCHEMA = "bronze"

FILES = {
    "crm/cust_info.csv": "crm_cust_info",
    "crm/prd_info.csv": "crm_prd_info",
    "crm/sales_details.csv": "crm_sales_details",
    "erp/CUST_AZ12.csv": "erp_cust_az12",
    "erp/LOC_A101.csv": "erp_loc_a101",
    "erp/PX_CAT_G1V2.csv": "erp_px_cat_g1v2",
}

print("Starting Bronze load...\n")

for rel_path, table_name in FILES.items():
    file_path = DATA_DIR / rel_path
    df = pd.read_csv(file_path)

    df.to_sql(
        table_name,
        engine,
        schema=SCHEMA,
        if_exists="replace",
        index=False
    )

    print(f"[OK] Loaded {len(df)} rows into {SCHEMA}.{table_name}")

print("\nAll Bronze tables created and loaded.")
