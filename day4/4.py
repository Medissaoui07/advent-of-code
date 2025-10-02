# Work done by Mohamed Issaoui for the application of wandercraft internship
# Advent of Code 2023 - Day 4

def solve_problem_part1():
    with open("day4/input.txt" , "r") as file : 
        data= file.read().strip().split('\n')
        count = 0 
     
        matrix = [list(line) for line in data]
        rows , cols = len(matrix) , len(matrix[0])
        directions = [
        (0, 1),   
        (0, -1),  
        (1, 0),   
        (-1, 0),  
        (1, 1),   
        (1, -1),  
        (-1, 1),  
        (-1, -1)  
    ]
        def search_word(r, c, dr, dc):
            target = "XMAS"
            row , col = r , c  
            for i in range(4):
                r , c = row + i * dr , col + i * dc
                if r < 0 or r >= rows or c < 0 or c >= cols:
                    return False
                if matrix[r][c] != target[i]:
                    return False
            return True
            

        for r in range(rows):
            for c in range(cols):
                current = matrix[r][c]
                if current == 'X' : 
                    for dr, dc in directions:
                        if search_word( r, c, dr, dc):
                            count += 1
                            
        return count


def solve_problem_part2(): 
    with open("day4/input.txt", "r") as file: 
        data = file.read().strip().split('\n')
        
    matrix = [list(line) for line in data]
    rows, cols = len(matrix), len(matrix[0])
    count = 0
    
    def check_x(r, c):
        if r - 1 < 0 or r + 1 >= rows or c - 1 < 0 or c + 1 >= cols:
            return False
        
        if matrix[r][c] != 'A':
            return False 
        top_left = matrix[r-1][c-1]
        top_right = matrix[r-1][c+1] 
        bottom_left = matrix[r+1][c-1]
        bottom_right = matrix[r+1][c+1]  
        diag1 = top_left + 'A' + bottom_right
        diag2 = top_right + 'A' + bottom_left
        valid_words = ["MAS", "SAM"]
        
        return diag1 in valid_words and diag2 in valid_words
    
    for r in range(1, rows - 1):  
        for c in range(1, cols - 1):
            if check_x(r, c):
                count += 1
                
    return count


def main(): 
    try : 
        result = solve_problem_part1()
        print(f"Result of part 1 : {result}")
        result = solve_problem_part2()
        print(f"Result of part 2 : {result}")
    except FileNotFoundError:
        print("Error: 'input.txt' file not found.")

if __name__ == "__main__":
    main()