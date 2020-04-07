## Primitive Data Types:
- byte      
- short
- boolean
- char
- int       
- long      
- double
- float

Simple type casting:
```java
System.out.println((int)(99.9999)); // Prints 99
```

int vs Integer: int is a primitive data type in java - Integer is a wrapper class, that wraps around int to create an object. Integer is used in converting an int to an object, an object into an int. 

Wrapper classes provide a way to use primitive data types (int, boolean, etc..) as objects.
```java
int twentyInt = Integer.parseInt("20"); 
```

2d Lists:
```java
List<List<String>> listOfLists = new ArrayList<List<String>>(size);
```

ArrayLists:
```java
List<String> cars = new ArrayList<String>();
cars.add("Volvo");
System.out.prinln(cars.get(0));
```
Vector is the thread-safe version of ArrayList.

HashMap:
```java
HashMap<String, Integer> wordCount = new HashMap<String, Integer>();
wordCount.put("Like", "100");
int likeValue = wordCount.get("Like");

// Iterate through hashMap
for (String i : wordCount.keySet()) {
      System.out.println(i);
}
```

Set:
```java
Set<Integer> a = new HashSet<Integer>();
Set<Integer> b = new HashSet<Integer>();
a.addAll(Arrays.asList(new Integer[] {1, 3, 2, 4, 8, 9, 0}));
b.addAll(Arrays.asList(new Integer[] {1, 3, 7, 5, 4, 0, 7, 5}));

// To find union 
Set<Integer> union = new HashSet<Integer>(a); 
union.addAll(b); 
System.out.print("Union of the two Set"); 
System.out.println(union); 

// To find intersection 
Set<Integer> intersection = new HashSet<Integer>(a); 
intersection.retainAll(b); 
System.out.print("Intersection of the two Set"); 
System.out.println(intersection); 

// To find the symmetric difference 
Set<Integer> difference = new HashSet<Integer>(a); 
difference.removeAll(b); 
System.out.print("Difference of the two Set"); 
System.out.println(difference);
```

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

## Abstract

- An abstract class is a class that is declared abstract—it may or may not include abstract methods. Abstract classes cannot be instantiated, but they can be subclassed
- When an abstract class is subclassed, the subclass usually provides implementations for all of the abstract methods in its parent class. However, if it does not, then the subclass must also be declared abstract.
- Ensures child classes implement a method. Enforces Inheritance. Enforces method overriding.
- If a class includes abstract methods, then the class itself must be declared abstract, as in:
```java
abstract class GraphicObject {
    int x, y;
    ...
    void moveTo(int newX, int newY) {
        ...
    }
    abstract void draw();
    abstract void resize();
}

class Circle extends GraphicObject {
    void draw() {
        ...
    }
    void resize() {
        ...
    }
}

class Rectangle extends GraphicObject {
    void draw() {
        ...
    }
    void resize() {
        ...
    }
}
```

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

## Abstract Classes Compared to Interfaces
Abstract classes are similar to interfaces. You cannot instantiate them, and they may contain a mix of methods declared with or without an implementation. However, with abstract classes, you can declare fields that are not static and final, and define public, protected, and private concrete methods. With interfaces, all fields are automatically public, static, and final, and all methods that you declare or define (as default methods) are public. In addition, you can extend only one class, whether or not it is abstract, whereas you can implement any number of interfaces.
Which should you use, abstract classes or interfaces?
Consider using abstract classes if any of these statements apply to your situation: 
You want to share code among several closely related classes.
You expect that classes that extend your abstract class have many common methods or fields, or require access modifiers other than public (such as protected and private).
You want to declare non-static or non-final fields. This enables you to define methods that can access and modify the state of the object to which they belong.
Consider using interfaces if any of these statements apply to your situation: 
You expect that unrelated classes would implement your interface. For example, the interfaces Comparable and Cloneable are implemented by many unrelated classes.
You want to specify the behavior of a particular data type, but not concerned about who implements its behavior.
You want to take advantage of multiple inheritance of type

## Memory in Java

** Fill this in **

## Garbage collection
- Main objective of Garbage Collector is to free heap memory by destroying unreachable objects.
- An object is said to be eligible for GC(garbage collection) iff it is unreachable. In above image, after i = null; integer object 4 in heap area is eligible for garbage collection.


## Testing in Java

** Fill this in ** 

junit, mockito, etc

## Strings

#### **String objects are immutable in java!**
- use == to compare primitive e.g. boolean, int, char etc, while use equals() to compare objects in Java. 
- == return true if two references are of the same object. The result of equals() method depends on overridden implementation. 
- For comparing the content of two Strings use equals() instead of == equality operator. 
- Create string literals rather than new objects (String newStringObj = new String()) <- bad
    - String newStringLiteral = "yo"; <- good. JVM wont create an entirely new reference if another "yo" is created.
- Using equalsIgnoreCase() is faster than using toUpperCase() or toLowerCase().equals()

#### StringBuffer vs StringBuilder
StringBuffer is synchronized i.e. thread safe. It means two threads can't call the methods of StringBuffer simultaneously.
StringBuilder is non-synchronized i.e. not thread safe. It means two threads can call the methods of StringBuilder simultaneously.
StringBuffer is less efficient than StringBuilder.
StringBuilder is more efficient than StringBuffer

```java
String demoString = "yo";
int demoStringLength = demoString.length();
```

## Collections
[Good Explanation](https://www.javatpoint.com/collections-in-java)

## Streams

## Acronyms 
- JPA: Java Persistence API
- JVM: Java Virtual Machine
- MVC: Model-View-Controller
    -  Design pattern for relating the user interface to underlying data models.
- ORM: Object Relational Mapping
    - Maps classes to DB tables
    - Maps instance variables to columns
    - Maps objects to rows in the table
    - DB independent
