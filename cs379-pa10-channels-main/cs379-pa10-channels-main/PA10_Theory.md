# Bounded Buffer Trace
```Rust
Start       [ , ]   empty buffer
P.put(1)    [1, ]   insert 1
P.put(2)    [1,2]   insert 2
P.put(3)    [1,2]   blocked no empty space, attemped to insert 3 <----
C.get()     [2, ]   get first value
P.put(3)    [2,3]   put(3) complete <----
C.get()     [3, ]   get first value
```

# Deadlock by Design
```cpp 
Thread 1: ch_a.get() is blocked
Waiting for a item in ch_a

Thread 2: ch_b.get() is blocked
Waiting for a item in ch_b

ch_b.put(ch_a.get()) T1 waiting for T2 to put an item into ch_a
ch_a.put(ch_b.get()) T2 waiting for T1 to put an item into ch_b

both are waiting for one and another which cause a deadlock

Fix:
have a value in ch_a before starting the Threads. T1 wont get stuck waiting it would get the value and put it into b then
T2 start get the value from b and put it in a
This will break the deadlock because neither thread is stuck waiting
```

# Bounded vs. Unbounded, and the GC Connection
A unbounded channel does not have a fixed cap limit so put() is never blocked. The producer can keep adding to the channel even when the consumer is not removing them.\
In PA9 the GCHeap uses ref counting to see when a obj can be collected. The obj can be collected when the ref count hit zero.\
The producer can keep adding obj while the consumer is too slow, the channel buffer will keep growing. the buffers still hold ref to those obj, making the count stay above zero. Overtime the program can use too much memory and eventually it will run out of memory.