## Basics 
- Agile : Rapid delivery of a working product, small incremental builds. Useful for rapidly changing requirements
- Waterfall: Linear, old methodology. Plan -> Design -> Build -> Test -> Deliver
- C++ is a *low* level languages, Python high
  + Low level languages are close to machine language. Generally more efficient
  + High level languages are easier to understand; more abstraction. More portable
- A *Compiler* generates an executable (.exe) 
- OOP: Objects contain variables and methods to store and compute data, and a constructor for initialization purposes. based on objects rather than just functions and procedures
  + Class: basic concept in OOP, bundles data type information with action
  + Hierarchy: classes can have super and subclasses
  + An *Object* is an instance of a *Class*
  + Why use OOP? 
    + Reduces complexity
    + Reduces redundancy (Inheritance)
    + Flexibility (Polymorphism)
- Functional/Procedural programming - useful when there are few *things* but more operations. 'State' does not exist.
  - OOP useful when there are more things, with less operations. State exists.
  
## Databases 
- ORM vs ODM - Object Relational Mapper vs Object Document Mapper
- SQL vs noSQL (non SQL) databases - MongoDB uses objects, non-relational database
	- Relational databases use relations (typically called tables) to store data and then match that data by using common characteristics within the dataset
	- All noSQL documents are JSON documents, which are complete entities that one can readily read and understand. Ease of use, scalable, wide availability.
    - Flexible, no forced schemas
    - Highly scalable, noSQL systems tend to have less features and are better performing and lightweight

### DB concepts
- ACID: Atomocity, Consistency, Isolation, Durability
- BASE: Basically Available, Soft-state, Eventual consistency
  
## SQL
- Primary Key (PK) : a unique key, but there can be only one primary key
- Unique Key (FK): Column/Group of columns that identify uniqueness in a row
- Foreign Key (FK) : Provides an association between data and 2 tables
  Field that is a PK in another table.
- Outer Join (Left, Right), Inner Join, Cross Join (Cartesian product; 1-4, 1-5, 1-6, 2-4, 2-5, 2-6, 3-4, 3-5, 3-6)

### Order of execution:
  1) FROM
  2) JOIN
  3) WHERE
  4) GROUP BY
  5) HAVING
  6) SELECT 
  7) DISTINCT 
  8) ORDER

#### SQL Injection
- Concept of giving an executable SQL statement inside an unsuspecting form (Username, Email) that will be ran by the underlying database.


## HTTP (HyperText Transfer Protocol)
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

Web service - Component for communication between two devices on a network (client - server)
API - Application Programming Interface
RESTful - Representational State Transfer technology 
  - Make call (http request) from client to server, get an answer (http response) from server
  - REST is a way to access resources which lie in a particular environment. For example, you could have a server that could be hosting important documents or pictures or videos. All of these are an example of resources. If a client, say a web browser needs any of these resources, it has to send a request to the server to access these resources. Now REST defines a way on how these resources can be accessed
    - Stateless
      - Up to the client to ensure that all the required information is provided to the server. This is required so that server can process the response appropriately. The server should not maintain any sort of information between requests from the client. It's a very simple independent question-answer sequence. The client asks a question, the server answers it appropriately. The client will ask another question. The server will not remember the previous question-answer scenario and will need to answer the new question independently

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

## Best Practices 
**DRY (Don’t Repeat Yourself)** - Should never have two blocks of identical code in two different places. Instead, have one method you use for different applications.
If you expect your Java code to change in the future, encapsulate it by making all variables and methods private at the outset. As the code changes, increase access to “protected” as needed, but not too public.
**Single Responsibility Principle** -  Simply put, a class should always have only one functionality. That way, it can be called and/or extended on its own when new uses arise for it, without causing coupling between different functionalities.
**Open Closed Design** - Make all methods and classes closed for modification but open for an extension. That way, tried and tested code can remain static but can be modified to perform new tasks as needed.

- Super - reference parent class methods/attributes

**Polymorphism** - One thing in many forms. Basically polymorphism is capability of one object to behave in multiple ways.
  - Method Overloading: Same method name, different parameters, method behaves differently based on input.
  - Method Overriding: Redefining the method in a child class. Overwriting previously defined method. 

```Python
class Animal:
	...
	
class Cat(Animal):
	def talk(self):
		return ("meow")
		
class Dog(Animal):
	def talk(self):
    return ("ruff")
```

**Encapsulation** - Encapsulation refers to binding the data and the code that works on that together in a single unit. Encapsulation also allows data-hiding as the data specified in one class is hidden from other classes. This data is only accessible through public methods. (Getters/Setters) Keeps data secure.

For example, we may create a piece of code that calls specific data from a database. It may be useful to reuse that code with other databases or processes. Encapsulation lets us do that while keeping our original data private. It also lets us alter our original code without breaking it for others who have adopted it in the meantime.

**Abstraction** - Abstraction means using simple things to represent complexity. We all know how to turn the TV on, but we don’t need to know how it works in order to enjoy it. In Java, abstraction means simple things like objects, classes, and variables represent more complex underlying code and data. This is important because it lets avoid repeating the same work multiple times. Consider your mobile phone, you just need to know what buttons are to be pressed to send a message or make a call, What happens when you press a button, how your messages are sent, how your calls are connected is all abstracted away from the user.

**Inheritance** - lets programmers create new classes that share some of the attributes of existing classes. This lets us build on previous work without reinventing the wheel. It works by letting a new class adopt the properties of another. We call the inheriting class a subclass or a child class. The original class is often called the parent. We use the keyword extends to define a new class that inherits properties from an old class.


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

**Aggregation** - Object contains another object as an attribute. 'HAS A' relationship
```java
{ 
  id: int
  name: String
  address: Address
}
```

**Association** - Object method uses another object. 'USES A' relationship
```java
  public int calculate(params) {
    BillCalculator b = new BillCalculator();
  }
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

## Sorting

**Insertion Sort:** Compare each element with the previous element, 'insert' element in previous position until it is in correct order. 

**Bubble Sort:** NOT efficient. Iterate through list, swap numbers if i < i+1, until all sorted. 
[6, 7, 8, 9, 2, 1, 5] -> [6, 7, 8, 2, 1, 5, 9]
9 'bubbles' to the top.

**Selection Sort:** Scan entire UNSORTED portion of the array until minimum value is found, then move this value to the front. 

**Merge Sort:** Efficient. Partition array until each number in own array, merge each partition until entire array is sorted.

**Quick Sort:** Efficient. Pick pivot element, ensure all elements before pivot < the pivot, all elements to right > pivot. Swapping elements on each side of pivot.

**Bucket Sort:** Buckets are created to put elements inside, then insertion sort applied on each bucket. Basically a stem and leaf plot, then sort merge each bucket together.

## Searches

**Binary Search:** If num im searching for is < midpoint, binary search on left side. else, right.
[1, 2, 3, 4, 5, 6, 7], Search for 2. Next iteration:
[1, 2, 3]

```python 
# This code not tested but looks right to me
def binSearchR(nums, value):
  if len(nums) <= 1:
    return -1

  mid = len(nums) // 2
  elif value < nums[i]:
    return binSearch(nums[:mid])
  elif value > nums[i]:
    return binSearch(nums[mid+1:])
  else:
    return mid

# Iterative
def binSearchI(nums, target):
  lo = 0
  hi = len(nums)-1
  while lo <= hi:
      mid = (lo+hi)//2
      if nums[mid] < target:
          lo = mid + 1
      elif nums[mid] > target:
          hi = mid -1
      else:
          return mid
        
  return -1

```

**(BFS) BreadthFirstSearch:** - Or, "Level-Order Traversal", row based search. Horizontal. QUEUE.
```python
def levelOrderSearch(root):
  ret = []   
  level = [root]
  
  while root and level:
      currentNodes = []
      nextLevel = []
      for node in level:
          currentNodes.append(node.val)
          if node.left:
              nextLevel.append(node.left)
          if node.right:
              nextLevel.append(node.right)
      ret.append(currentNodes)
      level = nextLevel
      
  return ret
```

### When to use:
- When you need to find the shortest path between any two nodes in an unweighted graph.
- If you're solving a problem, and know a solution is not far from the root of the tree, BFS will likely get you there faster.
- If the tree is very deep, BFS might be faster

**(DFS) DepthFirstSearch:** - Visits nodes starting from leaves, or from root. Vertical. STACK.

```python
# Inorder traversal (DFS Traversal)
# Left -> Root -> Right [L > N > R]
    def inorderTraversal(self, root):
        res = []
        if root:
            res = inorderTraversal(root.left)
            res.append(root.data)
            res = res + inorderTraversal(root.right)
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
Java Inorder traversal - Iterative
```java
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
    List<Integer> list = new ArrayList<Integer>();

    Stack<TreeNode> stack = new Stack<TreeNode>();
    TreeNode cur = root;

    while(cur!=null || !stack.empty()){
        while(cur!=null){
            stack.add(cur);
            cur = cur.left;
        }
        cur = stack.pop();
        list.add(cur.val);
        cur = cur.right;
    }

    return list;
  }
}
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

## Algorithm design

**Brute Force:**
Entertain every single possible choice. Exhaustive search. 

**Greedy:** 
Always makes the choice that seems to be the best at that moment. Locally optimal choice.

**Divide & Conquor** 
Divide problem into smaller subproblems - NO storing solution of each subproblem. 

**Dynamic Programming:**
Divide problem into smaller subproblems - Stores solution of each subproblem. Each subproblem IS dependent on the other.

## Questions to ask Interviewer 
-  Mentorship? Onboarding? 
-  What does a typical day look like?
-  Can you tell me about the team I'll be working with?
-  What do you personally like about working here?

## Behavioral questions 
- **Tell me about yourself.**
- **Why do you want to for for X?**
- **What are your goals/ What are you looking for in a new job?**
- **Why are you switching jobs?**
- Tell me about a time when you solved a conflict at work.
- What is your greatest strength?
- What is your greatest weakness?
- What was a challenge you had to overcome?
- Describe a time where you have failed, and what you learned from it
- What are you actively trying to improve on?
- Where do you see yourself in 5 years? 
- Tell me about a time you made a mistake and how did you resolve it?
- Tell me about something you did at work you are proud of?
- Tell me about an interesting problem you have worked on recently?
- Tell me about a time you took ownership/demonstrated leadership on a project?

# Things to work on: 
- SQL/Databases refresh
- Basic data structures, trade offs (dictionary good for lookup, linkedlist deletion, etc)
- map, reduce, filter in python
- refresh data structures & algos
- maybe another python project. Crypto? Stocks? Election data? Weather across the states? "Only in texas/midwest/florida/literallyeverywhere can you experience all 4 seasons in one day" data project to prove weather is unpredictable everywhere
- Coding questions:
  - LinkedList manipulations
  - Graph/Tree manipulations
  - Dynamic programming examples
  - Backtracking examples
  - Best/fastest route from a to b
  - Permutations/Combinations/Partitions
  - Sliding window -- 'Longest Continuous Increasing Subsequence'
  - Shortest path from a to b

- Leetcode Q's to revisit:
  ### EASY
  - Invert Binary Tree
  - Rotate Array
  - Subtree of Another Tree
  - Can Place Flowers (All dynamic programming probs tbh)
  - Non-decreasing array
  - Trim a Binary Search Tree
  ### MEDIUM
  - Find Peak Element

# Leetcode-y problem solving strategies:
  - Sliding window 
  - Dynamic Programming (with cache)
  - Two Pointers (fast/slow, beginning/end)
  - HashMap
  - Binary Search
  - Stack/Queue
  - Increment/Decrement hash table (d = {x: 1} , d[x] += 1 if x appears, d[x] -= 1 if x doesnt appear)

# External resources and sources:
- [Behavioral question tips](https://www.interviewcake.com/behavioral-questions-programming-interview-story-telling)
- [Tons of interview questions, specific to language/frameworks](https://www.onlineinterviewquestions.com/programming/)
- [System design resources](https://github.com/donnemartin/system-design-primer)
- [Reddit CS interview guide](https://www.reddit.com/r/cscareerquestions/comments/1jov24/heres_how_to_prepare_for_tech_interviews/)
- [Reddit free study resources](https://www.reddit.com/r/cscareerquestions/comments/e4v755/master_list_of_free_resources/)
- [Bfs vs Dfs](https://www.geeksforgeeks.org/bfs-vs-dfs-binary-tree/)
- [Basic graphs](https://www.bogotobogo.com/python/python_graph_data_structures.php)
- [Sorting](https://www.youtube.com/playlist?list=PL9xmBV_5YoZOZSbGAXAPIq1BeUf4j20pl)
- [Dijkstras](https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/)
- [Web application architecture {basics}](https://www.scnsoft.com/blog/web-application-architecture)
- [Web services](https://www.guru99.com/restful-web-services.html)
- [RESTful API's](https://searchapparchitecture.techtarget.com/definition/RESTful-API)