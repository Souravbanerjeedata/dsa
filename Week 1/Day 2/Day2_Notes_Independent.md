# Grokking Algorithms – Day 2 Notes
**Chapter 3 – Recursion**  
*Independent version – written without reference to any practice file*

---

## 1. What is Recursion?

Recursion is when a function calls itself.

It is an alternative way to solve problems that can also be solved with loops.  
Some problems become much clearer when written recursively.

Every recursive function has two parts:

1. **Base case** – the condition that stops the recursion  
2. **Recursive case** – the part where the function calls itself

Without a base case, the function will call itself forever and crash.

---

## 2. Base Case vs Recursive Case

**Base case**  
The simplest possible input. When the function reaches this, it returns a value and stops calling itself.

**Recursive case**  
The function calls itself with a smaller or simpler version of the original problem.

Example – Countdown:

```python
def countdown(i):
    print(i)
    if i <= 1:          # Base case
        return
    else:               # Recursive case
        countdown(i - 1)
```

---

## 3. The Call Stack

When you call a function, the computer uses a stack (the **call stack**) to keep track of function calls.

- Each time a function is called, a new frame is pushed onto the stack.
- The frame stores the function’s variables and the place to return to.
- When the function finishes, its frame is popped off the stack.

With recursion the same thing happens, but the stack grows deeper because the function keeps calling itself.

### Visual example (factorial of 3)

```
factorial(3)
  → factorial(2)
      → factorial(1)   ← base case returns 1
      ← returns 2 * 1
  ← returns 3 * 2
```

The stack grows as we go deeper, then shrinks as the calls return.

---

## 4. Factorial (Classic Recursive Example)

```python
def fact(x):
    if x == 1:          # Base case
        return 1
    else:               # Recursive case
        return x * fact(x - 1)
```

How it runs for `fact(3)`:

1. `fact(3)` → needs `3 * fact(2)`
2. `fact(2)` → needs `2 * fact(1)`
3. `fact(1)` → returns `1` (base case)
4. `fact(2)` returns `2 * 1 = 2`
5. `fact(3)` returns `3 * 2 = 6`

---

## 5. Infinite Recursion & Stack Overflow

If you forget the base case (or write a bad one), the function never stops calling itself.

Every call adds a new frame to the stack.  
The stack keeps growing until it runs out of memory → **stack overflow**.

This is exactly what Exercise 3.2 asks:

> Suppose you accidentally write a recursive function that runs forever.  
> What happens to the stack?

**Answer:** The stack fills up completely and the program crashes with a stack overflow error.

---

## 6. When to Use Recursion

- The problem can be broken into smaller identical sub-problems.
- The recursive version is clearer and easier to understand than the loop version.
- You are working with tree-like or nested structures (later chapters).

Recursion is not always the fastest or most memory-efficient choice, but it often makes the code much cleaner.

---

## Day 2 Recap

- Recursion = function calling itself.
- Always need a **base case** and a **recursive case**.
- The call stack tracks every function call.
- Infinite recursion → stack overflow.
- Factorial is the classic simple example of recursion.

---

*Notes based solely on Grokking Algorithms, Chapter 3 – Recursion.*
