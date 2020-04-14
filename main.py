import investController
import utils
import simplejson

def main():
    result = investController.investigateTickers()
    with open('data.json', 'w') as outfile:
        simplejson.dump(result, outfile, default=utils.convert, sort_keys=True, ignore_nan=True)

if __name__ == "__main__":
    main()