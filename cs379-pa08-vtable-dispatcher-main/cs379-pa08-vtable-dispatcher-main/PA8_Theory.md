# Building the Table
```rust
Class Animal {
    func speak() 
    {
        return "...";
    }

    func name()
    {
        return "Animal";
    }
}

Class Dog extends Animal{
    func speak()
    {
        return "Woof";
    }
}

Class Puppy extends Dog {
    func name()
    {
        return "Puppy";
    }
}

RunTime Class   |   Speak Slot  |   Name Slot   |   Unchanged inheritance
Animal          |   Animal.speak|   Animal.name |   _____________________
Dog             |   Dog.speak   |   Animal.name |   name from animal stay unchanged
Puppy           |   Dog.speak   |   Puppy.name  |   speak from dog stay unchanged

Animal VTable:
[0] Animal.speak
[1] Animal.name

Dog VTable:
[0] Dog.speak       override
[1] Animal.name     inherited from Animal

Puppy VTable:
[0] Dog.speak       inherited from Dog
[1] Puppy.name      override
```

# Static vs. Dynamic Dispatch
``` R
Animal a = Puppy();
a.speak();
```
**Static dispatch:** It would call Animal.speak() due to the declared variable being Animal\
**Dynamic dispatch:** It would call Dog.speak() due to the actual obj is a puppy, which speak would be inherited from the dog class.

Using the part 1 Vtable, the dynamic call points to slot 1 which is [0] of the puppy vtable. Which is Dog.speak(). The static answer for dynamic would be wrong because static select Animal.speak() based on declared type.

# Polymorphism Trace
`[Animal(), Dog(), Puppy()]`
```
Animal a = Animal()
Animal b = Dog()
Animal c = Puppy()

a.name()
b.name()
c.name()

a.name() -> Animal VTable   ->  [1] ->  Animal.name()   ->  "Animal"
b.name() -> Dog VTable      ->  [1] ->  Animal.name()   ->  "Animal"
c.name() -> Puppy VTable    ->  [1] ->  Puppy.name()    ->  "Puppy"
```