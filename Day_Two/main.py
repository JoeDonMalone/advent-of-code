# Part 1
class Main():

    def __init__(self, input):
        self.input = input
    
    def partOne(input: str) -> int:
        
        map = {
            "depth": 0,
            "hPos": 0,
            "up": lambda x: map["depth"] - x,
            "down": lambda x: map["depth"] + x,
            "forward": lambda x: map["hPos"] + x
        }
        
        for i, v in enumerate(input):
            move, distance = v.split(" ")
            if move == "up":
                map["depth"] = map["up"](int(distance))
            elif move == "down":
                map["depth"] = map["down"](int(distance))
            else:
                map["hPos"] = map["forward"](int(distance))
        
        finalMove = map["depth"] * map["hPos"]
        print(finalMove)
# Part 2

    def partTwo(input: str) -> int:
            
            mapping = {
                "depth": 0,
                "hPos": 0,
                "aim": 0,
                "up": lambda x: mapping["aim"] - x,
                "down": lambda x: mapping["aim"] + x,
                "forward": lambda x: mapping["hPos"] + x,
            }
            
            for i, v in enumerate(input):
                move, distance = v.split(" ")
                distance = int(distance)
                
                if move == "up":
                    mapping["aim"] = mapping["up"](distance)
                elif move == "down":
                    mapping["aim"] = mapping["down"](distance)
                elif move == "forward" and mapping["aim"]:
                    mapping["hPos"] = mapping["forward"](distance)
                    mapping["depth"] = mapping["depth"] + (distance * mapping["aim"])
                else:
                    mapping["hPos"] = mapping["forward"](distance)
            
            finalMove = mapping["depth"] * mapping["hPos"]
            print(finalMove)

with open("./Day_Two/input.txt") as File:
    input = File.read().strip().split("\n")
    
main = Main
main.partOne(input)
main.partTwo(input)