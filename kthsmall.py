# Import required libraries
import random
import time
import matplotlib.pyplot as plt

def partition(sequence, start_idx, end_idx, target_value=None):
    """
    Partition array segment around a specified value (if provided) or last element.
    Returns final pivot position.
    """
    # If specific target value is provided for pivot
    if target_value is not None:
        # Search for target value and swap with last element
        for current_pos in range(start_idx, end_idx + 1):
            if sequence[current_pos] == target_value:
                sequence[current_pos], sequence[end_idx] = sequence[end_idx], sequence[current_pos]
                break
    
    # Standard partitioning logic using last element as pivot
    boundary_element = sequence[end_idx]  # Pivot value
    boundary_pos = start_idx - 1  # Partition boundary index
    
    # Iterate through array segment
    for scan_pos in range(start_idx, end_idx):
        if sequence[scan_pos] <= boundary_element:
            # Move boundary forward and swap elements
            boundary_pos += 1
            sequence[boundary_pos], sequence[scan_pos] = sequence[scan_pos], sequence[boundary_pos]
    
    # Place pivot in correct position
    sequence[boundary_pos + 1], sequence[end_idx] = sequence[end_idx], sequence[boundary_pos + 1]
    return boundary_pos + 1  # Return final pivot position

def randomized_partition(sequence, start_idx, end_idx):
    """Randomly select pivot and partition array segment."""
    # Choose random pivot index
    random_pos = random.randint(start_idx, end_idx)
    # Swap with last element for standard partitioning
    sequence[random_pos], sequence[end_idx] = sequence[end_idx], sequence[random_pos]
    return partition(sequence, start_idx, end_idx)

def randomized_select(sequence, start_idx, end_idx, target_rank):
    """Find k-th smallest element using randomized QuickSelect algorithm."""
    # Base case: single element array
    if start_idx == end_idx:
        return sequence[start_idx]
    
    # Partition array and get pivot position
    division_point = randomized_partition(sequence, start_idx, end_idx)
    # Calculate rank of pivot (1-based)
    current_rank = division_point - start_idx + 1
    
    # Decide recursion direction based on rank comparison
    if target_rank == current_rank:
        return sequence[division_point]  # Found target element
    elif target_rank < current_rank:
        # Search left partition
        return randomized_select(sequence, start_idx, division_point - 1, target_rank)
    else:
        # Search right partition with adjusted rank
        return randomized_select(sequence, division_point + 1, end_idx, target_rank - current_rank)

def find_median(sequence):
    """Find median value of a small array (<=5 elements)."""
    seq_length = len(sequence)
    # Handle even-length arrays by taking lower median
    if seq_length % 2 == 0:
        return sequence[seq_length // 2 - 1]
    return sequence[seq_length // 2]

def median_of_medians(sequence, start_idx, end_idx, target_rank):
    """Find k-th smallest element using deterministic Median of Medians algorithm."""
    subset_size = end_idx - start_idx + 1
    
    # Base case: directly sort small arrays
    if subset_size <= 5:
        sorted_subset = sorted(sequence[start_idx:end_idx + 1])
        return sorted_subset[target_rank - 1]  # Return k-th element (1-based)
    
    # Split array into 5-element groups and find their medians
    central_values = []
    for group_start in range(start_idx, end_idx + 1, 5):
        # Handle last group which might be smaller than 5
        group_elements = sequence[group_start:min(group_start + 5, end_idx + 1)]
        group_elements.sort()
        central_values.append(find_median(group_elements))
    
    # Recursively find median of medians
    central_of_centrals = median_of_medians(
        central_values, 0, len(central_values) - 1, (len(central_values) + 1) // 2
    )
    
    # Partition array using median of medians as pivot
    division_point = partition(sequence, start_idx, end_idx, central_of_centrals)
    current_rank = division_point - start_idx + 1  # Calculate pivot's rank
    
    # Decide recursion direction
    if target_rank == current_rank:
        return sequence[division_point]
    elif target_rank < current_rank:
        # Search left partition
        return median_of_medians(sequence, start_idx, division_point - 1, target_rank)
    else:
        # Search right partition with adjusted rank
        return median_of_medians(sequence, division_point + 1, end_idx, target_rank - current_rank)

def generate_test_data(size, data_type):
    """Generate different types of test data arrays."""
    if data_type == "random":
        return [random.randint(1, 1000) for _ in range(size)]
    elif data_type == "sorted":
        return list(range(1, size + 1))
    elif data_type == "reversed":
        return list(range(size, 0, -1))
    elif data_type == "duplicates":
        return [random.randint(1, size//10) for _ in range(size)]
    return None

def measure_execution_time(algorithm, data):
    """Measure execution time for finding median element."""
    start_time = time.time()
    k = len(data) // 2  # Select median position
    # Execute algorithm on copied data to preserve original
    algorithm(data.copy(), 0, len(data) - 1, k)
    end_time = time.time()
    return end_time - start_time

def plot_performance(algorithm_name, input_sizes, times_random, times_sorted, times_reversed, times_duplicates):
    """Visualize performance results using matplotlib."""
    plt.figure(figsize=(10, 6))
    # Plot all data series
    plt.plot(input_sizes, times_random, marker='o', label='Random Data', color='skyblue')
    plt.plot(input_sizes, times_sorted, marker='o', label='Sorted Data', color='lightgreen')
    plt.plot(input_sizes, times_reversed, marker='o', label='Reverse Sorted Data', color='salmon')
    plt.plot(input_sizes, times_duplicates, marker='o', label='Duplicate Data', color='purple')
    
    # Configure plot appearance
    plt.xlabel('Input Size (number of elements)')
    plt.ylabel('Execution Time (seconds)')
    plt.title(f'Execution Time of {algorithm_name} for Different Input Types')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def test_algorithms():
    """Main testing function comparing both algorithms."""
    input_sizes = [1000, 5000, 10000, 15000, 20000]
    
    # Initialize time tracking lists
    times_random_rs, times_sorted_rs = [], []
    times_reversed_rs, times_duplicates_rs = [], []
    times_random_mom, times_sorted_mom = [], []
    times_reversed_mom, times_duplicates_mom = [], []
    
    for size in input_sizes:
        # Generate test datasets
        random_data = generate_test_data(size, "random")
        sorted_data = generate_test_data(size, "sorted")
        reversed_data = generate_test_data(size, "reversed")
        duplicates_data = generate_test_data(size, "duplicates")
        
        # Measure Randomized Select performance
        times_random_rs.append(measure_execution_time(randomized_select, random_data))
        times_sorted_rs.append(measure_execution_time(randomized_select, sorted_data))
        times_reversed_rs.append(measure_execution_time(randomized_select, reversed_data))
        times_duplicates_rs.append(measure_execution_time(randomized_select, duplicates_data))
        
        # Measure Median of Medians performance
        times_random_mom.append(measure_execution_time(median_of_medians, random_data))
        times_sorted_mom.append(measure_execution_time(median_of_medians, sorted_data))
        times_reversed_mom.append(measure_execution_time(median_of_medians, reversed_data))
        times_duplicates_mom.append(measure_execution_time(median_of_medians, duplicates_data))
    
    # Generate comparison plots
    plot_performance("Randomized Select", input_sizes, times_random_rs, 
                    times_sorted_rs, times_reversed_rs, times_duplicates_rs)
    plot_performance("Median of Medians", input_sizes, times_random_mom, 
                    times_sorted_mom, times_reversed_mom, times_duplicates_mom)

if __name__ == "__main__":
    random.seed(42)  # Ensure reproducible results
    test_algorithms()