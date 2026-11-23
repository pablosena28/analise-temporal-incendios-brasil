import pandas as pd
from src.data_cleaning import full_year_sample, prepare_data

def sample_data():
    return pd.DataFrame({
        "year":[2016,2017,2017],
        "state":["Acre","Alagoas","Alagoas"],
        "month":["Dezembro","Janeiro","Janeiro"],
        "number":[10.0,38.0,38.0],
        "date":["2016-01-01","2017-01-01","2017-01-01"],
    })

def test_prepare_data_reconstructs_period():
    result = prepare_data(sample_data())
    assert "period" in result.columns
    assert result.loc[0,"period"].month == 12

def test_prepare_data_removes_known_duplicate():
    assert len(prepare_data(sample_data())) == 2

def test_full_year_sample_excludes_2017():
    result = full_year_sample(prepare_data(sample_data()))
    assert result["year"].tolist() == [2016]

def test_month_number_mapping():
    assert set(prepare_data(sample_data())["month_num"]) == {1,12}

def test_prepare_data_has_no_missing_values():
    assert prepare_data(sample_data()).isna().sum().sum() == 0
