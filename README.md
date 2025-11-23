# README -- Selection Algorithms & Elementary Data Structures

## Overview

This project implements and analyzes two key selection
algorithms---**Deterministic Linear-Time Selection (Median of Medians)**
and **Randomized Quickselect**---along with fundamental data structures
such as **arrays, stacks, queues, and linked lists**. The repository
contains Python implementations, performance discussions, and an
accompanying academic report summarizing theoretical concepts and
empirical findings.

---

## How to Run the Code

### Requirements

- Python 3.8 or higher\
- No additional third-party libraries required

### Running Selection Algorithms

To execute and test both deterministic and randomized selection methods,
run:

```bash
python selection_algorithms.py
```

The script demonstrates: - Median of Medians selection\

- Randomized Quickselect\
- Tests on multiple datasets and k-values

### Running Data Structure Implementations

To explore arrays, stacks, queues, and linked list operations:

```bash
python elementary_data_structures.py
```

Each data structure file includes: - Insert, delete, and access
operations\

- Traversal for linked lists\
- Printed output illustrating behavior and time complexity

---

## Summary of Findings

### Selection Algorithms

Both algorithms correctly identified the k-th smallest value across all
tests, including the sample array\
`[12, 3, 5, 7, 19, 2, 17, 6, 14, 4]`\
where the **5th smallest element = 6**.

- **Median of Medians:**\
  Guaranteed **O(n)** worst-case time due to deterministic pivot
  selection using grouped medians. Performance is reliable but
  slightly slower because of overhead from grouping and recursion.

- **Randomized Quickselect:**\
  Achieved faster empirical performance with **expected O(n)**
  behavior. Although worst-case time is O(n²), poor pivots are
  statistically unlikely, making it efficient for most real-world
  inputs.

### Elementary Data Structures

- **Arrays:** Provide O(1) index access but O(n) insertions/deletions
  due to shifting elements.
- **Stacks & Queues:** Offer O(1) push/pop and enqueue/dequeue
  operations, ideal for LIFO/FIFO workflows.
- **Linked Lists:** Enable O(1) insertions/removals at ends but have
  O(n) search time because traversal is required.

---

## Conclusion

This project demonstrates the algorithmic trade-offs between
deterministic and randomized selection strategies and emphasizes how
elementary data structures influence computational efficiency.
Understanding these tools is essential for designing high-performance
algorithms and choosing appropriate data storage models for different
applications.
