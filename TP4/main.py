import json

def main(): 
    with open('./config.json', 'r') as f:
        data = json.load(f)
        f.close()


if __name__ == "__main__":
    main()