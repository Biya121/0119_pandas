import matplotlib.pyplot as plt

# # 하나의 숫자 리스트 입력 / y축값
# plt.plot([2,3,4,5])
# plt.clf()
# # plt.show()

# plt.plot([1,2,3,4], [1,4,9,16]) # 첫 번째 x축, 두 번째 y축
# plt.xlabel("X-label")
# plt.ylabel("Y-label")
# # plt.show()

# plt.plot([1,2,3,4], [1,4,5,13], label = "Square")
# plt.xlabel("X-label")
# plt.ylabel("Y-label")
# plt.legend()
# # plt.show()

# # xlim(xmin, xmax)
# # ylim(ymin,ymax)
# plt.plot([1,2,3,4], [3,6,9,12])
# plt.xlabel("X-label")
# plt.ylabel("Y-label")
# # plt.xlim([0,5])
# # plt.ylim([0,15])
# plt.axis([0,5,0,20])
# # plt.show()

# 선종류 solid line dashed line dash-dot line dotted line
# plt.plot([1,2,3], [4,4,4] ,"-", label = "solid", color = "#ff7f00")
# plt.plot([1,2,3], [3,3,3] , "--", label = "dashed")
# plt.plot([1,2,3], [2,2,2] , linestyle = "dotted", label = "dotted")
# plt.plot([1,2,3], [1,1,1] , linestyle = "dashdot", label = "dash-dot")
# plt.xlabel("X-label")
# plt.ylabel("Y-label")
# plt.legend(loc="upper right", ncol=4)
# plt.show()

# 마커
# plt.plot([4,5,6],"b")
# plt.plot([3,4,5],"ro")
# plt.plot([2,3,4], marker = "s")
# plt.plot([1,2,3], marker = "D")
# plt.plot([0,1,2], marker = "$A$")
# plt.title("titanic" , loc="center", pad=20)
# plt.show()


# 산점도 차트
import numpy as np

np.random.seed(0) # 코드 실행 시 매번 똑같은 랜덤 값 고정
n=50

x = np.random.rand(n)
y = np.random.rand(n)

size = (np.random.rand(n)*20)**2
color = np.random.rand(n)
plt.scatter(x, y, s=size, c=color, alpha = 0.5) # alpha = 투명도
plt.colorbar()
plt.show()