class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if s == "":
            return s
        
        stack = []
        remove = []
        for i, c in enumerate(s):
            if c == "(":
                if i == len(s)-1: # if at the very end then auto no
                    remove.append(i)
                else: # otherwise add to stack
                    stack.append(i)
                
            elif c == ")":
                if i == 0: # if at very beginning then auto no
                    remove.append(i)
                elif len(stack) == 0: # otherwise if stack empty (no open paranthese) then no
                    remove.append(i)
                else: # otherwise there's a match
                    stack.pop()

        for thing in stack:
            remove.append(thing)

        output = ""
        for i, c in enumerate(s):
            if i in remove:
                continue
            output += c

        return output