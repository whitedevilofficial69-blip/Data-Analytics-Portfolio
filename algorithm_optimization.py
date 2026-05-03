import time

# Function to search a number in a list
def search_number(data_list, target):
    start_time = time.time()
    
    # Built-in optimized search
    if target in data_list:
        found = True
    else:
        found = False
        
    end_time = time.time()
    execution_time = end_time - start_time
    
    return found, execution_time

# Create a huge dataset of 1 Million numbers
huge_dataset = list(range(1, 1000000))

# Test
is_found, time_taken = search_number(huge_dataset, 999999)
print(f"Number Found: {is_found}")
print(f"Time Taken: {time_taken:.5f} seconds")
