# Advent of Code 2023 - Day 3
# Work done by Mohamed Issaoui for the application of wandercraft internship

import re 
def solve_problem_part1():
    with open("input.txt" , "r") as file : 
        corruptet_data= file.read()

    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    matches = re.findall(pattern, corruptet_data)
    #print(matches)
    result = 0 
    for a,b in matches:
        
        result += int(a) * int(b)
    return result

def solve_problem_part2():
    with open("input.txt" , "r") as file : 
        corruptet_data= file.read()

        
    pattern = r'(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\))'
    matches = re.findall(pattern, corruptet_data)
    #print(matches)
    result = 0 
    enable = True
    for match in matches : 
        instruction = match[0]
        if instruction == "do()" :
            enable = True
        elif instruction == "don't()":
            enable = False
        elif instruction.startswith("mul(") and enable   :
            a = int(match[1])
            b = int(match[2])
            result += a * b
    return result


   

def main() :
    try : 
        #result = solve_problem_part1()
        
        #print(f"Result of part 1 : {result}")
        result = solve_problem_part2()
        print(f"Result of part 2 : {result}")
    except FileNotFoundError:
        print("Error: 'input.txt' file not found.")
             
if __name__ == "__main__":
    main()

