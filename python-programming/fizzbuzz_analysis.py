'''
[function] analyze_fizzbuzz
[constraints]
- 1부터 limit까지 순회
- 3의 배수이면 "Fizz" 카운트 증가
- 5의 배수이면 "Buzz" 카운트 증가
- 그 외의 숫자이면 "Other" 카운트 증가
- 결과를 딕셔너리로 반환
- 엣지 케이스: limit이 1이하이면 빈 딕셔너리 반환
[return]
- {"Fizz": fizz_count, "Buzz": buzz_count, "Other": other_count}

'''


def analyze_fizzbuzz(limit):
    """1부터 limit까지 집계하며, 공배수는 Fizz와 Buzz 모두에 포함한다."""
    if limit <= 1:
        return {}

    counts = {"Fizz": 0, "Buzz": 0, "Other": 0}

    for number in range(1, limit + 1):
        if number % 3 == 0:
            counts["Fizz"] += 1
        if number % 5 == 0:
            counts["Buzz"] += 1
        if number % 3 != 0 and number % 5 != 0:
            counts["Other"] += 1

    return counts


print(analyze_fizzbuzz(15))  # {'Fizz': 5, 'Buzz': 3, 'Other': 7}