import pandas as pd
import numpy as np
import os

# -----------------------------
# LOAD DATASET (ZIP FILE IN SAME FOLDER)
# -----------------------------
BASE_DIR = os.path.dirname(__file__)
DATA_PATH = os.path.join(BASE_DIR, "creditcard.csv.zip")

# Cache the DataFrame in memory
_df_cache = None

def get_dataframe():
    global _df_cache
    if _df_cache is None:
        _df_cache = pd.read_csv(DATA_PATH, compression='zip')
    return _df_cache

# -----------------------------
# PRELOADED TRANSACTION MAPPING (A2)
# -----------------------------
PRELOADED_MAP = {
    "TXN_001": 10,
    "TXN_002": 25,
    "TXN_003": 120,
    "TXN_004": 305,
    "TXN_005": 450
}

# -----------------------------
# TIME MAPPING (UI → NUMERIC)
# -----------------------------
def map_time(period):
    mapping = {
        "morning": 20000,
        "afternoon": 40000,
        "evening": 60000,
        "night": 80000
    }
    return mapping.get(period.lower(), 40000)

# -----------------------------
# FIND NEAREST TRANSACTION (A1)
# -----------------------------
def find_nearest_transaction(time_value, amount):
    df = get_dataframe().copy()

    # Normalize Time & Amount
    df['norm_time'] = (df['Time'] - df['Time'].mean()) / df['Time'].std()
    df['norm_amount'] = (df['Amount'] - df['Amount'].mean()) / df['Amount'].std()

    input_time_norm = (time_value - df['Time'].mean()) / df['Time'].std()
    input_amount_norm = (amount - df['Amount'].mean()) / df['Amount'].std()

    # Distance calculation
    df['distance'] = (
        abs(df['norm_time'] - input_time_norm) +
        abs(df['norm_amount'] - input_amount_norm)
    )

    nearest_row = df.loc[df['distance'].idxmin()]

    return nearest_row

# -----------------------------
# GET PRELOADED TRANSACTION (A2)
# -----------------------------
def get_preloaded_transaction(txn_id):
    df = get_dataframe()
    if txn_id not in PRELOADED_MAP:
        return None
    return df.iloc[PRELOADED_MAP[txn_id]]
