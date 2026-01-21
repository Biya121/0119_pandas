import numpy as np
# 선형대수 연사에 필요한 다차원 배열과 배열 연산을 수행하는 다양한 함수 제공

# 1. 넘파이 배열
# 파이썬 리스트와 비슷해 보이지만 계산 속도가 훨씬 빠르다.
a_values = np.array([12500,45000,32000,0,56000])
print(a_values)

b_values = np.array([
    [1000, 2000, 3000, 4000],
    [5000, 6000, 7000, 8000],
    [9000, 10000, 11000, 12000]
])
print(b_values)

c_values = np.array([
    # 지역이 아시아인 것
    [
        [100,200,300],
        [400,500,600],
        [700,800,900]
    ],
    [ 
        # 유럽
        [90,40,50],
        [80,80,90],
        [30,60,20]
    ],
    [
        # 북유럽
        [190,200,210],
        [300,520,212],
        [190,625,315],
    ]
])
print(c_values)

print(a_values.shape) # 행열 모양
print(b_values.shape)
print(c_values.shape)
print(a_values.itemsize) # 자료구조 byte
print(b_values.itemsize)
print(c_values.itemsize)
print(a_values.size) # 5
print(b_values.size) # 3*4
print(c_values.size) # 3*3*3 셀 개수

# np.zeros : 0으로 구성된 n차원 배열
# np.ones : 1로 구성된 n차원 배열
# np.empty : 초기화가 되는 n차원 배열

print(np.zeros((4,6)))
print(np.ones((2,3,4), dtype=np.int64))
print(np.empty((2,3)))

print(np.arange(10,30,5)) # [10,15,20,25]
print(np.arange(0,2,0.3)) # [0.  0.3 0.6 0.9 1.2 1.5 1.8]

print(np.linspace(0,99,100)) # 0부터 99까지 100등분
print(np.arange(0,1+0.25, 0.25))
print(np.linspace(0,1,5))

a = np.arange(6) # 1차원
print(a)
b = np.arange(12).reshape(4,3) # 1차원의 배열을 2차원으로 변경.
print(b)
c = np.arange(24).reshape(2,3,4) # 3차원으로 변경.
print(c)

a = np.array([20,30,40,50])
b = np.arange(4)
c = a-b
print(c) # 같은 열의 위치에 있는 것들끼리 연산됨. [20 29 38 47]

print(b**10)

print(a<35) # 만족시 True 그렇지않으면 False

A = np.array([
    [1,1],
    [0,1],
])

B = np.array([
    [2,0],
    [3,4]
])

print(A*B)
print(A@B) # 행렬 곱셈

# int < float # float이 더 강하게 취급됨.


# .sum
# .min
# .max
# .argmax : 모든 요소 중 최댓값의 인덱스
# .cumsum : 모든 요소의 누적합

a = np.arange(8).reshape(2,4)**2
# 8까지를 1차원으로 만들고 / 두 개의 행으로 나누고 네 개로 쪼개기 / 각각의 요소에 연산
print(a) # 0 1 4 9 16 25 36 49
print(a.sum())  # 140
print(a.min())
print(a.argmax()) # 7 = 49의 인덱스값
print(a.cumsum()) #   0   1   5  14  30  55  91 140

# 축기준 axis = 0 : 열기준 / axis = 1 : 행기준
b = np.arange(12).reshape(3,4) # 1차원의 자료를 3*4로 만든다!
print(b)
print(b.sum(axis=0))

# sqrt(25) = 제곱근을 찾아주는 함수

# 인덱싱 슬라이싱 : 데이터를 잘라서 가져오시오!
a = np.arange(10)**2
print(a)
print(a[2]) # 인덱스 번호 2번 가져오도록.
print(a[2:5]) # 4, 9, 16

a[0:6:2] = 1000
# 0번부터 6번 미만에서 두칸씩 점프
print(a) # [1000    1 1000    9 1000   25   36   49   64   81]

a = np.arange(8)**2
i = np.array([1,3,3,5])
print(a[i]) # [ 1  9  9 25]
j = np.array([[3,4], [5,6]])
print(a[j])

# 다차원이어도 1차원으로 변경    .ravel
# 지정한 차원으로 변경  .reshape
# 전치변환(행과 열 수를 변환)   .T

a = np.arange(12).reshape(3,4)
print(a) 
print(a.shape) # 3열 4행
print(a.ravel()) # 줄바꿈 안된 1차원의 결과
print(a.reshape(2,6)) # 2열 6행
print(a.T) # 4행 3열로 변경 - shape의 변형.
print(a.T.shape)

# np.vstack : axis = 0 (열) 방향으로 쌓기
# np.hstack : axis = 1 (행) 방향으로 쌓기
# np.hsplit : 숫자 1개가 들어가면 x개로 등분 / 리스트를 넣을 겨우 x 기준으로 데이터 분할

a = np.arange(12).reshape(2,6)
print(np.hsplit(a, 3))

print(np.hsplit(a,(3,4)))

a = np.array([1,2,3,4]).reshape(2,2)
b = np.array([5,6,7,8]).reshape(2,2)
print(np.vstack((a,b)))