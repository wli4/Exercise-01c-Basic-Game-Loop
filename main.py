#!/usr/bin/env python3
import sys,os,json
assert sys.version_info >= (3,8), "This script requires at least Python 3.8"

def load(l):
    f = open(os.path.join(sys.path[0], l))
    data=f.read()
    return json.loads(data)
    
    







def main():
    game_desc = load("adventure.json")
    print(game_desc)


if __name__ == "__main__":
    main()