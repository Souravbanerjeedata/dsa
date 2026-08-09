# Grokking Algorithms – Day 1 Notes
**Chapters 1 & 2 (Binary Search → Selection Sort)**

---

## 1. Binary Search

**Core idea**  
Works only on a **sorted** list. Repeatedly check the middle element and discard half of the remaining elements.

```python
def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None
```

**Time complexity**: \( O(\log n) \)

### Exercises
| # | Question | Answer |
|---|----------|--------|
| 1.1 | Sorted list of 128 names → max steps with binary search? | **7** (\( 128 = 2^7 \)) |
| 1.2 | List size doubled (256) → max steps? | **8** (\( 256 = 2^8 \)) |

**Key insight**  
Binary search is dramatically faster than simple search as the list grows.  
\( O(\log n) \) grows very slowly compared to \( O(n) \).

---

## 2. Big O Notation & Running Time

- Algorithm speed is **not** measured in seconds.
- We measure how the runtime **grows** as the input size grows.
- Written in Big O notation.

### Common runtimes (from fastest to slowest)
| Notation     | Name              | Example |
|--------------|-------------------|---------|
| \( O(1) \)   | Constant          | Array access by index |
| \( O(\log n) \) | Logarithmic    | Binary search |
| \( O(n) \)   | Linear            | Simple search |
| \( O(n \log n) \) | Log-linear   | Fast sorting algorithms |
| \( O(n^2) \) | Quadratic         | Selection sort, nested loops |
| \( O(n!) \)  | Factorial         | Traveling Salesperson (brute force) |

### Phone-book exercises
| # | Scenario | Runtime |
|---|----------|---------|
| 1.3 | Name → find phone number | \( O(\log n) \) (binary search possible) |
| 1.4 | Phone number → find name | \( O(n) \) (must scan whole book) |
| 1.5 | Read every number | \( O(n) \) |
| 1.6 | Read only the “A”s | \( O(n) \) in worst case (still have to look through the book to find where As end) |

---

## 3. Arrays vs Linked Lists

Your computer’s memory is like a giant set of drawers.

| Feature              | Array                          | Linked List                     |
|----------------------|--------------------------------|---------------------------------|
| Memory layout        | Contiguous (side-by-side)      | Scattered (each node points to next) |
| Random access        | \( O(1) \)                     | \( O(n) \)                      |
| Insert / Delete      | \( O(n) \) (need to shift)     | \( O(1) \) (if you have the position) |
| Best for             | Fast reads, binary search      | Frequent inserts/deletes        |

### Decision guide from the book

**Restaurant order queue**  
Servers add to the back, chef takes from the front.  
→ **Linked List** (both ends \( O(1) \) with head + tail pointers)

**Facebook usernames + binary search**  
Many logins (searches), need instant middle access.  
→ **Array** (random access \( O(1) \))

**Downside of array when users keep signing up**  
To keep the list sorted for binary search:
- Find correct position
- Shift all later elements → \( O(n) \)
- Occasionally resize the whole array → another \( O(n) \)

**Trade-off summary**  
- Arrays → fast reads, slow inserts/deletes  
- Linked lists → fast inserts/deletes, slow reads

---

## 4. Selection Sort

**Idea**  
Repeatedly find the **smallest** remaining element and put it in its final place.

### How it works
1. Find the smallest element in the unsorted portion.
2. Swap it with the first unsorted element.
3. Shrink the unsorted portion by one and repeat.

### Code (from your practice file)

```python
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    copiedArr = list(arr)          # avoid mutating original
    for i in range(len(copiedArr)):
        smallest = findSmallest(copiedArr)
        newArr.append(copiedArr.pop(smallest))
    return newArr
```

**Example**  
`[5, 3, 6, 2, 10]`  
→ `[2, 3, 5, 6, 10]`

**Complexity**
- Time: \( O(n^2) \) (always — roughly \( n + (n-1) + \dots + 1 \) comparisons)
- Space: \( O(n) \) with the version above (or \( O(1) \) extra if you sort in-place)

**When to use**  
- Very simple to understand and implement
- Only practical for tiny lists
- Good teaching example of a quadratic algorithm

**One-liner**  
“Find the next smallest and put it in place, again and again.”

---

## Quick Recap – Day 1

- Binary search → \( O(\log n) \), needs sorted array + random access
- Big O tells us how runtime grows with input size
- Arrays: fast reads, slow inserts
- Linked lists: fast inserts/deletes, slow reads
- Selection sort: simple but \( O(n^2) \)

---

*Notes compiled from Chapters 1–2 of Grokking Algorithms (2nd Edition) + your practice file.*
