with open("./Day_One/input.txt") as File:
   input = File.read().strip().split("\n")

# Part 1
def count_depth_increases(input):
    prev_read = 0
    depth_increases = 0
        
    for i,v in enumerate(input):
        if int(v) > prev_read and i != 0:
            print('Prev_read:', prev_read)
            print('current_read:', v)
            depth_increases += 1
            print('current_score:', depth_increases)
        prev_read = int(v)
    print(depth_increases)
    
def window_avg_increase(input):
    pass

count_depth_increases(input)