# Recursive Trace
Function Name
Value of N
return address
Dynamic link
Static Link
``` rust
1 func factorial(n) {
2     if (n <= 1) { return 1;}
3     return n * factorial(n - 1);
4 }
5 call factorial(4);

factorial(1)
n = 1
Return at line 3
Dynamic Link: factorial(2)
Static Link: Global Scope
factorial(2)
n = 2
Return at line 3
Dynamic Link: factorial(3)
Static Link: Global Scope
factorial(3)
n = 3
Return at line 3
Dynamic Link: factorial(4)
Static Link: Global Scope
factorial(4)
n = 4
Return at line 5
Dynamic Link: Global Caller
Static Link: Global Scope
```
## Stack Unwinding
```
Starting Stack
TOP
factorial(1)
factorial(2)
factorial(3)
factorial(4)
BOTTOM

return 1: factorial(1): out: 1
TOP
factorial(2)
factorial(3)
factorial(4)
BOTTOM

return 2: factorial(2): out: 2
TOP
factorial(3)
factorial(4)
BOTTOM

return 3: factorial(3): out: 6
TOP
factorial(4)
BOTTOM

return 4: factorial(4): out: 24
TOP
EMPTY STACK
BOTTOM
```

# Static Link vs. Dynamic Link
```rust
func One(){
    func Two(){
        print("in Two");
    }
    func Three(){
        call Two();
    }

    call Three();
}
call One();
Call: One() => Three() => Two()
Two() runs: Dynamic link: Three()
Static link: One()
```
Static links are needed because dynamic links can only show which function call which. Static links can help the function to access var in the scope where it was defined. 

# Stact Overflow
S = fixed stack size\
R = fixed activation record size\
D = recursion depth\
DR <= S

Maximum safe depth\
D <= (S/R)\
Tail recusrsion can cause a stack overflow in the interpreter due to the recursive call making new activation record. A compiler avoid stack overflow by reusing the current activation record instead of making a new one.