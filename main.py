import investController
import json
import utils

def main():
    result = investController.investigateTickers()
    with open('data.json', 'w') as outfile:
        json.dump(result, outfile, default=utils.convert)

if __name__ == "__main__":
    main()