# Advent of Code 2024 - Day 1
# Work done by Mohamed Issaoui for the application of wandercraft intership 



def solve_problem_part1(): 
    leftlist = []
    rightlist = []
    with open("day1/input.txt", "r") as file:
        for line in file:
            left, right = line.strip().split()
            leftlist.append(int(left))
            rightlist.append(int(right))
    #sort the lists
    leftlist.sort()
    rightlist.sort()

    #calculate the distance 
    total_distance = 0
    for i in range(len(leftlist)):
        distance = abs(int(leftlist[i]) - int(rightlist[i]))
        total_distance += distance

    #print(total_distance)  
    return total_distance   

def solve_problem_part2():
    
    leftlist = []
    rightlist = []
    with open("day1/input.txt", "r") as file:
        for line in file:
            left, right = line.strip().split()
            leftlist.append(int(left))
            rightlist.append(int(right))

        #calculate similarity score
        similarity_score = 0
        sim=0
        for i in range(len(leftlist)):
            for j in range(len(rightlist)):
                if leftlist[i] == rightlist[j]:
                    sim+=1
                similarity_score += leftlist[i]*sim
                sim=0
                
 
    return similarity_score

    
def main(): 
    try:
        result = solve_problem_part1()
        print(f"The result is: {result}")
        result2 = solve_problem_part2()
        print(f"The result is: {result2}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()