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