# Static vs. Dynamic Scoping
Static Scoping looks for where the var is defined in the source code. While Dynamic Scoping is where var is called during runtime.
Python use static Scoping, and bash uses dynamic scoping when local is not used.
Static scoping is easier to predict becasue you can find what the var refers to just by reading the source code. While with dynamic scoping, the variable depends on what function was called before it. Due to this you would need to know the full history at runtime to find which vaiable it refers to. So this means static scoping is easier to use in a larger codebase because you wouldn't need to trace the whole program just to know what a variable means.

# The Classic Divergence, Traced
## Lexical Nesting diagram static
```Rust
Global Scope
|---x = 10
|---A
|   |
|   ---local x = 1
|   
|---B
    |
    ---Print(x)
B is declared in global scope, and the lexical parent is the global scope.
So, B will print x = 10
```

## Call Stack - Dynamic Scoping
```Rust
A
|---local x = 1
|---calls B
    |---B
        |---print(x)
B get called inside of A, so during dynamic scoping, B will find the A local x = 1
So, B will print x = 1
```
The two strategies does diverge: Static prints 10, while dynamic prints 1.

# Scope Holes
Scope hole is when the nested(inner) variable has the same name as the variable outside(outer). The innver variable with the same name hide the variable outside. Even tho the outer variable is still in the scope but it can't be accessed by using the same name inside the inner scope.
```
global x = 40

process A():
    x = 90

    process B(x):
        print(x)
    
    call B(1)

This will print 1
```

# Dynamic Scoping and Shared State
Dynamic Scoping can be dangerous in a interpreter because it finds names by walking through shared call stack. 2 thread can be pushing an popping in the same stack frames at the same time. One of the threads can change while the other thread is trying to look up a variable. This could make the lookup to the wrong variable value