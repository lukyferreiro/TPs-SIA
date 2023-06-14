import json
from src.utils import DataConfig

def main(): 
    with open('./config.json', 'r') as f:
        data_config = json.load(f)

    config = DataConfig(data_config)


if __name__ == "__main__":
    main()