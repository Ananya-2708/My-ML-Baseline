import pytest
from src.my_project.data import load_data

def test_load_data_missing_file():
    with pytest.raises(FileNotFoundError):
        load_data("nonexistent.csv")