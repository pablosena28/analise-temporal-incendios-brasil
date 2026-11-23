"""Limpeza e reconstrução temporal da base de incêndios."""
from __future__ import annotations
import pandas as pd

MONTHS = [
    "Janeiro","Fevereiro","Março","Abril","Maio","Junho",
    "Julho","Agosto","Setembro","Outubro","Novembro","Dezembro",
]
MONTH_MAP = {month:i+1 for i,month in enumerate(MONTHS)}

def load_source(path: str) -> pd.DataFrame:
    return pd.read_csv(path, encoding="latin1")

def prepare_data(df: pd.DataFrame) -> pd.DataFrame:
    required = {"year","state","month","number","date"}
    missing = required.difference(df.columns)
    if missing:
        raise ValueError(f"Colunas ausentes: {sorted(missing)}")

    data = df.copy()
    if data[list(required)].isna().any().any():
        raise ValueError("A base contém valores ausentes.")

    duplicate_mask = (
        (data["state"] == "Alagoas")
        & (data["year"] == 2017)
        & (data["month"] == "Janeiro")
        & (data["number"] == 38.0)
    )
    idx = data.index[duplicate_mask].tolist()
    if len(idx) > 1:
        data = data.drop(index=idx[1:])

    data["month_num"] = data["month"].map(MONTH_MAP)
    if data["month_num"].isna().any():
        raise ValueError("Há mês não reconhecido.")

    data["period"] = pd.to_datetime(
        dict(year=data["year"], month=data["month_num"], day=1)
    )
    return data.sort_values(["period","state"]).reset_index(drop=True)

def full_year_sample(df: pd.DataFrame) -> pd.DataFrame:
    return df[(df["year"] >= 1998) & (df["year"] <= 2016)].copy()
