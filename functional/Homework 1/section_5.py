def search_list(L):
    index = {
                "list":0,
                "int":0,
                "float":0,
                "str":0,
                "tuple":0
            }

    for i in L:
        if isinstance(i, list):
            index["list"] += 1
        elif isinstance(i, int):
            index["int"] += 1
        elif isinstance(i, float):
            index["float"] += 1
        elif isinstance(i, str):
            index["str"] += 1
        elif isinstance(i, tuple):
            index["tuple"] += 1

    print(index)

def main():
    list = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]
    search_list(list)

if  __name__ == '__main__':
    main()
