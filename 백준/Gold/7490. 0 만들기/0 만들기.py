def find_zero_sum_expressions(N):
    results = []

    def evaluate_expression(expr):
        # Replace spaces with empty string to concatenate numbers
        expr = expr.replace(" ", "")
        return eval(expr)

    def backtrack(expr, index):
        if index > N:
            if evaluate_expression(expr) == 0:
                results.append(expr)
            return

        # Add the current number with different operators
        backtrack(expr + ' ' + str(index), index + 1)
        backtrack(expr + '+' + str(index), index + 1)
        backtrack(expr + '-' + str(index), index + 1)

    # Start the backtracking process with the first number
    backtrack("1", 2)
    return results

import sys
input = sys.stdin.readline

N = int(input())
for i in range(N):
    zero_sum_expressions = find_zero_sum_expressions(int(input()))
    for expr in zero_sum_expressions:
        print(expr)

    if i != N - 1:
        print()

