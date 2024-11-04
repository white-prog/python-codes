import unittest

# Assuming the is_balanced function is defined in the same file.
# If it's in a different module, you can import it with:
# from your_module_name import is_balanced

def is_balanced(s: str) -> bool:
    stack = []
    matching_bracket = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in matching_bracket.values():  # If it's an opening bracket
            stack.append(char)
        elif char in matching_bracket.keys():  # If it's a closing bracket
            if stack == [] or stack.pop() != matching_bracket[char]:
                return False
    
    return stack == []  # Returns True if stack is empty

class TestIsBalanced(unittest.TestCase):
    def test_balanced_parentheses(self):
        # Test cases where the parentheses are balanced
        self.assertTrue(is_balanced("()[]{}"))
        self.assertTrue(is_balanced("{[()]}"))
        self.assertTrue(is_balanced(""))
        self.assertTrue(is_balanced("((()))"))
        self.assertTrue(is_balanced("[[{}]]"))

    def test_unbalanced_parentheses(self):
        # Test cases where the parentheses are not balanced
        self.assertFalse(is_balanced("{[(])}"))
        self.assertFalse(is_balanced("{[}"))
        self.assertFalse(is_balanced("(]"))
        self.assertFalse(is_balanced("([)]"))
        self.assertFalse(is_balanced("((("))

    def test_no_parentheses(self):
        # Test cases with no parentheses
        self.assertTrue(is_balanced("abc"))
        self.assertTrue(is_balanced("12345"))

    def test_mixed_characters(self):
        # Test cases with mixed characters and balanced parentheses
        self.assertTrue(is_balanced("a(b)c[d]{e}"))
        self.assertFalse(is_balanced("a(b{c]d)e"))

if __name__ == "__main__":
    unittest.main()
