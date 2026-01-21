import pandas as pd
import numpy as np
import time 

# 1. 데이터 가져와서 넘파이 변환
try :
    df = pd.read_csv("./advanced_trade_data.csv", encoding = "cp949")
    print(f"데이터를 성공적으로 불러왔습니다! 총 {len(df):,}행")
except FileNotFoundError : 
    print("파일이 없습니다. 파일다시찾아보쎄용.")
    exit()

# 판다스 컬럼을 넘파이 배열로 변환
# 분석 속도 높이기 위해 순수 수치 데이만 배열로 추출
print(df.head(10))
print(df.info())

export_val = df["export_value"].values
weight = df["weight"].values
logistics_rate = df["logistics_cost_rate"].values
tax_rate = df["tax_rate"].values
region_code = df["region_code"].values
# print(export_val)

start_time = time.time() # 현재 시간
# 물류비용 수출액 * 물류비율
logistics_cost = export_val * logistics_rate
print(logistics_cost)

# 관세 = 수출액 * 관세율
tax_cost = export_val * tax_rate

# 최종 순이익 = 수출액 - 물류비용 - 관세
net_profit = export_val - logistics_cost - tax_cost

end_time = time.time()

print(f"연산 완료 시간 : {end_time - start_time}초")
print(f"전체 순이익 : {net_profit}")
print(f"전체 평균 순이익 : {np.mean(net_profit):.2f}")


# 실습 2 통계분석 : 수출입 데이터 분포 파악
print("\n 주요 지표 통계 분석")
print(f" - 수출액 중앙값 : {np.median(export_val)}")
print(f" - 수출액 표준편차 : {np.std(export_val)}")
print(f" - 수출액 상위 5% 경계값 : {np.percentile(export_val, 95):,.2f}")

# 실습 3 
# 내용: 특정 조건을 만족하는 '우량 거래' 데이터만 따로 추출하여 분석하세요.
# 조건: 수출액이 $150,000$ 달러 이상이면서, 동시에 물류비 비율이 $10\%$($0.10$) 이하인 거래

prime_mark = (export_val >= 150000) & (logistics_rate <= 0.10)
# print(prime_mark)
prime_trades = export_val[prime_mark]
print(prime_trades)

print(f"\n 우량 거래 필터링 결과")
print(f" - 해당 건수 : {len(prime_trades)}건")
print(f" - 해당 거래 중 총 수출액 : {np.sum(prime_trades):,.2f}")


# 미션 4

unique_region = np.unique(region_code)
print(unique_region)
region_metrics=[]

for r in unique_region :
    mask = (region_code == r)
    region_metrics.append([
        np.mean(export_val[mask]),
        np.mean(logistics_rate[mask]),
        np.mean(tax_rate[mask])
    ])

A = np.array([
    [0.5],
    [-0.24], 
    [-0.24]
])

print(region_metrics)
B = np.array(region_metrics)
print(A)
print(B)

# print {market}
market = B @ A
print("\n 지역별 시장 매력도 점수")
region_name = ["아시아", "유럽", "북미", "기타"]
for i, name in enumerate(region_name) :
    print(f" - {name}지역의 종합 점수 : {market[i,0]:,.2f}")


# 미션 5 : 이상치 찾아 정상화
avg_log = np.mean(logistics_rate)
cleaned_log = np.where(logistics_rate > 0.15, avg_log, logistics_rate)
print(f"\n 데이터 보정 완료")
print(f" - 보정 전 최대 물류 비율 : {np.max(logistics_rate):,.2%}")
print(f" - 보정 후 최대 물류 비율 : {np.max(cleaned_log):.2%}")