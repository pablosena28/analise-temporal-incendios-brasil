"""Análise temporal e sazonal dos registros de incêndio."""
from pathlib import Path
from src.data_cleaning import MONTHS, full_year_sample, load_source, prepare_data

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "source" / "Dados_Indendio.csv"

def main() -> None:
    raw = load_source(str(SOURCE))
    df = prepare_data(raw)
    full = full_year_sample(df)

    annual = full.groupby("year")["number"].sum()
    monthly = full.groupby("month")["number"].sum().reindex(MONTHS)

    print("=== QUALIDADE DA BASE ===")
    print(f"Linhas originais: {len(raw)}")
    print(f"Linhas após limpeza: {len(df)}")
    print(f"Rótulos territoriais: {df['state'].nunique()}")
    print(f"Período reconstruído: {df['period'].min().date()} a {df['period'].max().date()}")
    print("2017 é parcial: apenas janeiro a novembro.")

    print("\n=== ANÁLISE ANUAL — 1998 A 2016 ===")
    print(f"Ano com maior soma: {annual.idxmax()} ({annual.max():.3f})")
    print(f"Ano com menor soma: {annual.idxmin()} ({annual.min():.3f})")
    print(f"1998: {annual.loc[1998]:.3f}")
    print(f"2016: {annual.loc[2016]:.3f}")

    print("\n=== SAZONALIDADE ===")
    print(monthly.sort_values(ascending=False).round(3).to_string())

if __name__ == "__main__":
    main()
