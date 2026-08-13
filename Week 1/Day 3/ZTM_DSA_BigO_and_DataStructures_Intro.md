# ZTM DSA Course – Section 3: Big O + Section 5: Data Structures Introduction

**Sources**: Zero to Mastery DSA Course (Sections 3 & 5), Grokking Algorithms (Chapter 1), Big-O Cheat Sheet, bigocheatsheet.com

---

## 1. What is Big O Notation?

Big O describes **how the runtime (or memory usage) of an algorithm grows** as the input size (`n`) grows.

- It is **not** about exact seconds.
- We care about the **growth rate**.
- Always talk about the **worst case** (Rule 1).

From Grokking Algorithms:  
Binary search on a phone book with 4 billion names takes ~32 steps (`O(log n)`).  
Simple search takes up to 4 billion steps (`O(n)`).  
The difference becomes enormous as `n` grows.

---

## 2. Common Time Complexities (Fastest → Slowest)

| Complexity     | Name            | Everyday Meaning                          | Classic Example                  |
|----------------|-----------------|-------------------------------------------|----------------------------------|
| **O(1)**       | Constant        | Time stays the same no matter how big `n` | Array access by index            |
| **O(log n)**   | Logarithmic     | Doubling `n` adds only ~1 extra step      | Binary Search                    |
| **O(n)**       | Linear          | Time grows in direct proportion to `n`    | Single loop / linear search      |
| **O(n log n)** | Linearithmic    | Slightly worse than linear                | Good sorting algorithms (Merge Sort, Quicksort average) |
| **O(n²)**      | Quadratic       | Nested loops over the same collection     | Selection Sort, Bubble Sort      |
| **O(2ⁿ)**      | Exponential     | Doubles with every extra element          | Naive recursive Fibonacci        |
| **O(n!)**      | Factorial       | Grows extremely fast                      | Generating all permutations, brute-force Traveling Salesperson |

### Visual Growth Order (most important)
```
Excellent → Good → Fair → Bad → Horrible
O(1)  O(log n)  O(n)  O(n log n)  O(n²)  O(2ⁿ)  O(n!)
```

---

## 3. Big O Rules (from the Cheat Sheet – Memorize These)

1. **Always take the worst case**
2. **Drop constants** → `O(2n)` becomes `O(n)`, `O(500)` becomes `O(1)`
3. **Different inputs → different variables**  
   - Two separate arrays of size `a` and `b` → `O(a + b)` or `O(a * b)` if nested
4. **Drop non-dominant terms** → `O(n² + n)` becomes `O(n²)`

**Other quick facts**
- Iterating through half a collection is still **O(n)**
- Nested loops over the **same** collection → **O(n²)**
- Nested loops over **different** collections → **O(a * b)**

---

## 4. What Causes Time Complexity?

- Arithmetic operations (`+ - * /`)
- Comparisons (`< > ==`)
- Looping (`for`, `while`)
- Function calls

---

## 5. Space Complexity

How much **extra memory** an algorithm needs as input grows.

**What causes space complexity?**
- Variables
- Data structures
- Function call stack (especially recursion)
- Allocations

| Example                        | Space     |
|--------------------------------|-----------|
| Just a few variables           | O(1)      |
| Creating a new array of size n | O(n)      |
| Recursion depth of n           | O(n)      |

---

## 6. Code Examples (Python + JavaScript)

### O(1) – Constant
```python
def get_first(arr):
    return arr[0]          # always the same time
```

```javascript
function getFirst(arr) {
  return arr[0];
}
```

### O(n) – Linear
```python
def print_all(arr):
    for item in arr:       # one loop
        print(item)
```

```javascript
function printAll(arr) {
  for (let item of arr) {
    console.log(item);
  }
}
```

### O(n²) – Quadratic
```python
def print_pairs(arr):
    for i in arr:          # nested loops
        for j in arr:
            print(i, j)
```

```javascript
function printPairs(arr) {
  for (let i of arr) {
    for (let j of arr) {
      console.log(i, j);
    }
  }
}
```

### O(log n) – Logarithmic (Binary Search style)
```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1
```

---

## 7. Data Structures – Quick Introduction (Section 5)

A **data structure** is a way to organize and store data so we can use it efficiently.

### Why do we care?
Different structures give different trade-offs for:
- Access
- Search
- Insertion
- Deletion

### Two big categories
1. **Linear** – elements form a sequence  
   Array, Linked List, Stack, Queue
2. **Non-linear** – hierarchical or networked  
   Trees, Graphs, Hash Tables

### Most important Abstract Data Types (ADTs) to know early

| Data Structure     | Ordered? | Unique elements? | Common use                     |
|--------------------|----------|------------------|--------------------------------|
| Array / List       | Yes      | No               | Fast random access             |
| Linked List        | Yes      | No               | Frequent insert/delete at ends |
| Stack              | Yes      | No               | LIFO (undo, call stack)        |
| Queue              | Yes      | No               | FIFO (task scheduling)         |
| Hash Table / Map   | No       | Keys only        | Fast lookups by key            |
| Set                | No       | Yes              | Uniqueness                     |
| Tree / Graph       | —        | —                | Hierarchical / network data    |

From Grokking Algorithms (Chapter 2):  
- **Arrays** → great for reading, bad for inserting in the middle  
- **Linked Lists** → great for inserting/deleting, bad for random access

You will see these same trade-offs again and again throughout the course and in interviews.

---

## 8. Key Takeaways to Remember

- Big O is about **growth**, not absolute speed.
- Always think **worst case**.
- Drop constants and non-dominant terms.
- `O(log n)` and `O(n)` are usually acceptable.
- `O(n²)` and worse become painful very quickly.
- Choosing the right data structure is often more important than clever code.
- Grokking Algorithms Chapter 1 is the perfect companion for this section (binary search vs simple search + the traveling salesperson example for `O(n!)`).

---

*Focused notes for ZTM DSA Section 3 (Big O) + Section 5 (Data Structures Introduction). Only the most important concepts for interviews and daily coding.*
