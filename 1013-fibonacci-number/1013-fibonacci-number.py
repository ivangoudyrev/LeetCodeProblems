class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            fib_num = 0
            num1 = 0
            num2 = 1
            for i in range(n-1):
                fib_num = num1 + num2
                num1 = num2
                num2 = fib_num
            return fib_num

