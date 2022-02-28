from time import perf_counter
from main import Main

with open("./Day_Two/input.txt") as File:
    input = File.read().strip().split("\n")
main = Main
if __name__ == "__main__":
    start = perf_counter()
    main.partOne(input)
    duration = perf_counter() - start
    print(f"Duration: {duration}")
    
    start = perf_counter()
    main.partTwo(input)
    duration = perf_counter() - start
    print(f"Duration: {duration}")