# https://leetcode.com/problems/basic-calculator-ii/description/

class Solution:
    def calculate(self, s: str) -> int:

        """
        1. If the current character is a digit 0-9 ( operand ), add it to the number currentNumber.
        
        2. Otherwise, the current character must be an operation (+,-,*, /).
        Evaluate the expression based on the type of operation.
        
        3. Addition (+) or Subtraction (-): We must evaluate the expression 
        later based on the next operation. So, we must store the currentNumber 
        to be used later. Let's push the currentNumber in the Stack.
        """
        # Time complexity: O(n)
        # Space complexity: O(n)

        # Get rid of ll the white spaces
        s = s.replace(" ", "")

        current_num = 0
        result = 0
        operation = "+"

        stack = []

        for idx, ch in enumerate(s):
            if ch.isdigit():
                current_num = current_num * 10 + int(ch)
            if (not ch.isdigit()) or idx == len(s) - 1:
                if operation == "-":
                    stack.append(-current_num)
                elif operation == "+":
                    stack.append(current_num)
                elif operation == "*":
                    stack.append(stack.pop() * current_num)
                else:
                    stack.append(int(stack.pop() / current_num))
                
                operation = ch
                current_num = 0
        
        while stack:
            result += stack.pop()
        
        return result


# There is O(N) and O(1) solition as well
class Solution:
    def calculate(self, s: str) -> int:

        # 1) Strip out all spaces to simplify parsing
        s = s.replace(" ", "")
        n = len(s)

        # current_num: builds the integer we're currently reading
        current_num = 0
        # last_num: holds the last "term" we've processed to handle * and / first
        last_num = 0
        # result: accumulates the sum of completed terms for + and -
        result = 0
        # operation: the last operator we've seen (starts as '+' so first number is added)
        operation = '+'

        # 2) Single pass over the string
        for i, c in enumerate(s):
            if c.isdigit():
                # accumulate digit-by-digit (e.g. '42' → 4 then 42)
                current_num = current_num * 10 + int(c)

            # if c is an operator, or we're at the very end, time to process the term
            if (not c.isdigit()) or i == n - 1:
                if operation == '+':
                    # finish the previous term, then start a new positive term
                    result += last_num
                    last_num = current_num
                elif operation == '-':
                    # finish the previous term, then start a new negative term
                    result += last_num
                    last_num = -current_num
                elif operation == '*':
                    # multiply within the last term (higher precedence)
                    last_num = last_num * current_num
                elif operation == '/':
                    # integer division truncating toward zero
                    last_num = int(last_num / current_num)

                # update for the next round
                operation = c
                current_num = 0

        # 3) add the final pending term
        result += last_num
        return result
