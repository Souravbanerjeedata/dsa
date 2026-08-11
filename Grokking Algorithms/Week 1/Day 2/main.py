# exercise 3.2 after i finished recursion topic. Suppose you accidentally write a recursive function that runs forever. As you saw, your computer allocates memory on the stack for each function call. What happens to the stack when your recursive function runs forever?

# Answer: When a recursive function runs forever (infinite recursion), the call stack keeps growing without ever shrinking.
# Here’s what happens step by step:

# Every recursive call pushes a new frame onto the call stack (it stores the function’s local variables, return address, etc.).
# Because the function never reaches a base case, it never returns.
# Therefore no stack frames are ever popped.
# The stack keeps getting taller and taller until it hits the memory limit allocated for the stack.
# At that point the program crashes with a stack overflow error.

# In short: The stack fills up completely and the program crashes. This is exactly why every recursive function needs a proper base case — without it, the computer will eventually run out of stack space.