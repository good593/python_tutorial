# 파이썬 함수 문제 해답 모음
# 학습자를 위한 예시 답안

"""
=======================================================
                    초급 (Level 1) 해답
=======================================================
"""

# 문제 1-1 해답: 간단한 덧셈 함수
def add_two_numbers(a, b):
    """두 개의 숫자를 더한 결과를 반환"""
    return a + b

# 문제 1-2 해답: 인사말 함수
def greet(name):
    """이름을 받아 인사말을 반환"""
    return f"안녕하세요, {name}님!"

# 문제 1-3 해답: 절댓값 함수
def absolute_value(num):
    """숫자의 절댓값을 반환"""
    if num < 0:
        return -num
    else:
        return num

# 문제 1-4 해답: 짝수/홀수 판별 함수
def is_even(num):
    """짝수면 True, 홀수면 False 반환"""
    return num % 2 == 0

# 문제 1-5 해답: 세 수 중 최댓값 찾기
def find_max(a, b, c):
    """세 수 중 가장 큰 값을 반환"""
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

"""
=======================================================
                    중급 (Level 2) 해답
=======================================================
"""

# 문제 2-1 해답: 리스트 합계 계산
def calculate_sum(numbers):
    """리스트의 모든 원소의 합을 반환"""
    total = 0
    for num in numbers:
        total += num
    return total

# 문제 2-2 해답: 팩토리얼 계산
def factorial(n):
    """n의 팩토리얼을 계산"""
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# 문제 2-3 해답: 문자열 뒤집기
def reverse_string(text):
    """문자열을 뒤집어 반환"""
    result = ""
    for i in range(len(text) - 1, -1, -1):
        result += text[i]
    return result

# 문제 2-4 해답: 소수 판별
def is_prime(num):
    """소수인지 판별"""
    if num < 2:
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# 문제 2-5 해답: 리스트에서 중복 제거
def remove_duplicates(lst):
    """중복 제거된 리스트 반환 (순서 유지)"""
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

"""
=======================================================
                    고급 (Level 3) 해답
=======================================================
"""

# 문제 3-1 해답: 피보나치 수열
def fibonacci(n):
    """n번째 피보나치 수를 반환"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b

# 문제 3-2 해답: 단어 빈도수 계산
def word_frequency(text):
    """단어 빈도수를 딕셔너리로 반환"""
    import string
    
    # 구두점 제거하고 소문자로 변환
    text = text.lower()
    for punct in string.punctuation:
        text = text.replace(punct, "")
    
    words = text.split()
    frequency = {}
    
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    
    return frequency

# 문제 3-3 해답: 이차원 리스트 전치
def transpose_matrix(matrix):
    """이차원 리스트의 전치행렬을 반환"""
    if not matrix or not matrix[0]:
        return []
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    result = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        result.append(new_row)
    
    return result

# 문제 3-4 해답: 재귀를 이용한 리스트 합계
def recursive_sum(numbers):
    """재귀를 사용하여 리스트 합계 계산"""
    if not numbers:  # 빈 리스트
        return 0
    elif len(numbers) == 1:  # 원소가 하나
        return numbers[0]
    else:
        return numbers[0] + recursive_sum(numbers[1:])

# 문제 3-5 해답: 가변 인자를 사용한 평균 계산
def calculate_average(*numbers):
    """가변 인자로 받은 숫자들의 평균을 계산"""
    if len(numbers) == 0:
        return 0
    
    total = sum(numbers)
    average = total / len(numbers)
    return round(average, 2)

"""
=======================================================
                        테스트 코드
=======================================================
"""

def test_all_functions():
    """모든 함수들을 테스트"""
    print("초급 문제 테스트")
    print("-" * 30)
    print(f"add_two_numbers(3, 5) = {add_two_numbers(3, 5)}")
    print(f"greet('김철수') = {greet('김철수')}")
    print(f"absolute_value(-3) = {absolute_value(-3)}")
    print(f"is_even(4) = {is_even(4)}")
    print(f"find_max(3, 7, 5) = {find_max(3, 7, 5)}")
    
    print("\n중급 문제 테스트")
    print("-" * 30)
    print(f"calculate_sum([1, 2, 3, 4, 5]) = {calculate_sum([1, 2, 3, 4, 5])}")
    print(f"factorial(5) = {factorial(5)}")
    print(f"reverse_string('hello') = {reverse_string('hello')}")
    print(f"is_prime(7) = {is_prime(7)}")
    print(f"remove_duplicates([1, 2, 2, 3, 1, 4]) = {remove_duplicates([1, 2, 2, 3, 1, 4])}")
    
    print("\n고급 문제 테스트")
    print("-" * 30)
    print(f"fibonacci(6) = {fibonacci(6)}")
    print(f"word_frequency('Hello world hello') = {word_frequency('Hello world hello')}")
    print(f"transpose_matrix([[1, 2, 3], [4, 5, 6]]) = {transpose_matrix([[1, 2, 3], [4, 5, 6]])}")
    print(f"recursive_sum([1, 2, 3, 4, 5]) = {recursive_sum([1, 2, 3, 4, 5])}")
    print(f"calculate_average(1, 2, 3, 4, 5) = {calculate_average(1, 2, 3, 4, 5)}")

if __name__ == "__main__":
    test_all_functions()
