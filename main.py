import investController
import json
import utils

def main():
    result = investController.investigateTickers()
    print(json.dumps(result, default=utils.convert))

if __name__ == "__main__":
    main()