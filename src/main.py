import os
from getnwjs import get_nwjs
from convert import convert

def main():
    version = "0.78.0"
    gamepath = "oe" ####### TO BE SET BY GUI LATER
    #get_nwjs(version)
    convert(gamepath)

if __name__ == "__main__":
    main()