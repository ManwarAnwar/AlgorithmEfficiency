import time
import random
import sys
from randomized_quicksort import randomized_quicksort
from deterministic_quicksort import deterministic_quicksort

sys.setrecursionlimit(2000)

def test_sorts():
    cases = {
        "Random": [random.randint(0, 1000) for _ in range(1000)],
        "Sorted": list(range(1000)),
        "Reverse": list(range(999, -1, -1)),
        "Duplicates": [random.choice([1, 2, 3, 4, 5]) for _ in range(1000)]
    }

    for name, arr in cases.items():
        for sort_name, func in {
            "Randomized": randomized_quicksort,
            "Deterministic": deterministic_quicksort
        }.items():
            arr_copy = arr.copy()
            try:
                start = time.time()
                func(arr_copy)
                duration = time.time() - start
                print(f"{sort_name} Quicksort on {name}: {duration:.6f} seconds")
            except RecursionError:
                print(f"{sort_name} Quicksort on {name}: ❌ RecursionError (Too deep)")

if __name__ == "__main__":
    test_sorts()
