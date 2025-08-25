from common.math import add, subtract, multiply, divide 

# 구구단 함수 
def print_gugudan(n:int=3, sum_n:int=0, is_print=True) -> int:
  """
  구구단 함수 
  Args:
    n: 구구단 단수 
  Returns:
    None 
  """
  i = 1 # 구구단은 1부터 9까지 
  # 4. 1부터 9까지 반복하며 곱하는 함수 -> while 문 사용
  while True: # 무한 반복 
    if i > 9: # i가 10일 때 종료 
      # 5. 9까지 반복하였다면, break 문 사용하여 while 문 종료 
      break

    # 1. 특정 숫자를 1부터 9까지 곱하는 함수 -> multiply 함수 사용 
    # multiply(3,5) -> 15 
    result = multiply(n, i)
    sum_n = add(sum_n, result)

    if is_print:
      # 2. 곱한 결과를 출력 -> print 함수 사용
      # 3 * 5 = 15 
      print(f"{n} * {i} = {result}") # 구구단 출력 
    
    # 3. 1씩 증가하며 곱하는 함수 -> add 함수 사용
    # add(5,1) -> 6 
    # i = 6 
    i = add(i, 1) # 1씩 증가 

  return sum_n

# 홀수 구분 함수
def is_odd(n:int) -> bool:
  return int(str(divide(n,2)).split(".")[1]) != 0

if __name__ == "__main__": 
  print_gugudan(5) 
