class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_str = str(x)
        num_str_arr = []
        for ltr in num_str:
            num_str_arr.append(ltr)
        num_str_arr_backwards = num_str_arr[::-1]
        num_str_arr_backwards_str = ''.join(num_str_arr_backwards)
        if num_str == num_str_arr_backwards_str:
            return True
        else:
            return False