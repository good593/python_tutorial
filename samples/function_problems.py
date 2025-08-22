# 파이썬 함수 문제 모음
# 파이썬을 이제막 배운 학생들을 위한 함수 문제집

"""
=======================================================
                    초급 (Level 1)
=======================================================
"""

# 문제 1-1: 간단한 덧셈 함수
def problem_1_1():
    """
    문제: 두 개의 숫자를 입력받아 더한 결과를 반환하는 함수를 작성하세요.
    
    함수명: add_two_numbers
    매개변수: a (숫자), b (숫자)
    반환값: a와 b의 합
    
    예시:
    add_two_numbers(3, 5) -> 8
    add_two_numbers(10, 20) -> 30
    """
    pass

# 문제 1-2: 인사말 함수
def problem_1_2():
    """
    문제: 이름을 입력받아 "안녕하세요, [이름]님!"을 반환하는 함수를 작성하세요.
    
    함수명: greet
    매개변수: name (문자열)
    반환값: 인사말 문자열
    
    예시:
    greet("김철수") -> "안녕하세요, 김철수님!"
    greet("이영희") -> "안녕하세요, 이영희님!"
    """
    pass

# 문제 1-3: 절댓값 함수
def problem_1_3():
    """
    문제: 숫자를 입력받아 절댓값을 반환하는 함수를 작성하세요.
    (abs() 함수를 사용하지 말고 직접 구현하세요)
    
    함수명: absolute_value
    매개변수: num (숫자)
    반환값: num의 절댓값
    
    예시:
    absolute_value(5) -> 5
    absolute_value(-3) -> 3
    absolute_value(0) -> 0
    """
    pass

# 문제 1-4: 짝수/홀수 판별 함수
def problem_1_4():
    """
    문제: 숫자를 입력받아 짝수인지 홀수인지 판별하는 함수를 작성하세요.
    
    함수명: is_even
    매개변수: num (정수)
    반환값: 짝수면 True, 홀수면 False
    
    예시:
    is_even(4) -> True
    is_even(7) -> False
    is_even(0) -> True
    """
    pass

# 문제 1-5: 세 수 중 최댓값 찾기
def problem_1_5():
    """
    문제: 세 개의 숫자를 입력받아 가장 큰 값을 반환하는 함수를 작성하세요.
    (max() 함수를 사용하지 말고 직접 구현하세요)
    
    함수명: find_max
    매개변수: a (숫자), b (숫자), c (숫자)
    반환값: a, b, c 중 가장 큰 값
    
    예시:
    find_max(3, 7, 5) -> 7
    find_max(10, 2, 8) -> 10
    find_max(1, 1, 1) -> 1
    """
    pass

"""
=======================================================
                    중급 (Level 2)
=======================================================
"""

# 문제 2-1: 리스트 합계 계산
def problem_2_1():
    """
    문제: 숫자 리스트를 입력받아 모든 원소의 합을 반환하는 함수를 작성하세요.
    (sum() 함수를 사용하지 말고 직접 구현하세요)
    
    함수명: calculate_sum
    매개변수: numbers (숫자 리스트)
    반환값: 리스트 원소들의 합
    
    예시:
    calculate_sum([1, 2, 3, 4, 5]) -> 15
    calculate_sum([10, 20, 30]) -> 60
    calculate_sum([]) -> 0
    """
    pass

# 문제 2-2: 팩토리얼 계산
def problem_2_2():
    """
    문제: 양의 정수 n을 입력받아 n! (팩토리얼)을 계산하는 함수를 작성하세요.
    
    함수명: factorial
    매개변수: n (양의 정수)
    반환값: n의 팩토리얼
    
    예시:
    factorial(5) -> 120 (5 * 4 * 3 * 2 * 1)
    factorial(3) -> 6 (3 * 2 * 1)
    factorial(0) -> 1
    factorial(1) -> 1
    """
    pass

# 문제 2-3: 문자열 뒤집기
def problem_2_3():
    """
    문제: 문자열을 입력받아 뒤집은 문자열을 반환하는 함수를 작성하세요.
    (슬라이싱 [::-1]을 사용하지 말고 직접 구현하세요)
    
    함수명: reverse_string
    매개변수: text (문자열)
    반환값: 뒤집힌 문자열
    
    예시:
    reverse_string("hello") -> "olleh"
    reverse_string("python") -> "nohtyp"
    reverse_string("a") -> "a"
    """
    pass

# 문제 2-4: 소수 판별
def problem_2_4():
    """
    문제: 2 이상의 정수를 입력받아 소수인지 판별하는 함수를 작성하세요.
    
    함수명: is_prime
    매개변수: num (2 이상의 정수)
    반환값: 소수면 True, 아니면 False
    
    예시:
    is_prime(7) -> True
    is_prime(10) -> False
    is_prime(2) -> True
    is_prime(1) -> False
    """
    pass

# 문제 2-5: 리스트에서 중복 제거
def problem_2_5():
    """
    문제: 리스트를 입력받아 중복된 원소를 제거한 새로운 리스트를 반환하는 함수를 작성하세요.
    (set()을 사용하지 말고 직접 구현하세요. 순서는 처음 등장한 순서를 유지하세요)
    
    함수명: remove_duplicates
    매개변수: lst (리스트)
    반환값: 중복이 제거된 리스트
    
    예시:
    remove_duplicates([1, 2, 2, 3, 1, 4]) -> [1, 2, 3, 4]
    remove_duplicates([5, 5, 5]) -> [5]
    remove_duplicates([]) -> []
    """
    pass

"""
=======================================================
                    고급 (Level 3)
=======================================================
"""

# 문제 3-1: 피보나치 수열
def problem_3_1():
    """
    문제: n번째 피보나치 수를 반환하는 함수를 작성하세요.
    (피보나치 수열: 0, 1, 1, 2, 3, 5, 8, 13, ...)
    
    함수명: fibonacci
    매개변수: n (0 이상의 정수)
    반환값: n번째 피보나치 수
    
    예시:
    fibonacci(0) -> 0
    fibonacci(1) -> 1
    fibonacci(6) -> 8
    fibonacci(10) -> 55
    """
    pass

# 문제 3-2: 단어 빈도수 계산
def problem_3_2():
    """
    문제: 문자열을 입력받아 각 단어의 빈도수를 딕셔너리로 반환하는 함수를 작성하세요.
    (대소문자는 구분하지 않고, 구두점은 제거하세요)
    
    함수명: word_frequency
    매개변수: text (문자열)
    반환값: {단어: 빈도수} 형태의 딕셔너리
    
    예시:
    word_frequency("Hello world hello") -> {"hello": 2, "world": 1}
    word_frequency("Python is great! Python is fun.") -> {"python": 2, "is": 2, "great": 1, "fun": 1}
    """
    pass

# 문제 3-3: 이차원 리스트 전치(transpose)
def problem_3_3():
    """
    문제: 이차원 리스트(행렬)를 입력받아 전치행렬을 반환하는 함수를 작성하세요.
    
    함수명: transpose_matrix
    매개변수: matrix (이차원 리스트)
    반환값: 전치된 이차원 리스트
    
    예시:
    transpose_matrix([[1, 2, 3], [4, 5, 6]]) -> [[1, 4], [2, 5], [3, 6]]
    transpose_matrix([[1, 2], [3, 4], [5, 6]]) -> [[1, 3, 5], [2, 4, 6]]
    """
    pass

# 문제 3-4: 재귀를 이용한 리스트 합계
def problem_3_4():
    """
    문제: 재귀함수를 사용하여 숫자 리스트의 합을 계산하는 함수를 작성하세요.
    
    함수명: recursive_sum
    매개변수: numbers (숫자 리스트)
    반환값: 리스트 원소들의 합
    
    예시:
    recursive_sum([1, 2, 3, 4, 5]) -> 15
    recursive_sum([10, 20]) -> 30
    recursive_sum([]) -> 0
    """
    pass

# 문제 3-5: 가변 인자를 사용한 평균 계산
def problem_3_5():
    """
    문제: 가변 인자(*args)를 사용하여 임의의 개수의 숫자를 받아 평균을 계산하는 함수를 작성하세요.
    
    함수명: calculate_average
    매개변수: *numbers (가변 인자로 받는 숫자들)
    반환값: 숫자들의 평균 (소수점 둘째 자리까지)
    
    예시:
    calculate_average(1, 2, 3, 4, 5) -> 3.0
    calculate_average(10, 20, 30) -> 20.0
    calculate_average(7) -> 7.0
    """
    pass

if __name__ == "__main__":
    print("파이썬 함수 문제집")
    print("=" * 50)
    print("초급 (Level 1): 5문제")
    print("중급 (Level 2): 5문제") 
    print("고급 (Level 3): 5문제")
    print("=" * 50)
    print("각 문제의 함수 내용을 확인하여 문제를 해결해보세요!")
