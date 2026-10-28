# Three Modes, One Function
```
Swap(a, b) 
{
    let t = a;
    a = b;
    b = t;
}
```

## Pass-By-Value
```
Statement   a   b   t   caller(x,y)
start       1   2   -   (1,2)
t = a       1   2   1   (1,2)
a = b       2   2   1   (1,2)
b = t       2   1   1   (1,2)
```
## Pass-By-Reference
```
Statement   a   b   t   caller(x,y)
start       1   2   -   (1,2)
t = a       1   2   1   (1,2)
a = b       2   2   1   (2,2)
b = t       2   1   1   (2,1)
```

## Pass-By-Value-Result
```
Statement   a   b   t   caller(x,y)
start       1   2   -   (1,2)
t = a       1   2   1   (1,2)
a = b       2   2   1   (1,2)
b = t       2   1   1   (1,2)
return      -   -   -   (2,1)
```

# Asymmetric Aliasing
```
p(x, y)
{
x = x + 1;
y = y + 1;
}

a = 10;

p(a, a)

Statement   reference   value-result x  value-result y
start       10          10              10
x = x + 1   11          11              10
y = y + 1   12          11              11
return      12          copy x => a;    final a = 11
                        copy y => a;
reference 12; value result 11

this is becasue reference use the same storage cell for both while value result has different copies of both to copy them back in the order of x and y.
```

# Closures and Capture
```
let makers = [];

for (i = 0; i < 3; i = i + 1)
{
    makers.push(func() {return i;});
}
```
All three closures would return 3 due to them capturing the same env that hold the var i, not just a copy. When it loop it ends with i equal 3, so all three closures would return 3. The static link let each closure get the env where i is stored.
To make closure return a different value in usilangs for loops it should create new binding for every i in the loop.