# Hash Tables – Complete Study Notes

**Sources**
- Zero to Mastery DSA Course (Hash Tables section)
- Grokking Algorithms, 2nd Edition – Aditya Y. Bhargava (Chapter 5)
- A Common-Sense Guide to Data Structures and Algorithms – Jay Wengrow
- Common interview patterns & LeetCode

---

## 1. What is a Hash Table?

A **Hash Table** (also called Hash Map / Dictionary / Associative Array) stores data as **key → value** pairs and gives extremely fast average-case performance:

- **Insert** → O(1)
- **Lookup / Get** → O(1)
- **Delete** → O(1)

This is dramatically better than arrays (O(n) search) or sorted arrays (O(log n) search).

### Mental Model (from ZTM + Grokking)
A super-smart librarian. You give a book title (**key**) → she instantly tells you the exact shelf using a **hash function**.

---

## 2. How Hash Tables Work

### Hash Function
Converts a key into an array index.

```
hash("apple")  → 3
hash("banana") → 7
hash("orange") → 3   ← collision!
```

A good hash function should:
- Be deterministic (same key always produces same hash)
- Distribute keys uniformly
- Be fast to compute

### Collisions
When two different keys produce the same hash.

**Two main strategies:**

1. **Separate Chaining**  
   Each slot holds a linked list (or array) of items that hashed to that index.

2. **Open Addressing** (Linear Probing, Quadratic Probing, Double Hashing)  
   If the slot is taken, look for the next empty slot according to a probe sequence.

### Load Factor
```
Load Factor = Number of items / Table size
```
When the load factor gets too high (commonly > 0.7), the table **resizes** (usually doubles) and **rehashes** all existing keys.

---

## 3. Time & Space Complexity

| Operation     | Average Case | Worst Case |
|---------------|--------------|------------|
| Insert        | O(1)         | O(n)       |
| Lookup / Get  | O(1)         | O(n)       |
| Delete        | O(1)         | O(n)       |
| Space         | O(n)         | O(n)       |

In interviews we **almost always** talk about the **average case O(1)**.

Worst case happens when every key collides into the same bucket (extremely rare with a good hash function + resizing).

---

## 4. Using Hash Tables in Code

### JavaScript
```javascript
// Object (string keys only, prototype chain issues)
const map = {};
map["apple"] = 1.2;
console.log(map["apple"]);     // 1.2
console.log("banana" in map);  // false

// Map (better – any key type, no prototype pollution)
const betterMap = new Map();
betterMap.set("apple", 1.2);
betterMap.set(42, "answer");
console.log(betterMap.get("apple")); // 1.2
console.log(betterMap.has(42));      // true
```

### Python
```python
prices = {"apple": 1.2, "banana": 0.8}
print(prices["apple"])           # 1.2
print("banana" in prices)        # True
del prices["banana"]
print(prices.get("orange", 0))   # 0 (safe access)

# dict is the built-in hash table
from collections import defaultdict, Counter
freq = Counter(["a", "b", "a", "c", "a"])
print(freq["a"])                 # 3
```

---

## 5. Real-Life Use Cases

| Use Case                    | Why Hash Table?                          |
|-----------------------------|------------------------------------------|
| Database indexing           | Fast lookup by primary key / unique ID   |
| Caching (Redis, Memcached)  | Instantly check if data is already computed |
| Counting frequencies        | Count how many times each word/item appears |
| Removing duplicates         | Track what we’ve already seen            |
| Phone book / Contacts       | Name → Phone number                      |
| Two Sum style problems      | Store complements for O(1) lookup        |
| Session storage             | Session ID → user data                   |
| DNS / routing tables        | Fast domain → IP resolution              |

---

## 6. Common Patterns with Hash Tables

1. **Frequency Counting**  
   Count occurrences of characters, numbers, words, etc.

2. **Complement / Two Sum pattern**  
   Store what you need to reach the target.

3. **Seen / Visited tracking**  
   Detect duplicates or cycles.

4. **Grouping**  
   Group anagrams, group by some key, etc.

5. **Index mapping**  
   Store value → index for later O(1) retrieval.

6. **Caching / Memoization**  
   Store already computed results.

---

## 7. Common Interview Questions on Hash Tables

1. What is a hash table and how does it work?
2. What is a hash function? What makes a good one?
3. What is a collision and how do we handle it?
4. Explain separate chaining vs open addressing.
5. What is load factor and why does the table resize?
6. What is the average and worst-case time complexity of insert/lookup/delete?
7. When would the worst case actually happen?
8. How would you implement a simple hash table from scratch?
9. What is the difference between a HashMap and a HashSet?
10. Why are hash tables so widely used in real systems?

---

## 8. Popular LeetCode Problems Involving Hash Tables

- Two Sum
- Contains Duplicate
- Valid Anagram
- Group Anagrams
- First Unique Character in a String
- Intersection of Two Arrays
- Happy Number
- Longest Consecutive Sequence
- Ransom Note
- Isomorphic Strings
- Word Pattern
- Subarray Sum Equals K
- 4Sum II
- Design HashMap / Design HashSet
- LRU Cache (advanced – Hash Table + Doubly Linked List)

*(Only names are listed — full solutions are studied separately.)*

---

## 9. Key Takeaways

1. Hash Tables give **average O(1)** insert, lookup, and delete — one of the most powerful tools in programming.
2. They work by converting keys into array indexes via a **hash function**.
3. Collisions are handled by chaining or open addressing.
4. When the table gets too full it **resizes and rehashes**.
5. In interviews, assume average O(1) unless asked about worst case.
6. Hash Tables appear in a huge percentage of real-world systems and interview problems.
7. Master frequency counting, complement patterns, and “seen” tracking — they solve dozens of problems.

---

*End of Hash Tables Notes*
