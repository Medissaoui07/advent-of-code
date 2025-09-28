# Test with the example from the problem
def test_example():
    # Example data from the problem
    example_data = """3   4
4   3
2   5
1   3
3   9
3   3"""
    
    leftlist = []
    rightlist = []
    
    for line in example_data.strip().split('\n'):
        left, right = line.strip().split()
        leftlist.append(int(left))
        rightlist.append(int(right))
    
    # Sort the lists
    leftlist.sort()
    rightlist.sort()
    
    print(f"Left sorted:  {leftlist}")
    print(f"Right sorted: {rightlist}")
    
    # Calculate the distance 
    total_distance = 0
    for i in range(len(leftlist)):
        distance = abs(leftlist[i] - rightlist[i])
        print(f"Pair {i+1}: {leftlist[i]} and {rightlist[i]}, distance = {distance}")
        total_distance += distance
    
    print(f"Total distance: {total_distance}")
    return total_distance

if __name__ == "__main__":
    test_example()
