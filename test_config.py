
from config import load_config

def test_load_config():
    assert load_config("rate: 3") == {"rate": 3}
