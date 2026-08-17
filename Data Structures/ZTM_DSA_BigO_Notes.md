# Big O Notation – Complete Study Notes

**Sources**
- Zero to Mastery DSA Course (Section 3 – Big O)
- Grokking Algorithms, 2nd Edition – Aditya Y. Bhargava (Chapter 1)
- A Common-Sense Guide to Data Structures and Algorithms – Jay Wengrow (Chapter 3: O Yes! Big O Notation + related chapters)
- Big-O Cheat Sheet (bigocheatsheet.com)

---

## 1. What is Big O Notation?

Big O describes **how the runtime (or memory usage) of an algorithm grows as the input size (n) grows**.

Key points:
- It is **not** about exact seconds or absolute speed.
- We care about the **growth rate**.
- We almost always talk about the **worst case** (most important rule).

### From Grokking Algorithms
Binary search on a phone book with 4 billion names takes ~32 steps → **O(log n)**.  
Simple search takes up to 4 billion steps → **O(n)**.  
The difference becomes enormous as `n` grows.

### From A Common-Sense Guide
Big O answers one simple question:

> “How many steps does this algorithm take **relative to** the number of elements (N)?”

It is a way of expressing the **efficiency** of an algorithm in terms of the size of the data it processes.

---

## 2. Common Time Complexities (Fastest → Slowest)

| Complexity   | Name          | Everyday Meaning                              | Classic Example                  |
|--------------|---------------|-----------------------------------------------|----------------------------------|
| O(1)         | Constant      | Time stays the same no matter how big n       | Array access by index            |
| O(log n)     | Logarithmic   | Doubling n adds only ~1 extra step            | Binary Search                    |
| O(n)         | Linear        | Time grows in direct proportion to n          | Single loop / Linear search      |
| O(n log n)   | Linearithmic  | Slightly worse than linear                    | Merge Sort, Quicksort (average)  |
| O(n²)        | Quadratic     | Nested loops over the same collection         | Bubble Sort, Selection Sort      |
| O(2ⁿ)        | Exponential   | Doubles with every extra element              | Naive recursive Fibonacci        |
| O(n!)        | Factorial     | Grows extremely fast                          | All permutations, TSP brute-force|

### Visual Growth Order (Most Important)

```
Excellent → Good → Fair → Bad → Horrible
O(1)   O(log n)   O(n)   O(n log n)   O(n²)   O(2ⁿ)   O(n!)
```

---

## 3. Big O Rules (Memorize These)

From ZTM + Common-Sense Guide + Grokking:

1. **Always take the worst case**
2. **Drop constants**  
   - O(2n) → O(n)  
   - O(500) → O(1)  
   - O(n/2) is still O(n)
3. **Different inputs → different variables**  
   - Two separate arrays of size `a` and `b` → O(a + b) or O(a × b) if nested
4. **Drop non-dominant terms**  
   - O(n² + n) → O(n²)  
   - O(n + log n) → O(n)

### Other Quick Facts
- Iterating through **half** a collection is still **O(n)**
- Nested loops over the **same** collection → **O(n²)**
- Nested loops over **different** collections → **O(a × b)**
- Even if a loop runs only `n/2` or `n/3` times, it is still linear: **O(n)**

---

## 4. What Causes Time Complexity?

Anything that takes work:
- Arithmetic operations (`+ − * /`)
- Comparisons (`< > ==`)
- Looping (`for`, `while`)
- Function calls
- Recursion (each call adds work)

---

## 5. Space Complexity

**Space complexity** measures how much **extra memory** an algorithm needs as the input size grows.

### What causes space complexity?
- Variables
- Data structures (arrays, hash tables, etc.)
- Function call stack (especially recursion)
- Allocations

| Example                        | Space     |
|--------------------------------|-----------|
| A few variables                | O(1)      |
| An array of size n             | O(n)      |
| Recursive call stack of depth n| O(n)      |
| Creating a new array of size n²| O(n²)     |

**Rule of thumb**: If you create a new data structure whose size depends on `n`, that usually dominates the space complexity.

---

## 6. Practical Understanding from Common-Sense Guide

### Counting Steps
Instead of saying “this is fast”, we count the actual number of steps relative to N:

- Looking up an array element by index → **1 step** → O(1)
- Searching an unordered array → up to **N steps** → O(n)
- Binary search on a sorted array → roughly **log₂ N steps** → O(log n)

### Why Logarithms Appear
Every time you **halve** the problem size, you get a logarithm.

Binary search example (from both Grokking and Common-Sense Guide):
- 100 elements → ~7 steps
- 1,000 elements → ~10 steps
- 1,000,000 elements → ~20 steps

This is why O(log n) is considered extremely efficient.

---

## 7. Code Examples (Python + JavaScript)

### O(1) – Constant Time
```python
def get_first(arr):
    return arr[0]          # always 1 step
```

```javascript
function getFirst(arr) {
  return arr[0];           // always 1 step
}
```

### O(n) – Linear Time
```python
def find_max(arr):
    max_val = arr[0]
    for num in arr:        # loops n times
        if num > max_val:
            max_val = num
    return max_val
```

```javascript
function findMax(arr) {
  let maxVal = arr[0];
  for (let num of arr) {   // loops n times
    if (num > maxVal) maxVal = num;
  }
  return maxVal;
}
```

### O(n²) – Quadratic Time
```python
def print_pairs(arr):
    for i in arr:          # n times
        for j in arr:      # n times
            print(i, j)    # total n * n steps
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

### O(log n) – Binary Search Style
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

```javascript
function binarySearch(arr, target) {
  let left = 0, right = arr.length - 1;
  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    if (arr[mid] === target) return mid;
    if (arr[mid] < target) left = mid + 1;
    else right = mid - 1;
  }
  return -1;
}
```

---

## 8. Real-Life Use Cases

| Situation                              | Typical Complexity | Why it matters                          |
|----------------------------------------|--------------------|-----------------------------------------|
| Looking up a user by ID in a database  | O(1) or O(log n)   | Must stay fast even with millions of users |
| Searching a contact in an unsorted list| O(n)               | Becomes slow with large lists           |
| Sorting a large dataset                | O(n log n)         | Better than O(n²) algorithms            |
| Checking if an item exists (hash set)  | O(1) average       | Extremely fast membership tests         |
| Generating all possible passwords      | O(n!) or O(2ⁿ)     | Quickly becomes impossible              |

---

## 9. Common Interview Questions on Big O

1. What is Big O notation and why do we use it?
2. Explain the difference between O(n) and O(log n).
3. What is the time complexity of accessing an element in an array by index?
4. What is the time complexity of inserting at the beginning of an array? Why?
5. Drop the constants and non-dominant terms: O(3n² + 5n + 100)
6. What is the space complexity of a recursive function that makes n calls?
7. Why do we usually care about the **worst case**?
8. Is O(n/2) the same as O(n)? Explain.
9. Compare linear search vs binary search in terms of Big O.
10. Give a real-world example of an O(n²) algorithm and why it can be a problem.

---

## 10. Popular LeetCode Problems Involving Big O Thinking

- Two Sum
- Contains Duplicate
- Best Time to Buy and Sell Stock
- Valid Anagram
- Group Anagrams
- Longest Consecutive Sequence
- Product of Array Except Self
- Maximum Subarray
- Climbing Stairs
- Fibonacci Number (and its optimizations)

*(You should be able to analyze both the brute-force and the optimal solution’s time & space complexity for each of these.)*

---

## 11. Quick Reference Cheat Sheet

```
O(1)       → Constant       → Excellent
O(log n)   → Logarithmic    → Excellent
O(n)       → Linear         → Good / Fair
O(n log n) → Linearithmic   → Fair
O(n²)      → Quadratic      → Bad
O(2ⁿ)      → Exponential    → Horrible
O(n!)      → Factorial      → Horrible
```

**Rules to remember forever:**
1. Worst case
2. Drop constants
3. Different inputs = different variables
4. Drop non-dominant terms

---

*End of Big O Notes*  
*Next: Data Structures Introduction*
