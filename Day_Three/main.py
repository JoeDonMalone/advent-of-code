# Part 1
with open("./Day_Three/input.txt") as File:
    input = File.read().strip().split("\n")

class Main():

    def __init__(self, input):
        self.input = input
    
        
    def partOne(input: str) -> int:
        
        # finalArr = [{"0":0, "1":0}] * len(input[0])
        finalArr = [
                    {0: 0, 1: 0}, 
                    {0: 0, 1: 0}, 
                    {0: 0, 1: 0}, 
                    {0: 0, 1: 0}, 
                    {0: 0, 1: 0}, 
                    {0: 0, 1: 0}, 
                    {0: 0, 1: 0}, 
                    {0: 0, 1: 0}, 
                    {0: 0, 1: 0}, 
                    {0: 0, 1: 0}, 
                    {0: 0, 1: 0}, 
                    {0: 0, 1: 0}
                    ]
        gam = [0] * len(finalArr)
        eps = [0]* len(finalArr)
        
        for row in input:
            for i, v in enumerate(row):
                v = int(v)
                # print('FinalArr vs bit:', finalArr[i][v])
                finalArr[i][v] += 1
        
        print(finalArr)
        
        for j, v in enumerate(finalArr):
            print(j, v[1])
            if v[0] > v[1]:
                gam[j] = "0"
                eps[j] = "1"
            else: 
                gam[j] = "1"
                eps[j] = "0"
            
        print("".join(gam))
        print("".join(eps))
        
        def binToDec(bin):
            dec = 0
            for i in range(len(bin)):
                digit = bin.pop()
                if digit == '1':
                    dec = dec + pow(2, i)
            return(dec)
        
        powerConsumption = lambda x,y: binToDec(x) * binToDec(y)
            
        print(powerConsumption(gam, eps))
            
# Part 2
    def partTwo(input: str) -> int:
        pass

main = Main
main.partOne(input)
main.partTwo(input)
