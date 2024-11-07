def hamming_distance(str1, str2):
    # Returns the Hamming distance between two strings
    return sum(1 for a, b in zip(str1, str2) if a != b)

def process_test_case(binary_str, A, B):
    # Check if binary_str is a valid binary string
    if not all(c in '01' for c in binary_str):
        return "INVALID"
    
    # Count number of 0s and 1s in the string
    count_0 = binary_str.count('0')
    count_1 = binary_str.count('1')
    
    # Calculate the cost for the original string
    original_cost = 0
    for i in range(len(binary_str) - 1):
        if binary_str[i:i+2] == "01":
            original_cost += A
        elif binary_str[i:i+2] == "10":
            original_cost += B
    
    # The best arrangement is either "000...111" or "111...000"
    rearranged_str1 = '0' * count_0 + '1' * count_1  # All 0's followed by all 1's
    rearranged_str2 = '1' * count_1 + '0' * count_0  # All 1's followed by all 0's
    
    # Calculate the cost for the rearranged strings
    def calculate_cost(rearranged_str):
        cost = 0
        for i in range(len(rearranged_str) - 1):
            if rearranged_str[i:i+2] == "01":
                cost += A
            elif rearranged_str[i:i+2] == "10":
                cost += B
        return cost
    
    cost1 = calculate_cost(rearranged_str1)
    cost2 = calculate_cost(rearranged_str2)
    
    # We choose the rearranged string with the minimal cost
    # If both have the same cost, choose the one with the minimal Hamming distance
    if cost1 < cost2:
        rearranged_str = rearranged_str1
    elif cost2 < cost1:
        rearranged_str = rearranged_str2
    else:
        # If costs are equal, choose the one with the minimal Hamming distance
        dist1 = hamming_distance(binary_str, rearranged_str1)
        dist2 = hamming_distance(binary_str, rearranged_str2)
        rearranged_str = rearranged_str1 if dist1 <= dist2 else rearranged_str2
    
    # Return the Hamming distance between original and chosen rearranged string
    return hamming_distance(binary_str, rearranged_str)

def main():
    # Input number of test cases
    T = int(input())
    
    for _ in range(T):
        # Read binary string and costs
        binary_str = input().strip()
        A, B = map(int, input().split())
        
        # Process each test case
        result = process_test_case(binary_str, A, B)
        print(result)

if __name__ == "__main__":
    main()
