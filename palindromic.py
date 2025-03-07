def is_palindromic(n):
    return str(n) == str(n)[::-1]
n = int(input())  
listt = set(map(int, input().split()))  
all_non_negative = all(i >= 0 for i in listt)
at_least_one_palindrome = any(is_palindromic(i) for i in listt)
print(all_non_negative and at_least_one_palindrome)