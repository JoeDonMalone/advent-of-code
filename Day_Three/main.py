with open("./Day_Three/input.txt") as File:
    input = File.read().strip().split("\n")

class Main():

    def __init__(self, input):
        self.input = input
    
    
    def partOne(input: str) -> int:
        finalArr = [ {0:0, 1:0} for _ in range(len(input[0]))]

        for row in input:
            for i, v in enumerate(row):
                v = int(v)
                finalArr[i][v] += 1
        print(finalArr)
        
        gam = [0] * len(finalArr)
        eps = [0]* len(finalArr)
        
        for j, v in enumerate(finalArr):
            gam[j] = "0" if v[0]>v[1] else "1"
            eps[j] = "1" if v[0]>v[1] else "0"
        
        def binToDec(bin):
            print(bin)
            dec = 0
            for i in range(len(bin)):
                digit = bin.pop()
                if digit == '1':
                    dec = dec + pow(2, i)
            return(dec)
        
        powerConsumption = binToDec(gam) * binToDec(eps)
            
        print(powerConsumption)
            
# Part 2
    def partTwo(input: str) -> int:
        arr = input
        
        def binToDec(bin):
            dec = 0
            bin = [i for i in bin]
            for i in range(len(bin)):
                digit = bin.pop()
                if digit == '1':
                    dec = dec + pow(2, i)
            return(dec)
        
        
        searchVal = 0
        rowIndex = 0
        charIndex = 0
        finalVal = []
        
        while rowIndex <= len(input[0])-1:
            left = []
            right = []
            for i, row in enumerate(input):
                left.append(row) if row[charIndex] == "0" else right.append(row)
                
            # Generator Logic
            if searchVal == 1: 
                input = right if len(right) >= len(left) else left
                
            # Scrubber Logic
            if searchVal == 0:
                input = left if len(left) <= len(right) else right
            
            rowIndex += 1
            charIndex += 1
            left = []
            right = []
            
            if len(input) == 1 and searchVal == 0:
                print("Generator Result: ", input)
                finalVal.append(binToDec(input[0]))
                rowIndex = 0
                charIndex = 0
                searchVal = 1
                input = arr
                
            if len(input) == 1 and searchVal == 1:
                print("Scrubber Result: ", input)
                finalVal.append(binToDec(input[0]))
                print(finalVal[0] * finalVal[1]) 
            
main = Main
# main.partOne(input)
main.partTwo(input)
