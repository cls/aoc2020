import operator
import sys

class Parser:
    def __init__(self, string, precedence):
        self._char = None
        self._iter = iter(string)
        self._precedence = precedence

    def peek_char(self):
        if self._char is None:
            self._char = next(self._iter)
        return self._char

    def next_char(self):
        char = self.peek_char()
        self._char = None
        return char

    def peek_token(self):
        while self.peek_char() == ' ':
            self.next_char()
        return self.peek_char()

    def next_token(self):
        self.peek_token()
        return self.next_char()

    def peek_precedence(self):
        return self._precedence.get(self.peek_token(), -1)

    def parse_line(self):
        value = self.parse_expression()
        if self.next_token() != '\n':
            raise Exception("Expected newline")
        return value

    def parse_expression(self):
        return self.parse_subexpression(self.parse_number(), 0)

    def parse_subexpression(self, lhs, min_precedence):
        while self.peek_precedence() >= min_precedence:
            op_precedence = self.peek_precedence()
            op = self.parse_operator()
            rhs = self.parse_number()
            while self.peek_precedence() > op_precedence:
                rhs = self.parse_subexpression(rhs, self.peek_precedence())
            lhs = op(lhs, rhs)
        return lhs

    def parse_number(self):
        char = self.next_token()
        if char == '(':
            value = self.parse_expression()
            if self.next_token() != ')':
                raise Exception("Expected closing parenthesis")
            return value
        elif char.isdigit():
            result = char
            while self.peek_char().isdigit():
                result += self.next_char()
            return int(result)
        else:
            raise Exception("Expected number")

    def parse_operator(self):
        char = self.next_token()
        if char == '+':
            return operator.add
        elif char == '*':
            return operator.mul
        else:
            raise Exception("Expected operator")

def parse(string, precedence):
    return Parser(string, precedence).parse_line()

result1 = 0
result2 = 0

for line in sys.stdin:
    result1 += parse(line, {'+': 0, '*': 0})
    result2 += parse(line, {'+': 1, '*': 0})

print(result1)
print(result2)
