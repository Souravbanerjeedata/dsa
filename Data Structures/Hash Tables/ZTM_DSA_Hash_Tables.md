# ZTM DSA – Hash Tables

**Sources**: Zero to Mastery DSA Course (Hash Tables section), Grokking Algorithms (Chapter 5), LeetCode  
**Related previous topics**: Arrays, Big O, Two Sum, Contains Duplicate, First Recurring Character

---

## 1. What is a Hash Table?

A **Hash Table** (also called Hash Map / Dictionary) is a data structure that stores data as **key → value** pairs.

It gives us extremely fast average-case performance:
- Insert → **O(1)**
- Lookup → **O(1)**
- Delete → **O(1)**

This is much better than arrays (O(n) search) or sorted arrays (O(log n) search).

### Simple Mental Model
Think of a super-smart librarian:
- You give her a book title (the **key**)
- She instantly tells you the exact shelf location (using a **hash function**)
- She never has to walk through every shelf

---

## 2. How Hash Tables Work

### Hash Function
A **hash function** takes a key and converts it into an array index.

```
hash("apple")  →  3
hash("banana") →  7
hash("orange") →  3   ← collision!
```

Good hash functions:
- Are fast to compute
- Distribute keys evenly
- Minimize collisions

### Collisions
When two different keys produce the same hash → **collision**.

**Common ways to handle collisions:**
1. **Separate Chaining** → Each slot holds a linked list (or array) of items
2. **Open Addressing** (Linear Probing, Quadratic Probing, Double Hashing) → Find the next empty slot

In interviews you rarely implement collision handling from scratch. Just know that collisions exist and that average performance is still O(1) with a good hash function + reasonable load factor.

### Load Factor
```
Load Factor = Number of items / Table size
```
When the load factor gets too high (usually > 0.7), the table **resizes** (grows) and rehashes everything.

---

## 3. Time & Space Complexity

| Operation     | Average Case | Worst Case |
|---------------|--------------|------------|
| Insert        | O(1)         | O(n)       |
| Lookup / Get  | O(1)         | O(n)       |
| Delete        | O(1)         | O(n)       |
| Space         | O(n)         | O(n)       |

> In interviews we almost always talk about the **average case O(1)**.

---

## 4. Using Hash Tables in Code

### JavaScript

```javascript
// Using plain Object
const map = {};
map["apple"] = 1.2;
map["banana"] = 0.8;

console.log(map["apple"]);     // 1.2
console.log("banana" in map);  // true
delete map["banana"];

// Using Map (better for non-string keys)
const betterMap = new Map();
betterMap.set("apple", 1.2);
betterMap.set(42, "answer");
console.log(betterMap.get("apple")); // 1.2
console.log(betterMap.has(42));      // true
```

### Python

```python
# Dictionary (the most used hash table)
prices = {
    "apple": 1.2,
    "banana": 0.8
}

print(prices["apple"])        # 1.2
print("banana" in prices)     # True
del prices["banana"]

# Using .get() to avoid KeyError
print(prices.get("orange", 0))  # 0
```

---

## 5. Real-Life Use Cases

| Use Case                        | Why Hash Table?                              |
|--------------------------------|----------------------------------------------|
| Database indexing              | Fast lookup by primary key / unique ID       |
| Caching (Redis, Memcached)     | Instantly check if data is already computed  |
| Counting word frequencies      | Count how many times each word appears       |
| Removing duplicates            | Track what we’ve already seen                |
| Phone book / Contact list      | Name → Phone number                          |
| Compiler symbol tables         | Variable name → memory address               |
| Browser history / cookies      | Fast existence checks                        |
| Two Sum / Interview problems   | Store complements for O(1) lookup            |

---

## 6. Common Interview Questions on Hash Tables

**Conceptual**
- What is a hash function?
- What is a collision and how do we handle it?
- What is load factor? Why do we resize?
- Difference between HashMap and HashSet?
- When would you prefer a TreeMap over a HashMap?

**Coding Problems (Very Common)**
- Two Sum
- Contains Duplicate
- First Recurring Character
- Group Anagrams
- Valid Anagram
- Longest Consecutive Sequence
- Subarray Sum Equals K
- Top K Frequent Elements
- LRU Cache
- Insert Delete GetRandom O(1)

---

## 7. LeetCode Examples

### Example 1: Two Sum (LeetCode 1)

**Problem**: Return indices of two numbers that add up to `target`.

```javascript
function twoSum(nums, target) {
  const map = {};                       // value → index

  for (let i = 0; i < nums.length; i++) {
    const complement = target - nums[i];
    if (map[complement] !== undefined) {
      return [map[complement], i];
    }
    map[nums[i]] = i;
  }
}
```

```python
def twoSum(nums, target):
    seen = {}                           # value → index

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
```

**Time**: O(n) | **Space**: O(n)

---

### Example 2: Contains Duplicate / First Recurring Character

**Problem**: Return the first number that appears more than once.  
If none, return `undefined` / `None`.

```javascript
function firstRecurringCharacter(arr) {
  const seen = new Set();               // or use a Map/Object

  for (const item of arr) {
    if (seen.has(item)) return item;
    seen.add(item);
  }
  return undefined;
}
```

```python
def first_recurring_character(arr):
    seen = set()

    for item in arr:
        if item in seen:
            return item
        seen.add(item)
    return None
```

**Using Hash Map instead of Set:**

```javascript
function firstRecurringCharacter(arr) {
  const map = {};
  for (const item of arr) {
    if (map[item]) return item;
    map[item] = true;
  }
  return undefined;
}
```

```python
def first_recurring_character(arr):
    map = {}
    for item in arr:
        if item in map:
            return item
        map[item] = True
    return None
```

---

### Example 3: Valid Anagram (LeetCode 242)

**Problem**: Check if two strings are anagrams of each other.

```javascript
function isAnagram(s, t) {
  if (s.length !== t.length) return false;

  const count = {};

  for (const char of s) {
    count[char] = (count[char] || 0) + 1;
  }

  for (const char of t) {
    if (!count[char]) return false;
    count[char]--;
  }
  return true;
}
```

```python
def isAnagram(s, t):
    if len(s) != len(t):
        return False

    count = {}

    for char in s:
        count[char] = count.get(char, 0) + 1

    for char in t:
        if char not in count or count[char] == 0:
            return False
        count[char] -= 1

    return True
```

**Time**: O(n) | **Space**: O(1) (only 26 letters) or O(k) where k is unique characters

---

## 8. Key Takeaways

- Hash Tables give **average O(1)** insert, lookup, and delete.
- They are one of the most useful data structures in interviews and real systems.
- Most “smart” array solutions use a Hash Map or Hash Set under the hood.
- From Grokking Algorithms (Chapter 5):  
  > “When I want to solve a problem, the two plans of attack I start with are ‘Can I use a hash table?’ and ‘Can I model this as a graph?’”
- Always ask yourself:  
  **“Can I trade some space for a big speed improvement using a hash table?”**

---

*Notes compiled from ZTM DSA Hash Tables section + Grokking Algorithms Chapter 5 + common LeetCode patterns.*
