
import pandas as pd
import numpy as np

# -----------------------------
# LOAD DATASET (Google Drive Path)
# -----------------------------
DATA_PATH = '/content/drive/MyDrive/FraudDetection/creditcard.csv'

df = pd.read_csv(DATA_PATH)

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
    df_copy = df.copy()

    # Normalize Time & Amount
    df_copy['norm_time'] = (df_copy['Time'] - df_copy['Time'].mean()) / df_copy['Time'].std()
    df_copy['norm_amount'] = (df_copy['Amount'] - df_copy['Amount'].mean()) / df_copy['Amount'].std()

    input_time_norm = (time_value - df_copy['Time'].mean()) / df_copy['Time'].std()
    input_amount_norm = (amount - df_copy['Amount'].mean()) / df_copy['Amount'].std()

    # Distance calculation
    df_copy['distance'] = (
        abs(df_copy['norm_time'] - input_time_norm) +
        abs(df_copy['norm_amount'] - input_amount_norm)
    )

    nearest_row = df_copy.loc[df_copy['distance'].idxmin()]

    return nearest_row

# -----------------------------
# GET PRELOADED TRANSACTION (A2)
# -----------------------------
def get_preloaded_transaction(txn_id):
    if txn_id not in PRELOADED_MAP:
        return None
    return df.iloc[PRELOADED_MAP[txn_id]]
