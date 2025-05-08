def shiftL(binNr, N):
    digit_list = [int(digit) for digit in str(binNr)]

    start = digit_list[N:]           
    zeros = [0] * N                   
    new_list = start + zeros

    new_bin_str = ''.join(map(str, new_list))  
    return new_bin_str


def shiftR(binNr, N):
    digit_list = [int(digit) for digit in str(binNr)]

    zeros = [0] * N  
    end = digit_list[:len(digit_list) - N]
    new_list = zeros + end

    new_bin_str = ''.join(map(str, new_list))
    return new_bin_str

def main(): 
    print(shiftR(1000111, 2))

if __name__ == "__main__":
    main()