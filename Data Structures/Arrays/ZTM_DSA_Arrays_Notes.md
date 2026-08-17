# Arrays – Complete Study Notes

**Sources**
- Zero to Mastery DSA Course (Section 6 – Arrays)
- Grokking Algorithms, 2nd Edition – Aditya Y. Bhargava (Chapter 2)
- A Common-Sense Guide to Data Structures and Algorithms – Jay Wengrow (Chapters 1–2)
- LeetCode Top Interview patterns involving arrays

---

## 1. What is an Array?

An **array** stores a collection of elements in **contiguous memory locations**.

Because the elements sit next to each other in memory, the computer can jump directly to any index using simple arithmetic:

```
address of element i = base_address + (i × size_of_each_element)
```

This is why **access by index is O(1)** — the fastest possible access.

---

## 2. Static vs Dynamic Arrays

| Type     | Size              | Resize?          | Common Languages                  |
|----------|-------------------|------------------|-----------------------------------|
| Static   | Fixed at creation | No               | C, classic arrays                 |
| Dynamic  | Grows as needed   | Yes (amortized)  | Python `list`, JavaScript `Array`, Java `ArrayList` |

In Python and JavaScript the built-in arrays/lists are **dynamic**.

### How Dynamic Arrays Grow (Amortized Analysis)

When a dynamic array runs out of space it typically:
1. Allocates a new array of double the size
2. Copies all existing elements over
3. Continues

Even though the occasional resize costs O(n), the *average* cost of many appends is still **O(1)**. This is called **amortized O(1)**.

---

## 3. Core Operations & Time Complexity

| Operation                  | Time      | Why                                      |
|----------------------------|-----------|------------------------------------------|
| Access by index            | O(1)      | Direct memory address calculation        |
| Push / Append (end)        | O(1)*     | Write at the end (*amortized)            |
| Pop (end)                  | O(1)      | Just remove last element                 |
| Insert / Delete (middle)   | O(n)      | Must shift all subsequent elements       |
| Search (unsorted)          | O(n)      | Linear scan                              |
| Search (sorted + binary)   | O(log n)  | Halve the search space each time         |

**From Grokking Algorithms (Chapter 2)**:  
Arrays are excellent for fast reads. Linked lists are better when you do many insertions/deletions in the middle.

**From Common-Sense Guide**:  
Deleting or inserting at the beginning of an array is the worst case because every element after it must be shifted.

---

## 4. Building an Array from Scratch (Mental Model)

To truly understand arrays, it helps to implement a simple dynamic array yourself:

### Core idea
- Keep a fixed-size underlying storage
- Track the current `length`
- When full → allocate bigger storage and copy

### Python-style sketch
```python
class MyArray:
    def __init__(self):
        self.length = 0
        self.data = {}          # using dict to simulate contiguous slots

    def get(self, index):
        return self.data[index]

    def push(self, item):
        self.data[self.length] = item
        self.length += 1
        return self.length

    def pop(self):
        last = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return last

    def delete(self, index):
        # shift everything after index to the left
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]
        del self.data[self.length - 1]
        self.length -= 1
```

### JavaScript-style sketch
```javascript
class MyArray {
  constructor() {
    this.length = 0;
    this.data = {};
  }

  get(index) {
    return this.data[index];
  }

  push(item) {
    this.data[this.length] = item;
    this.length++;
    return this.length;
  }

  pop() {
    const lastItem = this.data[this.length - 1];
    delete this.data[this.length - 1];
    this.length--;
    return lastItem;
  }

  delete(index) {
    this.shiftItems(index);
  }

  shiftItems(index) {
    for (let i = index; i < this.length - 1; i++) {
      this.data[i] = this.data[i + 1];
    }
    delete this.data[this.length - 1];
    this.length--;
  }
}
```

This exercise shows **why** insert/delete in the middle is O(n).

---

## 5. Common Patterns with Arrays

These patterns appear constantly in interviews:

1. **Two Pointers**  
   - Left & right moving toward each other  
   - Or both moving in the same direction  
   - Classic for sorted arrays, palindromes, container-with-most-water, etc.

2. **Sliding Window**  
   - Maintain a window that expands/contracts  
   - Used for subarray/substring problems (minimum size subarray sum, longest substring without repeating characters, etc.)

3. **Hash Map / Set for O(1) lookups**  
   - Extremely common complement to arrays  
   - Two Sum, Contains Duplicate, Group Anagrams, etc.

4. **Prefix / Running values**  
   - Keep track of min-so-far, max-so-far, running sum  
   - Best Time to Buy and Sell Stock, Maximum Subarray, Product of Array Except Self, etc.

5. **In-place modification**  
   - Two pointers to overwrite the array without extra space  
   - Remove Duplicates, Move Zeroes, etc.

---

## 6. Real-Life Use Cases of Arrays

| Use Case                        | Why Array?                              |
|---------------------------------|-----------------------------------------|
| Image pixels                    | Contiguous memory, fast random access   |
| Lookup tables / caches          | Index = key, O(1) access                |
| Matrices / grids / game boards  | Natural 2-D layout                      |
| Time-series data                | Sequential access is cache-friendly     |
| Implementing other structures   | Stacks, Queues, Hash Tables, Heaps often use arrays under the hood |

---

## 7. Common Interview Questions on Arrays

1. What is the time complexity of accessing an element by index? Why?
2. What is the difference between a static and a dynamic array?
3. Explain amortized O(1) for appending to a dynamic array.
4. Why is inserting at the beginning of an array O(n)?
5. How would you implement a dynamic array from scratch?
6. When would you choose a linked list over an array?
7. What is the difference between an array and a set?
8. Explain the two-pointer technique with an example.
9. What is a sliding window and when do you use it?
10. How can you reverse an array in-place?

---

## 8. Popular LeetCode Problems on Arrays

- Two Sum
- Contains Duplicate
- Best Time to Buy and Sell Stock
- Best Time to Buy and Sell Stock II
- Product of Array Except Self
- Maximum Subarray
- Maximum Product Subarray
- Container With Most Water
- 3Sum
- Move Zeroes
- Remove Duplicates from Sorted Array
- Rotate Array
- Plus One
- Merge Sorted Array
- Majority Element
- Jump Game / Jump Game II
- Longest Consecutive Sequence
- First Missing Positive

*(Only names are listed — full solutions are studied in the LeetCode 150 book.)*

---

## 9. Key Takeaways

1. Arrays give the fastest possible access by index (**O(1)**).
2. Inserting or deleting in the middle is expensive (**O(n)**) because of shifting.
3. Dynamic arrays give amortized O(1) appends, but occasional resizing costs O(n).
4. Most interview array problems are solved with **two pointers**, **sliding window**, **hash maps**, or **prefix techniques**.
5. Mastering arrays is non-negotiable — almost every other structure is built on top of them or compared against them.

---

*End of Arrays Notes*  
*Next: Hash Tables*
