def isBalanced(s):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in bracket_map: 
            top_element = stack.pop() if stack else '#'
            if bracket_map[char] != top_element:
                return "NO"
        else: 
            stack.append(char)
    return "YES" if not stack else "NO"

if __name__ == "__main__":
    n = int(input())
    results = []
    for _ in range(n):
        s = input() 
        results.append(isBalanced(s))
    print("\n".join(results))