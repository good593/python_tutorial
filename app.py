from common.utils import print_gugudan, is_odd
from common.math import add, subtract, multiply, divide 

def main():
  """
  홀수(3,5,7,9) 단위의 구구단 합과 짝수(2,4,6,8) 단위의 구구단 합을 빼주면 값은?
  """
  # 초기값 
  sum_even = 0
  sum_odd = 0 
  
  for i in range(2,10):
    if is_odd(i): # 홀수 
      sum_odd = print_gugudan(n=i, sum_n=sum_odd, is_print=False) 
    else: # 짝수 
      sum_even = print_gugudan(n=i, sum_n=sum_even, is_print=False)  
  
  # 전체 for문이 끝났을 때, 
  print(f"sum_odd: {sum_odd}")
  print(f"sum_even: {sum_even}")
  print(f"홀수의 합과 짝수의 합을 빼면, {subtract(sum_odd, sum_even)}")

if __name__ == "__main__": 
  main() 
