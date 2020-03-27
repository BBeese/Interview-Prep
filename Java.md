[ Need to add - Super, ArrayList vs Vector, StringBuffer vs StringBuilder,

## Primitive Data Types:
- Byte      
- Short
- Boolean
- Char
- Int       
- Long      
- Double
- Float

Non-primitive data types do not explicitly contain the value, instead is just a reference (Kind of like a pointer)

## Access Specifiers
**Add some extra clarification here**
1. Public - Accessible everywhere
2. Protected - Accessible inside some packages, subclasses
3. Default - Accessible inside same package
4. Private - Accessible only inside same class  

Used like an access specifier: Final - Used when a class/variable/method should not be modified or extended. 


## Arrays
**IMMUTABLE IN JAVA!!**

int[] nums = {1, 2, 3, 4, 5}

# Classes

```java

class Product {

    public static int idCounter = 1000

    public Product(String name, float price) {
        this.id = this.idCounter + 1
        this.name = name
        this.price = price
        Product.idCounter++
    }

    public float getStock() {
        return this.stock;
    }

    public void setStock(int stock) {
        this.stock = stock;
    }

}

```

#### Create new object:
```java
Product product1 = new Product();
```

- A **static** variable is shared by all instances of the class
- An **instance** variable is unique to each instance of the class

## Method overloading
Two or more methods with the same name. 

Can have the same method name for multiple methods, if different number of parameters, different types of parameters. Constructor overloading is possible as well. 

```java
public void demoOverloading() {
    System.out.println("this is before being overloaded");
}
public void demoOverloading("yello") {
    System.out.println("after being overloaded");
}
```

Different from 'Method Overriding'; 
```java
@Override
public float addProduct(Product[] products) {
    System.out.println("overroad (overrided?) this method rn");
}
```

## Abtract

- Ensures child classes implement a method. Enforces Inheritance. Enforces method overriding.
**Fill this in**

## Interface
- Blueprint of a class. Only contains method signatures. (No body!)
- Used to achieve total abstraction
- Enforces standard rules or contracts. Specifies WHAT, not HOW

```java
interface x {
    void display();
}

class y implements x {
    public void display() {
        System.out.println("yeet");
    }
}
```

## Memory in Java

** Fill this in **

## Testing in Java

** Fill this in ** 

junit, mockito, etc

## String methods

**Strings are immutable in java!**

Just look these up im not listing them all 

```java
String demoString = "yo";
int demoStringLength = demoString.length();
```

## Collections; Listiterator, arraylist, Map

## Set, Hashset, Treeset (Maybe)

## Streams
