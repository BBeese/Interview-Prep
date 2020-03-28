## Basics 
- SDLC (Software Development Life Cycle): design, develop, test high quality software
    + Planning -> Defining -> Designing -> Building -> Testing -> Deployment
- AGILE : Rapid delivery of a working product, small incremental builds
- C++ is a *low* level languages, Python high
  + Low level languages are close to machine language. Generally more efficient
  + High level languages are easier to understand; more abstraction. More portable
- A *Compiler* generates an executable (.exe) 
- OOP: Objects contain variables and methods to store and compute data, and a constructor for initialization purposes. 
  They can be bound by encapsulation and information hiding to prevent data leaks and can be implemented in other objects with inheritance.
  Polymorphism can be used to overwrite variables and methods and abstraction can be used to template future instances.
  + Class: basic concept in OOP, bundles data type information with action
  + Hierarchy: classes can have super and subclasses
  + An *Object* is an instance of a *Class*
  
## Databases 
- ORM vs ODM - Object Relational Mapper vs Object Document Mapper
- SQL vs noSQL (non SQL) databases - MongoDB uses objects, non-relational database
	- Relational databases use relations (typically called tables) to store data and then match that data by using common characteristics within the dataset
	- All noSQL documents are JSON documents, which are complete entities that one can readily read and understand. Ease of use, scalable, wide availability. 
  
  
## SQL
- Unique Key (FK): Column/Group of columns that identify uniqueness in a row
- Primary Key (PK) : a unique key, but there can be only one primary key
- Foreign Key (FK) : Provides an association between data and 2 tables
- Outer Join (Left, Right), Inner Join

### Order of execution:
  1) FROM
  2) JOIN
  3) WHERE
  4) GROUP BY
  5) HAVING
  6) SELECT 
  7) DISTINCT 
  8) ORDER

## HTTP
### Methods
- GET: used to retrieve data, no other effect on the data
- POST: used to send data to the server (e.g. form)
- PUT: replaces current representation of resource (idempotent)
- DELETE: remove current representation resource

### Status Codes
- 200 OK: success
- 400 Bad Request: syntax could not be understood
- 401 Unauthorized: request not fulfilled due to lack of authorization
- 403 Forbidden: request understood but not fulfilled, authorization will not help
- 404 Not Found: URI could not be matched
- 408 Request Timeout: server did not receive a timely response from client
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

**Encapsulation** - a mechanism of binding the data and methods into a single unit known as class. Encapsulation provides a way for abstraction. In OOP the encapsulation is mainly achieved by creating classes, the classes expose public methods and properties. The class is kind of a container or capsule or a cell, which encapsulate the set of methods, attribute and properties to provide its indented functionalities to other classes

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

**Abstraction** - Abstraction means using simple things to represent complexity. We all know how to turn the TV on, but we don’t need to know how it works in order to enjoy it. In Java, abstraction means simple things like objects, classes, and variables represent more complex underlying code and data. This is important because it lets avoid repeating the same work multiple times.

	Abstraction as an OOP concept in Java works by letting programmers create useful, reusable tools. For example, a programmer can create several different types of objects. These can be variables, functions, or data structures. Programmers can also create different classes of objects. These are ways to define the objects.
	Consider your mobile phone, you just need to know what buttons are to be pressed to send a message or make a call, What happens when you press a button, how your messages are sent, how your calls are connected is all abstracted away from the user.

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
ar = [] #better never forget this 
```

**Hashing:** a function mapping an object to an integer such that if a==b, H(a)==H(b). A dictionary in python 
```python
d = {} #better never forget this either 
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
    self.stack.insert (0, item)

  def pop (self):
    return self.stack.pop(0)

  def peek (self):
    return self.stack[0]

  def isEmpty (self):
    return (len(self.stack) == 0)

  def size (self):
    return (len(self.stack))
```

**Queue:** first in, first out (FIFO) 
```python
class Queue (object):
  def __init__ (self):
    self.queue = []

  def enqueue (self, item):
    self.queue.append(item)

  # Removes last element
  def dequeue (self):
    return (self.queue.pop(0))

  def isEmpty (self):
    return (len (self.queue) == 0)

  def size (self):
    return len (self.queue)
 ```

**BST (Binary Search Tree):** nodes connected by edges. Left node smaller than right. A node with no child is typically called a leaf node. [Twitter username validation]
```python
class Node (object):
  def __init__ (self, data):
    self.data = data
    self.left = None
    self.right = None
    
class Tree (object):
  def __init__ (self):
    self.root = None
    
  def insert(self, data):
    new_node = Node (data)
    if (self.root == None):
      self.root = new_node
    else:
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
        if (data == current.data):
          return
        elif (data < current.data):
          current = current.left
        else:
          current = current.right
      if (data < parent.data):
        parent.left = new_node
      else:
        parent.right = new_node
	
  # the search() function will search for a character in the binary
  # search tree and return a string containing a series of lefts
  # (<) and rights (>) needed to reach that character. It will
  # return a blank string if the character does not exist in the tree.
  # It will return * if the character is the root of the tree.
  
  def search (self, data):
    output = ''
    current = self.root
    if (self.root.data == data):
      return '*'
    while (current != None):
      if (current.data == data):
          return output
      elif (data < current.data):
        current = current.left
        output += '<'
      else:
        current = current.right
        output += '>'

    return output
    
def num_nodes(self, node):
  if node == None:
    return 0
  else:
    return 1 + num_nodes(self, node.left) + num_nodes(self, node.right)
    
def get_height(self, node):
  if node == None:
    return 0
  else:
    return 1 + max(num_nodes(self, node.left) + num_nodes(self, node.right))
```

**Heap:** A special tree structure in which each parent node is less than or equal to its child node. Then it is called a Min Heap. If each parent node is greater than or equal to its child node then it is called a max heap. It is very useful is implementing priority queues where the queue item with higher weightage is given more priority in processing.

**Graph:** A collection of nodes and edges and can be directed or undirected.

# Algorithms:

**Insertion Sort:** Compare each element with the previous element, 'insert' element in previous position until it is in correct order. 

**Bubble Sort:** NOT efficient. Iterate through list, swap numbers if i < i+1, until all sorted. 
[6, 7, 8, 9, 2, 1, 5] -> [6, 7, 8, 2, 1, 5, 9]
9 'bubbles' to the top.

**Selection Sort:** Scan entire UNSORTED portion of the array until minimum value is found, then move this value to the front. 

**Merge Sort:** Efficient. Partition array until each number in own array, merge each partition until entire array is sorted.

**Quick Sort:** Efficient. Pick pivot element, ensure all elements before pivot < the pivot, all elements to right > pivot. Swapping elements on each side of pivot.

**Bucket Sort:** Buckets are created to put elements inside, then insertion sort applied on each bucket. Basically a stem and leaf plot, then sort merge each bucket together.

**Binary Search:** If num im searching for is < midpoint, binary search on left side. else, right.
[1, 2, 3, 4, 5, 6, 7], Search for 2. Next iteration:
[1, 2, 3]

**BreadthFirstSearch:** - Or, "Level-Order Traversal", row based search. Horizontal. QUEUE.
```python
def bfs(root):
  if root == None:
    return
  
  q = Queue()
  q.enque(root)
  payload = []

  while not (q.isEmpty):
    node = q.deque()
    payload.insert(0, node.value)
    if node.left: 
      q.enque(node.left)
    elif node.right():
      q.enque(node.right)

```

### When to use:
- When you need to find the shortest path between any two nodes in an unweighted graph.
- If you're solving a problem, and know a solution is not far from the root of the tree, BFS will likely get you there faster.
- If the tree is very deep, BFS might be faster

**DepthFirstSearch:** - Visits nodes starting from leaves, or from root. Vertical. STACK.

```python
# Inorder traversal (DFS Traversal)
# Left -> Root -> Right [L > N > R]
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res
	
# Preorder traversal (DFS Traversal)
# Root -> Left ->Right [N > L > R]
    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res
	
# Postorder traversal (DFS Traversal)
# Left -> Right -> Root [L > R > N]
    def PostorderTraversal(self, root):
        res = []
        if root:
            res = self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.data)
        return res
```

### When to use:
- DFS is more space efficient than BFS.
- If the tree is very wide, BFS will likely be incredibly memory inefficient, so DFS could be better.

**Dijkstra's Algorithm:** [Weighted Graph] Minimum distance from one node to all other nodes. 
Given graph g, list of all vertices allVertices, list of all edges edges, starting vertex startVertex ->

1. Set array vertexDistances = {}; distances from startVertex to all other vertices
2. Set array unvisitedVertices = []  
3. For every vertex v in allVertices, set vertexDistances[v] = infinity
4. For every vertex v in allVertices, add v to unvisitedVertices
5. Set vertexDistances[startVertex] = 0
6. Update vertexDistance[adjacent vertices of startNode] = weight(startVertex, adjVertex)
7. If unvisitedVertices is not empty, select v from unvisitedVertices with SMALLEST vertexDistance value
8. For every adjacent vertex n of v, such that n is in unvisitedVertex:
  - Let a = vertexDistances[n] + weight(v, n). weight(x, y) is the edge weight from vertex x to vertex y.
9. if a < vertexDistance[n], set vertexDistance[n] = a. 
10. Repeat step 6 until unvisitedVertices is empty.  

**Brute Force:**

**Greedy:** 

**Divide & Conquor** 

**Dynamic Programming:**

## Questions to ask Interviewer 
-  Mentorship? Onboarding? 
-  What does a typical day look like?
-  Can you tell me about the team I'll be working with?
-  What do you personally like about working here?

## Behavioral questions 
- Tell me about yourself.
- **Why do you want to for for X?**
- What is a time you had a conflict with a team member, and how did you resolve it?
- Tell me about a time when you solved a conflict at work.
- What is your greatest strength?
- What is your greatest weakness?
- **What are your goals?**
- What was a challenge you had to overcome?
- Describe a time where you have failed, and what you learned from it
- What are you actively trying to improve on?
- **Why are you switching jobs?**
- Where do you see yourself in 5 years? 
- Tell me about a time you made a mistake and how did you resolve it?
- Tell me about something you did at work you are proud of?

# Things to work on: 
- map, reduce, filter in python
- cloud with python 
- refresh data structures & algos
- maybe another python project. Crypto? Stocks? Election data? Weather across the states? "Only in texas/midwest/florida/literallyeverywhere can you experience all 4 seasons in one day" data project to prove weather is unpredictable everywhere
- refresh Java

# External resources and sources:
- [Tons of interview questions, specific to language/frameworks](https://www.onlineinterviewquestions.com/programming/)
- [System design resources](https://github.com/donnemartin/system-design-primer)
- [reddit CS interview guide](https://www.reddit.com/r/cscareerquestions/comments/1jov24/heres_how_to_prepare_for_tech_interviews/)
- [reddit free study resources](https://www.reddit.com/r/cscareerquestions/comments/e4v755/master_list_of_free_resources/)
- [bfs vs dfs](https://www.geeksforgeeks.org/bfs-vs-dfs-binary-tree/)
- [basic graphs](https://www.bogotobogo.com/python/python_graph_data_structures.php)
- [sorting](https://www.youtube.com/playlist?list=PL9xmBV_5YoZOZSbGAXAPIq1BeUf4j20pl)
- [dijkstras](https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/)
