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