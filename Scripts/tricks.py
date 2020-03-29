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