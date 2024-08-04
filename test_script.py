from program import calculate_statistics

def test_mrs():
    # Original data
    original_data = [5, 6, 7, 8, 9]
    print("Original Data:", original_data)
    
    # Calculate statistics for original data
    original_mean, original_variance = calculate_statistics(original_data)
    print(f"Original Mean: {original_mean}, Original Variance: {original_variance}")
    
    # MR1: Data shift by subtracting a constant
    subtract_constant = 10
    new_data_mr1 = [x - subtract_constant for x in original_data]
    mean_mr1, variance_mr1 = calculate_statistics(new_data_mr1)
    print(f"MR1: New Data after subtraction: {new_data_mr1}")
    print(f"MR1: New Mean: {mean_mr1}, Variance: {variance_mr1}")
    print(f"MR1 Check: New Mean = Original Mean - {subtract_constant} -> {mean_mr1 == original_mean - subtract_constant}")
    print(f"MR1 Check: Variance remains the same -> {variance_mr1 == original_variance}")
    
    # MR2: Data shift by addition of a constant
    addition_constant = 3
    new_data_mr2 = [x + addition_constant for x in original_data]
    mean_mr2, variance_mr2 = calculate_statistics(new_data_mr2)
    print(f"MR2: New Data after addition: {new_data_mr2}")
    print(f"MR2: New Mean: {mean_mr2}, Variance: {variance_mr2}")
    print(f"MR2 Check: New Mean = Original Mean + {addition_constant} -> {mean_mr2 == original_mean + addition_constant}")
    print(f"MR2 Check: Variance remains the same -> {variance_mr2 == original_variance}")
    
    # MR3: Swapping the first and last elements
    new_data_mr3 = [original_data[-1]] + original_data[1:-1] + [original_data[0]]
    mean_mr3, variance_mr3 = calculate_statistics(new_data_mr3)
    print(f"MR3: Data with first and last elements swapped: {new_data_mr3}")
    print(f"MR3: Mean: {mean_mr3}, Variance: {variance_mr3}")
    print(f"MR3 Check: Mean remains unchanged -> {mean_mr3 == original_mean}")
    print(f"MR3 Check: Variance remains unchanged -> {variance_mr3 == original_variance}")
    
    # MR4: Adding and removing elements to form new subsets
    extended_data = original_data + [10, 11]
    new_data_mr4 = extended_data[:len(original_data)]
    mean_mr4, variance_mr4 = calculate_statistics(new_data_mr4)
    print(f"MR4: New Data after extension and trimming: {new_data_mr4}")
    print(f"MR4: Mean: {mean_mr4}, Variance: {variance_mr4}")
    print(f"MR4 Check: Mean and Variance should be checked manually for correctness")

# Run the test cases
test_mrs()
