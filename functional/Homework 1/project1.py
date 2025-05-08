from MenuForTar1 import *
from section_5 import *
from section_6 import *

def main():
    lfuncs = [trianlge_checker, rectangleArea, circleArea, triangleArea, squareArea,
              sphereVolume, coneVolume, squarPyramidVolume, function3V11, function3V12,
              function3V21, function3V22, function3V3, 
              shiftL, shiftR, shiftCL, shiftCR, search_list, function6] # function names 
    lstrs = ["exit", "triangles", "rectangle area", "circle area", "triangle area", "square area",
             "sphere volume", "cone volume", "square pyramid", "middle numbers 1", "middle numbers 1",
             "middle numbers 2", "middle numbers 2", "middle numbers 3", "shift left", "shift right",
             "shift circular left", "shift circular right", "search a list for types", "randomness"] #description of functions 
    
    while True:
        print("Your choices:")
        for i, s in enumerate(lstrs):
            print(f"{i} : {s}")
        c = int(input("Please enter your choice: "))
        if c == 0:
            break
        elif 1 <= c <= 7:
            lfuncs[c-1]()
        elif 8 <= c <= 10:
            lfuncs[c-1]
        else:
            print("Error: Invalid choice")

if __name__ == "__main__":
    main()
