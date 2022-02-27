from time import perf_counter
from main import count_depth_increases, window_avg_increase

with open("./Day_One/input.txt") as File:
    input = File.read().strip().split("\n")

if __name__ == "__main__":
    start = perf_counter()
    count_depth_increases(input)
    duration = perf_counter() - start
    print(f"Duration: {duration}")
    
    start = perf_counter()
    window_avg_increase(input)
    duration = perf_counter() - start
    print(f"Duration: {duration}")