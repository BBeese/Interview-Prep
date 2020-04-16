def fizzBuzz(self, n):
    return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]

# Reverse a linkedlist
def reverseList(self, head): 
    prev = None
    while head:
        curr = head
        head = head.next
        curr.next = prev
        prev = curr
    return prev

# Fibonacci. Most optimal solution - use LRU Cache
cache = {}
def fibonacci(num):
    if num in cache:
        return cache[num]

    if num == 0:
        result = 0
    elif num == 1 or num == 2:
        result = 1
    else:
        result = fibonacci(num - 2) + fibonacci(num - 1)

    cache[num] = result
    return result

# Valid parenthesis string check. valid input: "{[()]}" ; invalid input: "{)" ; uneven parenthesis
def isValid(s: str):
    stack = []
    ref = {"(": ")", "[": "]", "{": "}"}
    for item in s:
        if item in ref:
            stack.insert(0, item)
        elif stack and item == ref[stack[0]]:
            stack.pop(0)
        else:
            return False
            
    return not stack

# iteratively       
def inorderTraversal(self, root):
    res, stack = [], []
    while True:
        while root:
            stack.append(root)
            root = root.left
        if not stack:
            return res
        node = stack.pop()
        res.append(node.val)
        root = node.right

def isValidBST(self, root: TreeNode) -> bool:
    if not root: 
        return True
    stack = []
    pre = None
    while root or stack != []:
        while root:
            stack.insert(0, root)
            root = root.left
        root = stack.pop(0)
        if pre and root.val <= pre.val:
            return False
        pre = root
        root = root.right
    
    return True

# https://leetcode.com/problems/permutations/discuss/18237/My-AC-simple-iterative-javapython-solution
def permute(self, nums):
    perms = [[]]   
    for n in nums:
        new_perms = []
        for perm in perms:
            for i in xrange(len(perm)+1):   
                new_perms.append(perm[:i] + [n] + perm[i:])   ###insert n
        perms = new_perms
    return perms

# https://leetcode.com/problems/container-with-most-water/
def maxArea(self, height: List[int]) -> int:
    maxA = 0
    l = 0
    r = len(height)-1
    while (l<r):
        maxA = max(maxA, min(height[l], height[r])*(r-l))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return maxA

# Sliding window
def lengthOfLongestSubstring(self, s: str) -> int:

        j = 0
        i = 0
        ans = 0
        foundNums = set()
        while j < len(s) and i < len(s):
            if s[j] not in foundNums:
                foundNums.add(s[j])
                j += 1
                ans = max(ans, j-i)
            else:
                foundNums.remove(s[i])
                i += 1
    
        return ans

# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        if not self.stack:
            self.stack.append((x,x)) 
        else:
           self.stack.append((x,min(x,self.stack[-1][1])))

    def pop(self):
        if self.stack: 
            self.stack.pop()

    def top(self):
        if self.stack: 
            return self.stack[-1][0]
        return None

    def getMin(self):
        if self.stack: return self.stack[-1][1]
        else: return None
    
# Peak / Valley
def maxProfit(prices):
        i = 0
        maxProfit = 0
        valley, peak = prices[0]
        length = len(prices) - 1
        while (i < length:
            while (i < length and prices[i] >= prices[i + 1]):
                i += 1
            valley = prices[i]
            while (i < length and prices[i] <= prices[i + 1]):
                i += 1
            peak = prices[i]
            maxProfit += peak - valley
        return maxProfit