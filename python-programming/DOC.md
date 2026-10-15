### 2026.10.14

- 코드 주석 관리 및 변수 할당
팀 베이스 프로젝트 시 각 문서에 대한 주석, 변수명 설정 중요.
    - 변수: 값이나 값을 반환하는 수식, 함수
    - 64bits 기준 변수 당 28bytes

- 함수(`def`)
    - 재사용성을 높임.
    - 가독성을 높임.

- 리스트(List)
    - 여러 값을 순서대로 저장하는 자료형. 인덱스는 `0`부터 시작하며, 요소를 추가·조회·수정·삭제할 수 있음.
    - CRUD: 데이터를 다루는 네 가지 기본 작업.

    | 약자 | 의미 | 사용 방법 |
    | --- | --- | --- |
    | C — Create | 추가 | `append(x)`, `insert(i, x)`, `extend(iterable)` |
    | R — Read | 조회 | 인덱싱 `items[0]`, 슬라이싱 `items[1:3]` |
    | U — Update | 수정 | 인덱스에 값 할당 `items[0] = 새 값` |
    | D — Delete | 삭제 | `remove(x)`, `pop(i)`, `clear()`, `del items[i]` |

    - 조회와 수정은 보통 함수 대신 인덱스 문법을 사용함.
    - 추가 메서드
        - `append(x)`: 맨 뒤에 요소 하나 추가.
        - `insert(i, x)`: 지정한 인덱스에 요소 추가.
        - `extend(iterable)`: 전달한 iterable의 요소들을 차례로 추가.
    - 삭제 방법
        - `remove(x)`: 값이 `x`인 첫 번째 요소 삭제. 값이 없으면 `ValueError` 발생.
        - `pop(i)`: 지정한 인덱스의 요소를 삭제하면서 반환. 인덱스를 생략하면 마지막 요소를 처리함.
        - `clear()`: 모든 요소 삭제.
        - `del items[i]`: 지정한 인덱스의 요소 삭제. `del`은 함수가 아닌 문법임.
    - CRUD 예시

        ```python
        fruits = ["사과", "바나나"]

        # C: 추가
        fruits.append("포도")  # ["사과", "바나나", "포도"]

        # R: 조회
        print(fruits[0])  # 사과

        # U: 수정
        fruits[1] = "딸기"  # ["사과", "딸기", "포도"]

        # D: 삭제
        fruits.remove("사과")  # ["딸기", "포도"]
        ```
    - CRUD 외에도 순회(`for`), 정렬(`sort()`), 포함 여부 확인(`in`)을 함께 익히면 좋음.

- 조건문 (`if`, `elif`, `else`)


- 순환문 (`for`, `while`)

### 2026.10.15

#### day2.py — 기본 문법과 자료구조

- 논리 연산자: `and`는 두 조건이 모두 참, `or`는 하나 이상 참일 때 조건을 만족함.
    - 단락 평가: `and`는 앞이 거짓이면, `or`는 앞이 참이면 뒤를 평가하지 않음.
    - 예: `user_profile and user_profile.get("name")`은 객체가 있을 때만 이름을 조회함.
- 클래스와 객체: 클래스는 속성과 동작을 정의하고, 객체는 클래스로 만든 개별 인스턴스임.
    - `__init__`: 객체 생성 시 속성을 초기화. `self`: 해당 객체를 가리킴.
    - 예: `user_profile = SafeProfile("홍길동", 30)`, 속성 조회는 `user_profile.name`.
    - 클래스명은 `PascalCase`, 변수·함수·메서드명은 `snake_case` 사용.
- 조건 표현식: `"성인" if user_age >= 18 else "미성년자"`처럼 조건에 따라 값을 선택함.
- 포함 여부: `in`은 포함, `not in`은 미포함 확인. 딕셔너리에서는 키를 검사함.

| 구분 | 리스트 (`list`) | 딕셔너리 (`dict`) |
| --- | --- | --- |
| 구조 | `[1, 2, 3]` | `{"one": 1, "two": 2}` |
| 조회 | `items[0]` — 인덱스 | `data["one"]` — 키 |
| 용도 | 여러 항목을 순서대로 저장 | 이름이 있는 데이터를 저장 |

- 딕셔너리 주요 사용법
    - `data.get("key", 기본값)`: 키가 없으면 기본값 반환. 기본값 생략 시 `None`.
    - `data["key"]`: 키가 없으면 `KeyError` 발생.
    - `keys()`, `values()`, `items()`: 각각 키, 값, `(키, 값)` 쌍 조회.
    - `data["key"] = 값`, `data.update({...})`: 항목 추가 또는 수정.
    - `data.pop("key")`: 항목을 삭제하고 해당 값 반환.
    - `for key in data:`는 키를 순회. 키와 값은 `for key, value in data.items():`로 순회.
    - n번째 항목: `key, value = list(data.items())[n]` (`0`부터 시작, 추가한 순서 기준).
    - `data[0]`은 첫 번째 항목이 아니라 정수 키 `0`에 접근함.

#### day2.py — 리스트 가공과 정규식 활용

- 리스트 컴프리헨션: `[표현식 for 항목 in 데이터 if 조건]`으로 변환과 필터링을 간결하게 작성함.
    - 필터링: `[i for i in list_1 if i % 2 == 0]`
    - 값 선택: `["adult" if age >= 20 else "adolescent" for age in ages]`
- `if word`는 빈 문자열을 제외함. 공백만 있는 문자열(`" "`)은 제외하지 않음.
- `set()`은 중복을 제거하지만 기존 순서를 유지하지 않음.
- `sorted(데이터)`는 정렬된 새 리스트를 반환함. `리스트.sort()`는 원본을 정렬하고 `None`을 반환함.

```python
bad_words = ["bad", "", "evil", "nasty", "", "mean", "bad"]
filtered_words = sorted({word for word in bad_words if word})
print(filtered_words)  # ['bad', 'evil', 'mean', 'nasty']
```

정규식(`re`)을 활용하면 문자열이 특정 규칙에 맞는지도 검사할 수 있음. 현재 `day2.py`는 `re`를 가져오기만 하므로, 아래는 확장 예시임.

```python
import re

# 영문 소문자로만 구성된 단어를 추출하고, 중복 제거 후 정렬
words = ["bad", "", "evil", "bad", "bad123", " "]
filtered_words = sorted({word for word in words if re.fullmatch(r"[a-z]+", word)})
print(filtered_words)  # ['bad', 'evil']
```

- `re.fullmatch(패턴, 문자열)`: 문자열 전체가 패턴과 일치하면 매치 객체, 아니면 `None`을 반환함.
- `r"[a-z]+"`: 영문 소문자(`[a-z]`)가 한 글자 이상(`+`)인 패턴. 빈 문자열도 제외됨.
- `r"..."`는 역슬래시를 그대로 표현하는 raw 문자열로, 정규식 작성에 주로 사용함.

| 패턴 | 의미 | 예시 |
| --- | --- | --- |
| `[a-z]`, `[A-Z]` | 영문 소문자, 대문자 한 글자 | `[a-z]+` → `hello` |
| `[0-9]` | 숫자 0~9 한 글자 | `[0-9]+` → `123` |
| `[가-힣]` | 완성형 한글 음절 한 글자 | `[가-힣]+` → `안녕` |
| `[^0-9]` | 숫자 0~9가 아닌 한 글자 | `[^0-9]+` → `abc` |
| `\d` | 유니코드 숫자 한 글자 | `\d+` → `123` |
| `\w` | 유니코드 문자·숫자 또는 밑줄(`_`) | `\w+` → `이름_1` |
| `\s` | 공백 문자(스페이스, 탭, 줄바꿈 등) | `\s+` → 연속된 공백 |
| `.` | 줄바꿈을 제외한 임의의 한 글자 | `a.c` → `abc` |
| `*` | 앞 패턴이 0회 이상 반복 | `ab*` → `a`, `ab`, `abb` |
| `+` | 앞 패턴이 1회 이상 반복 | `ab+` → `ab`, `abb` |
| `?` | 앞 패턴이 0회 또는 1회 등장 | `ab?` → `a`, `ab` |
| `{n}`, `{n,m}` | 앞 패턴이 n회, n~m회 반복 | `[0-9]{2,3}` → `12`, `123` |
| `^`, `$` | 문자열 시작, 끝 (`$`는 마지막 줄바꿈 직전도 허용) | `^hello$` → `hello` |
| `\.` | 실제 마침표 | `a\.b` → `a.b` |

문자열 전체의 형식을 검사할 때는 `re.fullmatch()`를 사용하면 `^`, `$`를 붙일 필요가 없음.

#### api_request.py — 사용자 권한 분기

- 사용자 한 명은 딕셔너리, 여러 명은 딕셔너리들을 담은 리스트로 관리함.
- 필드: `username`(이름), `user_role`(역할), `is_suspended`(정지 여부, 불리언).
- 처리 순서: 정지 여부 확인 → 허용된 역할인지 확인 → 역할별 안내 출력.
    - 정지 계정이면 안내 후 `continue`로 현재 사용자 처리를 끝내고 다음 사용자로 넘어감.
    - 정의되지 않은 역할이면 오류 메시지 출력.

| 역할 | 권한 |
| --- | --- |
| `admin` | 전체 시스템 관리 및 데이터 수정 |
| `manager` | 팀 데이터 조회 및 수정 |
| `user` | 개인 데이터 조회 |
| `guest` | 일부 데이터 읽기 전용 |

#### CSV 파일로 사용자 입력 받기

`csv.DictReader`는 첫 행을 키로 사용하고, 이후 각 행을 딕셔너리로 읽음.

```csv
username,user_role,is_suspended
alpha,admin,False
bravo,user,True
```

기존 `test_users` 선언을 다음 코드로 바꾸면 아래의 권한 검사 반복문을 그대로 사용할 수 있음.

```python
import csv
from pathlib import Path

csv_path = Path(__file__).with_name("users.csv")  # 파이썬 파일과 같은 폴더
with csv_path.open(encoding="utf-8-sig", newline="") as file:
    test_users = []
    for row in csv.DictReader(file):
        suspended = row["is_suspended"].strip().lower()
        if suspended not in ("true", "false"):
            raise ValueError("is_suspended는 True 또는 False여야 합니다.")
        row["is_suspended"] = suspended == "true"
        test_users.append(row)
```

- CSV 값은 기본적으로 문자열이므로 `is_suspended`를 불리언으로 변환해야 함. `bool("False")`는 `True`이므로 사용하지 않음.
- `utf-8-sig`는 일반 UTF-8과 BOM이 있는 UTF-8 파일을 읽을 수 있음.
- 전체 데이터를 저장할 필요가 없다면 `with` 블록 안에서 `for user in csv.DictReader(file):`로 바로 처리할 수 있음. 이때도 불리언 변환은 필요함.


#### vibe-coding
1. 무엇을 만들지
2. 어떤 제약을 가지고 동작하는지
3. 구현은 어떻게
4. 결과를 검증

- 핵심 룰: P(Prompt) --> G(Generation) --> V(Validation)
    - Prompt: 입력, 출력, 알고리즘 제약 조건, 함수 명시
    [Problem]
    [Fuctions]
    [Rules]
    [Inputs]
    [Outputs]

    - Validation: 결과검증 --> one-shot to few-shot examples
                         --> "생성하는 코드는 대중적으로 해석하기 쉬운 방법과 라이브러리를 사용해줘"
                         --> "테스트 케이스(assert 사용)를 n개 만들어서 오류가 생기면 수정할 것."
                         --> "주석으로 각 핵심 라인의 동작을 설명할 것."
                         --> "채팅창에는 최소한의 알아야 할 것, 선택이 필요한 부분을 남기고, 파일 주석에는 자세한 정보를 담을 것"

- assert 조건, "실패 시 나올 메시지"
