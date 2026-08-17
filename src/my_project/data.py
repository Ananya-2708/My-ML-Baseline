import pandas as pd
from pathlib import Path

def load_data(path: str) -> pd.DataFrame:
    if not Path(path).exists():
        raise FileNotFoundError(f"Data not found: {path}")
    return pd.read_csv(path)