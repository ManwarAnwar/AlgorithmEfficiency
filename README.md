
# Algorithm Efficiency and Scalability

This project compares the efficiency and scalability of two algorithmic techniques:
- Randomized Quicksort
- Hash Table using Chaining

## 📁 Files Included
- `randomized_quicksort.py`: Randomized quicksort implementation.
- `deterministic_quicksort.py`: Deterministic quicksort using first element as pivot.
- `quicksort_comparison.py`: Empirical performance comparison between the two sorting algorithms.
- `hash_table.py`: Hash table implementation using chaining.

## 🧪 How to Run

1. Clone the repository or copy files into a directory.
2. Ensure Python 3 is installed.
3. Run quicksort comparison:
    ```bash
    python quicksort_comparison.py
    ```
4. Use the hash table by importing `HashTable` class from `hash_table.py`.

## Summary

- Randomized Quicksort is efficient and avoids worst-case scenarios using random pivot selection.
- Hash Tables with chaining offer constant-time average-case operations if the load factor is managed well.
- Full analysis is provided in the `Algorithm_Efficiency_Report.docx` file.
