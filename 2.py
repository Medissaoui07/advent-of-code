#Advent of Code 2024 - Day 2 
#Work done by Mohamed Issaoui for the application of wandercraft intership


def solve_problem_part1():
    with open("input.txt", "r") as file:
        data = file.read()
        nb_safe=0   
    for line in data.strip().split('\n'):
        levels = list(map(int, line.split()))  
        #see if the levels are safe 
        is_safe = True
        
        diff = 0 

        is_decreasing = all(levels[i] > levels[i + 1] for i in range(len(levels) - 1))
        is_increasing = all(levels[i] < levels[i + 1] for i in range(len(levels) - 1)) 
        if not (is_decreasing or is_increasing):
            is_safe = False
        if is_safe:
            if is_safe:
                for i in range (len(levels)-1):
                    diff = abs(levels[i] - levels[i+1])
                    if diff > 3 or diff < 1:
                        is_safe=False
                        break
                if is_safe:
                    nb_safe+=1    
    return nb_safe    
            
def solve_problem_part2():
    with open("input.txt", "r") as file:
        data = file.read()
        nb_safe=0   
    for line in data.strip().split('\n'):
        levels = list(map(int, line.split())) 
        if is_safe(levels):
            nb_safe+=1
            continue 
        safe = False 
        for i in range(len(levels)):
            new_levels=levels[:i] + levels[i+1:]
            if is_safe(new_levels):
                safe=True
                break
        if safe :
            nb_safe+=1
    
    return nb_safe



def is_safe(levels):
    is_decreasing = all(levels[i] > levels[i + 1] for i in range(len(levels) - 1))
    is_increasing = all(levels[i] < levels[i + 1] for i in range(len(levels) - 1)) 
    if not (is_decreasing or is_increasing):
        return False
    for i in range(len(levels) - 1):
        diff = abs(levels[i] - levels[i + 1])
        if diff > 3 or diff < 1:
            return False
    
    return True

def main():
    try:
        #result = solve_problem_part1()
        result = solve_problem_part2()
        print(f"The result is: {result}")
    except Exception as e:
        print(f"An error occurred: {e}")    

if __name__ == "__main__":
    main()