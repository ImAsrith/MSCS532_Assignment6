# MSCS532 Assignment6

This assignment implements and analyzes two main components:
1. Selection Algorithms (kthsmall.py)
2. Elementary Data Structures (data_structures.py)

## Setup and Requirements

To run this project, you need:
- Python 3.x
- matplotlib (for visualization)
- dsa module (for data structures implementation)

## Running the Programs

### Selection Algorithms (kthsmall.py)
```bash
python kthsmall.py
```
This will:
- Run both Randomized Select and Median of Medians algorithms
- Generate performance comparison plots
- Test with different input distributions (random, sorted, reversed, duplicates)
- Show execution time visualization for different input sizes

### Data Structures (data_structures.py)
```bash
python data_structures.py
```
This will run tests demonstrating the functionality of:
- Arrays
- Matrices
- Stacks
- Queues
- Singly Linked Lists

## Key Findings

### Selection Algorithms Analysis

1. Randomized Select (QuickSelect):
   - Performs best with smaller inputs (up to 5000 elements)
   - Shows efficient performance on sorted data
   - Exhibits some volatility with reverse-sorted data
   - Generally faster but less predictable

2. Median of Medians:
   - Demonstrates consistent linear time growth
   - Shows uniform performance across all input types
   - Higher but predictable execution times
   - Preferred when consistency is crucial

### Data Structures Analysis

1. Arrays vs Linked Lists:
   - Arrays: O(1) random access, ideal for caching and lookup tables
   - Linked Lists: Better for frequent insertions/deletions
   - Trade-off between access speed and modification efficiency

2. Specialized Data Structures:
   - Stacks (LIFO): Optimal for function call tracking and recursion
   - Queues (FIFO): Essential for scheduling and BFS algorithms

3. Implementation Considerations:
   - Memory overhead varies between implementations
   - Choice depends on specific use case requirements
   - Performance characteristics differ based on operation patterns

## Conclusion

The choice of algorithm or data structure should be based on specific requirements:
- For selection algorithms, use Randomized Select for better average-case performance and Median of Medians for predictable execution times
- For data structures, consider the primary operations (access vs modifications) and specific use case requirements when making implementation choices
