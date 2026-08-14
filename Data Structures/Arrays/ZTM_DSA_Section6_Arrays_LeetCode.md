# ZTM DSA – Section 6: Arrays + LeetCode Problems

**Topics**: Arrays (Static vs Dynamic, Operations, Big O)  
**LeetCode**: 1. Two Sum · 217. Contains Duplicate · 121. Best Time to Buy and Sell Stock  
**Sources**: Zero to Mastery DSA Course (Section 6), Grokking Algorithms (Chapter 2), LeetCode

---

## 1. Arrays – Key Takeaways

An **array** stores elements in **contiguous** memory locations.  
Because of this, we get very fast access by index.

### Static vs Dynamic Arrays
| Type          | Size          | Resize?     | Common Languages      |
|---------------|---------------|-------------|-----------------------|
| Static        | Fixed at creation | No       | C, classic arrays     |
| Dynamic       | Grows as needed   | Yes (amortized) | JavaScript, Python, Java ArrayList |

In JavaScript and Python the built-in arrays/lists are **dynamic**.

### Core Operations & Time Complexity

| Operation              | Time     | Why |
|------------------------|----------|-----|
| Access by index        | O(1)     | Direct memory address calculation |
| Push / Append (end)    | O(1)*    | Write at the end (*amortized) |
| Pop (end)              | O(1)     | Just remove last element |
| Insert at beginning/middle | O(n) | Must shift elements |
| Delete at beginning/middle | O(n) | Must shift elements |
| Search (unsorted)      | O(n)     | Linear scan |

> **From Grokking Algorithms (Chapter 2)**  
> Arrays are excellent for fast reads.  
> Linked lists are better when you do many insertions/deletions in the middle.

---

## 2. Common Patterns with Arrays

- **Two pointers** (left & right moving toward each other or in the same direction)
- **Sliding window**
- **Hash Map / Set** for O(1) lookups (very common in array problems)
- **Prefix / running values** (min so far, max so far, running sum)

Most interview array problems are solved by combining one of the above patterns with careful Big O thinking.

---

## 3. LeetCode 1. Two Sum

**Problem**  
Given an array of integers `nums` and an integer `target`, return the **indices** of the two numbers that add up to `target`.  
You may assume exactly one solution and you may not use the same element twice.

### Approaches

**1. Brute Force – O(n²)**
```javascript
// Check every pair
for (let i = 0; i < nums.length; i++) {
  for (let j = i + 1; j < nums.length; j++) {
    if (nums[i] + nums[j] === target) return [i, j];
  }
}
```

**2. Optimal – Hash Map – O(n) time & space**

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

**Key Insight**  
While iterating, we ask: “Have I already seen the number that would complete the target?”  
A hash map answers this in O(1).

---

## 4. LeetCode 217. Contains Duplicate

**Problem**  
Given an integer array `nums`, return `true` if any value appears **at least twice**, otherwise return `false`.

### Approaches

**1. Brute Force – O(n²)**  
Compare every element with every other element.

**2. Sorting – O(n log n)**  
Sort the array, then check adjacent elements.

**3. Optimal – Hash Set – O(n) time & space**

```javascript
function containsDuplicate(nums) {
  const seen = new Set();

  for (const num of nums) {
    if (seen.has(num)) return true;
    seen.add(num);
  }
  return false;
}
```

```python
def containsDuplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
```

**Even shorter (Python)**
```python
def containsDuplicate(nums):
    return len(nums) != len(set(nums))
```

**Key Insight**  
A set only stores unique values. If the size of the set is smaller than the original array, a duplicate existed.

---

## 5. LeetCode 121. Best Time to Buy and Sell Stock

**Problem**  
You are given an array `prices` where `prices[i]` is the price of a stock on day `i`.  
You want to maximize profit by choosing **one day to buy** and a **different future day to sell**.  
Return the maximum profit. If no profit is possible, return 0.

### Optimal Approach – One Pass – O(n) time, O(1) space

Track the **lowest price so far** and the **maximum profit** we can make by selling today.

```javascript
function maxProfit(prices) {
  let minPrice = Infinity;
  let maxProfit = 0;

  for (const price of prices) {
    if (price < minPrice) {
      minPrice = price;                 // new lowest buy point
    } else if (price - minPrice > maxProfit) {
      maxProfit = price - minPrice;     // better profit found
    }
  }
  return maxProfit;
}
```

```python
def maxProfit(prices):
    min_price = float("inf")
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit
```

**Key Insight**  
We only need to remember the cheapest price we have seen **before** the current day.  
No need for nested loops.

---

## 6. Quick Comparison of the Three Problems

| Problem                  | Optimal Time | Optimal Space | Main Tool          |
|--------------------------|--------------|---------------|--------------------|
| Two Sum                  | O(n)         | O(n)          | Hash Map           |
| Contains Duplicate       | O(n)         | O(n)          | Hash Set           |
| Best Time to Buy/Sell    | O(n)         | O(1)          | Running min + max  |

---

## 7. Section 6 Recap – What You Should Remember

- Arrays give **O(1)** access but **O(n)** insert/delete in the middle.
- Most array interview problems are solved with:
  1. Hash Map / Set
  2. Two pointers
  3. One-pass tracking of min/max/running values
- Always start by asking:  
  “Can I trade space for time?” (Hash Map/Set)  
  “Do I need to look at every pair?” (usually no)
- Practice writing both the brute-force and the optimal solution so you can explain the improvement.

---

*Notes compiled from ZTM DSA Section 6 (Arrays) + the three LeetCode problems solved on this topic.*
