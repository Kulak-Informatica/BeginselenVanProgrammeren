# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 12:48:10 2020

@author: Thibaut
"""

"""
def collatz(num):
    if num%2 == 0:
        num/=2
    else:
        num=(3*num)+1
    return num


def main():
    import time
    Dtime = 0
    if input("Individuele berekening? (j/n): \n> ") == "j":
        i = int(input('> '))
        
        start = time.time()
        print(start)
        
        num = collatz(i)
        step = 1
        maxNum = num
        countNum = i + num
        while num != 1:
            num = collatz(num)
            step +=1
            countNum += num
            if num>maxNum:
                maxNum = num
        
        Dtime = time.time() - start
        print(f"Aantal stappen: {step}")
        print(f"Maximum: {maxNum}")
        print(f"Gemiddelde: {round(countNum/(step+1), 2)}")
        print()
        
        
    else:
        start = time.time()
        numRange = input("Range of numbers (space between): \n> ").split(" ")
        while int(numRange[0]) <= 0:
            print("Invalid range!")
            numRange = input("Range of numbers (space between): \n> ").split(" ")
        
        lijst = []
        for i in range(int(numRange[0]), int(numRange[1]) + 1):
            line = []
            num = collatz(i)
            step = 1
            maxNum = num
            countNum = i + num
            
            while num != 1:
                num = collatz(num)
                step +=1
                countNum += num
                
                if num>maxNum:
                    maxNum = num
            
            percentage = (i*100)/int(numRange[1])
            if percentage % 10 == 0:
                print(f"Calculation: {round(percentage, 2)}%")
            lijst += [[step, int(maxNum), round(countNum/(step+1), 2)]]
        
        Dtime = time.time() - start
        num = int(input("Geef getal op (0 => exit): \n> "))
        lengte = len(lijst)
        
        while num!=0 and num<lengte:
            print(f"Aantal stappen: {lijst[num-1][0]}")
            print(f"Maximum: {lijst[num-1][1]}")
            print(f"Gemiddelde: {lijst[num-1][2]}")
            print()
            num = int(input("> "))
        
    print(f"Calculation finished in {Dtime} seconds.")

main()
"""



def collatz(num):
    if num%2 == 0:
        num/=2
    else:
        num=(3*num)+1
    return int(num)


def main():
    import time
    Dtime = 0
    tfCalc = input("Tussenresultaten zien? (j/n) \n> ")
    num = int(input("Geef getal op (0 => exit): \n> "))
    while num < 0:
        num = int(input("Geef GELDIG getal op (0 => exit): \n> "))
    
    while num != 0:
        start = time.time()
        calcSet = [num]

        step = 0
        maxNum = num
        countNum = num
        
        while num != 1:
            num = collatz(num)
            step +=1
            countNum += num
            
            if num>maxNum:
                maxNum = num
                
            calcSet += [num]
        Dtime = time.time() - start
        
        print(f"Aantal stappen: {step}")
        print(f"Maximum: {maxNum}")
        print(f"Gemiddelde: {round(countNum/(step+1), 2)}")
        if tfCalc == "j":
            print(f"Tussenresultaten: {calcSet}")
        print(f"Calculation finished in {Dtime} seconds.")
            
        print()
        num = int(input("Geef getal op (0 => exit): \n> "))
        while num < 0:
            num = int(input("Geef GELDIG getal op (0 => exit): \n> "))      
    

main()