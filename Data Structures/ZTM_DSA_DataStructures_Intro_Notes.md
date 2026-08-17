# Data Structures Introduction – Complete Study Notes

**Sources**
- Zero to Mastery DSA Course (Section 5 – Data Structures Introduction)
- Grokking Algorithms, 2nd Edition – Aditya Y. Bhargava
- A Common-Sense Guide to Data Structures and Algorithms – Jay Wengrow (Chapters 1–2)
- Wikipedia List of Data Structures + common interview knowledge

---

## 1. What is a Data Structure?

A **data structure** is a way of organizing and storing data so that it can be accessed and modified efficiently.

From *A Common-Sense Guide*:
> Data structures are the foundation of how we store and organize information in our programs. Choosing the right one can make the difference between a program that runs in milliseconds and one that takes minutes (or never finishes).

From ZTM:
- Data structures are the building blocks of algorithms.
- Different structures are optimized for different operations (read, write, insert, delete, search).

**Mental Model**:  
Think of data structures as different types of containers. A backpack, a filing cabinet, a stack of plates, and a phone book all store things, but each is better for certain tasks.

---

## 2. Why Data Structures Matter

From *A Common-Sense Guide* (Chapter 1):

1. **Speed** – Some operations are dramatically faster with the right structure.
2. **Memory usage** – Some structures use more or less memory.
3. **Correctness & constraints** – Some structures enforce rules (e.g. uniqueness in a Set).

**Classic example from the book**:
- An **array** gives O(1) access by index but O(n) insertion/deletion in the middle.
- A **set** prevents duplicates, but insertion becomes slower because you must first check whether the value already exists.

Choosing the wrong structure is one of the most common reasons software becomes slow as data grows.

---

## 3. The Two Big Categories

### 1. Primitive / Built-in
- Integers, Floats, Booleans, Characters/Strings (in most languages)
- These are the basic building blocks.

### 2. Non-Primitive / Composite (what we mainly study)
- **Linear**: Array, Linked List, Stack, Queue
- **Non-Linear**: Tree, Graph, Heap, Hash Table

We also talk about **Abstract Data Types (ADTs)** – the *interface* (what operations it supports) vs the *concrete implementation* (how it is built under the hood).

---

## 4. Core Operations We Always Analyze

For almost every data structure we ask:

| Operation              | What it means                          |
|------------------------|----------------------------------------|
| Access / Read          | Get the value at a known location      |
| Search                 | Find if a value exists                 |
| Insertion              | Add a new value                        |
| Deletion               | Remove a value                         |
| Traversal              | Visit every element                    |

We measure these with **Big O** (time and space).

---

## 5. The Foundational Data Structure: The Array

From both *Common-Sense Guide* and *Grokking Algorithms*:

An **array** stores elements in **contiguous memory**.

### Advantages
- Extremely fast access by index → **O(1)**
- Excellent cache locality (CPU loves contiguous memory)

### Disadvantages
- Inserting or deleting in the middle requires shifting elements → **O(n)**
- Fixed size in some languages (static arrays)
- Dynamic arrays (Python list, JS Array, Java ArrayList) can grow, but resizing is expensive (amortized O(1) for append)

### Static vs Dynamic Arrays

| Type     | Size              | Resize?          | Common Languages              |
|----------|-------------------|------------------|-------------------------------|
| Static   | Fixed at creation | No               | C, classic arrays             |
| Dynamic  | Grows as needed   | Yes (amortized)  | Python, JavaScript, Java ArrayList |

**Key insight from Common-Sense Guide**:  
Even though appending to a dynamic array is usually fast, the occasional resize (copying all elements to a bigger array) still makes the *worst-case* of a single append O(n). We still call it amortized O(1) because the expensive resizes are rare.

---

## 6. How We Measure Efficiency (Recap)

From the books:

We count **steps** relative to N (the number of elements).

- Looking up `arr[5]` → 1 step → O(1)
- Searching an unordered array → up to N steps → O(n)
- Inserting at the beginning of an array → N + 1 steps (shift everything) → O(n)

This step-counting mindset is the heart of choosing good data structures.

---

## 7. High-Level Map of Important Data Structures

| Data Structure     | Best For                          | Access     | Search     | Insert     | Delete     | Notes                          |
|--------------------|-----------------------------------|------------|------------|------------|------------|--------------------------------|
| Array / List       | Fast index access, sequential     | O(1)       | O(n)       | O(n)*      | O(n)*      | *middle; end is amortized O(1)|
| Linked List        | Frequent insert/delete in middle  | O(n)       | O(n)       | O(1)**     | O(1)**     | **if you have the node        |
| Stack              | LIFO (last in, first out)         | O(n)       | O(n)       | O(1)       | O(1)       | Undo, recursion, DFS           |
| Queue              | FIFO (first in, first out)        | O(n)       | O(n)       | O(1)       | O(1)       | BFS, task scheduling           |
| Hash Table         | Fast lookups by key               | —          | O(1) avg   | O(1) avg   | O(1) avg   | Most used structure in practice|
| Tree / BST         | Ordered data, range queries       | O(log n)   | O(log n)   | O(log n)   | O(log n)   | Balanced is important          |
| Heap               | Priority / Min-Max                | O(1) peak  | O(n)       | O(log n)   | O(log n)   | Priority queues                |
| Graph              | Relationships, networks           | —          | O(V+E)     | —          | —          | Social networks, maps, etc.    |

---

## 8. Real-Life Analogies (from ZTM + Common-Sense Guide)

| Data Structure | Real-Life Analogy                              |
|----------------|------------------------------------------------|
| Array          | A row of numbered lockers                      |
| Linked List    | A scavenger hunt (each item points to the next)|
| Stack          | A stack of plates / browser back button        |
| Queue          | A line at the supermarket                      |
| Hash Table     | A library with a perfect catalog (instant lookup)|
| Tree           | Family tree / company org chart                |
| Graph          | Road map / social network connections          |
| Heap           | A priority hospital triage list                |

---

## 9. How to Choose a Data Structure

Ask yourself these questions (inspired by both books):

1. Do I need **fast access by index**? → Array
2. Do I need **fast insert/delete** in the middle? → Linked List
3. Do I need **LIFO** behavior? → Stack
4. Do I need **FIFO** behavior? → Queue
5. Do I need **very fast lookups by key**? → Hash Table
6. Do I need **ordered data** or range queries? → Balanced Tree / Sorted Array
7. Do I need **priorities**? → Heap
8. Do I need to model **relationships**? → Graph

**Most important rule**:  
Start with the simplest structure that meets your requirements. Optimize only when you have measured a real bottleneck.

---

## 10. Common Interview Questions on Data Structures Intro

1. What is a data structure? Why do we need different ones?
2. Explain the difference between an array and a linked list.
3. What is the difference between a static array and a dynamic array?
4. What does “amortized O(1)” mean for dynamic array append?
5. When would you choose a linked list over an array?
6. What is an Abstract Data Type (ADT)?
7. Name the main operations we analyze for every data structure.
8. Give real-life analogies for Stack, Queue, and Hash Table.
9. What is the time complexity of accessing an element in an array vs a linked list?
10. Why is contiguous memory important for arrays?

---

## 11. Popular LeetCode Problems That Rely on Understanding Data Structures

- Two Sum (Hash Table)
- Contains Duplicate (Hash Table / Set)
- Valid Anagram (Hash Table / Array)
- Group Anagrams (Hash Table)
- Best Time to Buy and Sell Stock (Array)
- Reverse Linked List
- Valid Parentheses (Stack)
- Implement Queue using Stacks
- Binary Tree Level Order Traversal (Queue + Tree)
- Number of Islands (Graph / DFS / BFS)

*(Only the names are listed — solutions are studied separately.)*

---

## 12. Key Takeaways

1. Data structures are tools. The right tool makes your program fast and clean.
2. Always analyze the **operations** you will perform most often.
3. Arrays are the foundation — master them first.
4. Hash Tables are the workhorse of modern software — learn them deeply.
5. Big O is the language we use to compare data structures.
6. Start simple. Measure. Then optimize.

---

*End of Data Structures Introduction Notes*  
*Next: Arrays*
