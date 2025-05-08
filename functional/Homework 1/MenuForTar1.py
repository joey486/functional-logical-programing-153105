#
#  Example program for Targil 1
#
import math
from myboolfuncs import *
#

PI = math.pi

# section 1
def triangle_numbers(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

def trianlge_checker():
    a = float(input("Enter 1st number: ")) 
    b = float(input("Enter 2nd number: "))
    c = float(input("Enter 3rd number: "))

    if triangle_numbers(a, b, c):
        print("correct triangle sides lengths")
    else:
        print("not correct triangle sides lengths")

# section 2
# Area calculation program  
def rectangleArea(w, h):
     return w*h
#
def circleArea(r):
     return PI * r**2
#
def triangleArea(b,h):
     return 0.5*b*h
#
def squareArea(w):
     return w**2
#
def sphereVolume(r):
     return 4/3*PI*r**3
#
def coneVolume(r,h):
     return PI*r**2*h/3
#
def squarPyramidVolume(base,h):
     return squareArea(base)*h/3
#
# printing the menu options
def prtMenu(shapes):
   for i in range(len(shapes)):
      print (i+1, shapes[i])
   return


# section 3
def function3V11():
    a = float(input("Enter 1st number: ")) 
    b = float(input("Enter 2nd number: "))
    c = float(input("Enter 3rd number: "))
    d = float(input("Enter 4th number: "))
    arr = [a, b, c, d]
    arr.sort()
    print(f"middle numbers are: {arr[1]}, {arr[2]}")
#
def function3V12():
    a = float(input("Enter 1st number: ")) 
    b = float(input("Enter 2nd number: "))
    c = float(input("Enter 3rd number: "))
    d = float(input("Enter 4th number: "))
    arr = [a, b, c, d]
    # bubble sort:
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(f"middle numbers are: {arr[1]}, {arr[2]}")

def function3V21(arr):
        arr.sort()
        n = int(len(arr)/2)
        print(f"middle numbers are: {arr[n]}, {arr[n+1]}")

def function3V22(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    m = int(len(arr)/2)
    print(f"middle numbers are: {arr[m]}, {arr[m+1]}")

def function3V3(arr):
    temparr = []
    for i in arr:
        if isinstance(i, (int, float)):
            temparr.append(i)
    function3V21(temparr)

# section 4   
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

def shiftCL(binNr, N):
    digit_list = [int(digit) for digit in str(binNr)]
    start = digit_list[N:] 
    end = digit_list[:N]    
    new_list = start + end

    new_bin_str = ''.join(map(str, new_list))    
    return new_bin_str

def shiftCR(binNr, N):
    digit_list = [int(digit) for digit in str(binNr)]
    end = digit_list[len(digit_list) - N:] # +1 ?
    start = digit_list[0:len(digit_list) - N]
    new_list = end + start

    new_bin_str = ''.join(map(str, new_list))
    return new_bin_str

      
#
# main program
#
def main():   
     print ("Welcome to the Area calculation program")
     print ("---------------------------------------\n")  
     # Print out the menu
     shapes = ("Rectangle", "Circle", "Triangle", "Square", "SphereVolume", "ConeVolume", "SquarPyramidVolume")
     while True:
          print ("\nPlease select a shape (press 0 to quit):")
          prtMenu(shapes) 
          # Get the user's choice: 
          shape = input("> ")
          # Calculate the area: 
          if shape == "1":
               height = getNumber("Please enter the height: ")    
               width  = getNumber("Please enter the width: ")
               area = rectangleArea(width, height)
               print ("The area is", area)
               continue
          elif shape == "2":
               radius = getNumber("Please enter the radius: ")
               area   = circleArea(radius)
               print ("The area is", area)
               continue
          elif shape == "3":
               base = getNumber("Please enter the base: ")
               height = getNumber("Please enter the height: ")
               area = triangleArea(base, height)
               print ("The area is", area)
               continue
          elif shape == "4":
               side = getNumber("Please enter the side: ")
               area = squareArea(side)
               print ("The area is", area)
               continue
          elif shape == "5":
               radius = getNumber("Please enter the radius: ")
               volume = sphereVolume(radius)
               print ("The volume is", volume)
               continue
          elif shape == "6":
               radius = getNumber("Please enter the radius: ")
               height = getNumber("Please enter the height: ")
               volume = coneVolume(radius, height)
               print ("The volume is", volume)
               continue
          elif shape == "7":
               base = getNumber("Please enter the base: ")
               height = getNumber("Please enter the height: ")
               volume = squarPyramidVolume(base, height)
               print ("The volume is", volume)
               continue
          elif shape == "0":
               print ("Bye!")
               break
          else:     
               print ("Invalid shape")

if __name__ == "__main__":
    main()
