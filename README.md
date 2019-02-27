# Interview_Prep
Collection of wonderful CS concepts and algorithms you will inevitably be asked asked about in an interview.

## Basics 
- Class: basic concept in OOP, bundles data type information with action
- Hierarchy: classes can have super and subclasses

## HTTP Methods
- GET: used to retrieve data, no other effect on the data
- POST: used to send data to the server (e.g. form)
- PUT: replaces current representation of resource (idempotent)
- DELETE: remove current representation resource

## HTTP Status Codes
- 200 OK: success
- 400 Bad Request: syntax could not be understood
- 401 Unauthorized: request not fulfilled due to lack of authorization
- 403 Forbidden: request understood but not fulfilled, authorization will not help
- 404 Not Found: URI could not be matched
- 408 Request Timeout: server did not receive a timely response from client
- 418 I'm a teapot: the resulting entity body may be short and stout
- 500 Internal Server Error: server exception
- 503 Service Unavailable: server unable to handle the request (temporary)
- 504 Gateway Timeout: server did not receive a timely response from upstream server

## UNIX
- Basic commands: ls, cd, mkdir,touch, cp, mv, rm, pwd, chmod, chown, man
- ping: ping a server, used for network diagnostics
- ps: display info about processes running on the system
- grep: searches through files for lines matching a given regular expression
- tar, zip, unzip: make and open compressed archives
- curl: send requests to web servers
- wget: download files from the web (can do recursively)
- dig: query over DNS
- crontab: use Cron to schedule recurring tasks

## Git
- init: creates/initializes .git folder in current directory
- clone: clone repo into new directory
- pull: fetch from another repo and integrate 
- add: add files to index of contents for next commit
- rm: remove files from working tree and index
- commit: record changes to the repo, along with a commit message
- rebase: transplant changes on one branch to another, edit commit history
- branch: list, create, or delete branches
- checkout: switch branches (or just get a version of specific files)
- status: show the working tree's status
- diff: show changes between commits or the working tree
- log: show commit logs in a repo
- remote: manage tracked remote repos
- reset: reset current HEAD to a different state (can do --hard or --soft)

# Object Oriented Programming (OOP)
##### *DRY: Dont Repeat Yourself!*

**Polymorphism** - one thing in many forms. Basically polymorphism is capability of one object to behave in multiple ways. Example : A man role changes at home, college, and outside the home.

Reference to a parent class to affect an object in the child class. We might create a class called “horse” by extending the “animal” class. That class might also implement the “professional racing” class. The “horse” class is “polymorphic,” since it inherits attributes of both the “animal” and “professional racing” class.

```Python
class Animal:
	def __init__(self, name):
		self.name = name
	
class Cat(Animal):
	def __init__(self):
		super().__init__(self)
		
	def talk(self):
		return ("meow")
		
class Dog(Animal):
	def talk(self):
        return ("ruff")
```

**Encapsulation** - a mechanism of binding the data member & member function into a single unit known as class. Encapsulation provides a way for abstraction. In OOP the encapsulation is mainly achieved by creating classes, the classes expose public methods and properties. The class is kind of a container or capsule or a cell, which encapsulate the set of methods, attribute and properties to provide its indented functionalities to other classes

For example, we may create a piece of code that calls specific data from a database. It may be useful to reuse that code with other databases or processes. Encapsulation lets us do that while keeping our original data private. It also lets us alter our original code without breaking it for others who have adopted it in the meantime.

```Python
class Car:
	def __init__(self):
		self.__update_software()
		
	def drive(self):
		print('driving')
		
	def __update_software(self):
		print('updating software')
		
c1 = Car()
c1.drive()

## OUTPUT : updating software \n driving 
## "__" means private variable 
```

**Inheritance** - lets programmers create new classes that share some of the attributes of existing classes. This lets us build on previous work without reinventing the wheel.

It works by letting a new class adopt the properties of another. We call the inheriting class a subclass or a child class. The original class is often called the parent. We use the keyword extends to define a new class that inherits properties from an old class


```python 
class Vehicle:
	def __init__(self, name, color):
		self.__name = name
		self.__color = color
	
	def getColor(self):
		return self.__color
		
	def getName(self):
		return self.__name
		
class Car(Vehicle):
	def __init__(self, name, color, make):
		super().__init__(name, color)
		self.__model = model
		
	def getDescription(self):
	        return self.getName() + self.__model + " in " + self.getColor() + " color"
	
		
c = Car("Toyota Corolla", "navy", "2015")
print(c.getDescription())
print(c.getName())

# Toyota Corolla2015 is navy in color
# Toyota Corolla
```

# Data Structures:

**Array:**  a collection with specified size 
```python
ar = [] #:)
```

**LinkedList:**  a collection of nodes where each node has a value and a reference
```python

class Link (object):
  def __init__ (self, data, next = None):
    self.data = data
    self.next = next
    
class LinkedList (object):
  def __init__ (self):
    self.first = None

  def insertFirst (self, data):
    newLink = Link (data)
    newLink.next = self.first
    self.first = newLink

  def insertLast (self, data):
    newLink = Link (data)
    current = self.first

    if (current == None):
      self.first = newLink
      return

    while (current.next != None):
      current = current.next

    current.next = newLink

  def findLink (self, data):
    current = self.first
    if (current == None):
      return None

    while (current.data != data):
      if (current.next == None):
        return None
      else:
        current = current.next

    return current

  def deleteLink (self, data):
    current = self.first
    previous = self.first

    if (current == None):
      return None

    while (current.data != data):
      if (current.next == None):
        return None
      else:
        previous = current
	current = current.next

    if (current == self.first):
      self.first = self.first.next
    else:
      previous.next = current.next

    return current
    ```

**Stack:** last in, first out (LIFO) 
```python
class Stack (object):
  def __init__ (self):
    self.stack = []

  def push (self, item):
    self.stack.insert (0, item )

  def pop (self):
    return self.stack.pop(0)

  def peek (self):
    return self.stack[0]

  def isEmpty (self):
    return (len(self.stack) == 0)

  def size (self):
    return (len(self.stack))```

**Queue:** first in, first out (FIFO) 
```python
class Queue (object):
  def __init__ (self):
    self.queue = []

  def enqueue (self, item):
    self.queue.append (item)

  def dequeue (self):
    return (self.queue.pop(0))

  def isEmpty (self):
    return (len (self.queue) == 0)

  def size (self):
    return len (self.queue)```

**Tree:** an undirected, connected, acyclic graph 

**Hashing:** a function mapping an object to an integer such that if a==b, H(a)==H(b)

**Heap:** a special tree where nodes have higher (in the case of a min-heap) values than their parents

**Graph:** a collection of nodes and edges and can be directed or undirected

# Algorithms:

**Binary Search:**

**Insertion Sort:**

**Bubble Sort:**

**Selection Sort:**

**Merge Sort:**

**Quick Sort:**

**Bucket Sort:**

**Graph - DepthFirstSearch:**

**Graph - BreadthFirstSearch:**

**Graph - Dijkstra'sAlgorithmSearch:**

**Brute Force:**

**Greedy:** 

**Dynamic Programming:**

## Questions? 
-  “Thinking back to people you’ve seen do this work previously, what differentiated the ones who were good from the ones who were really great at it?”
-  “What do you like about working here?” 


