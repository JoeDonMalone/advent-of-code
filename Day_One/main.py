with open("./Day_One/input.txt") as File:
    input = File.read().strip().split("\n")

# Part 1
def count_depth_increases(input:str) -> int:
    prev_read = 0
    depth_increases = 0

    for i, v in enumerate(input):
        if int(v) > prev_read and i != 0:
            # print('Prev_read:', prev_read)
            # print('current_read:', v)
            depth_increases += 1
        prev_read = int(v)
    return(depth_increases)

# Part 2
def window_avg_increase(input:str) -> int:
    prev_reads_sum = 0
    depth_increases = 0
    size_reqs = 3
    window_size = 0

    for i, v in enumerate(input):
        current_window_sum = 0
        if i != len(input) - 2:
            while window_size < size_reqs:
                # print(f"current_window_sum: {current_window_sum} Window_size: {window_size}, current_index: {i}")
                current_window_sum += int(input[i+window_size])
                window_size += 1
        else:
            break
        if i != 0:
            if current_window_sum > prev_reads_sum:
                depth_increases += 1
        prev_reads_sum = current_window_sum
        # print(prev_reads_sum, "Depth Increases: ", depth_increases)

        window_size = 0
    return(depth_increases)

print(count_depth_increases(input))
print(window_avg_increase(input))
