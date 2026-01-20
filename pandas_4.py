import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime


# 데이터 불러오기
try : 
    # 실적 데이터 가져오기 trade_performance
    df_pref = pd.read_csv("./trade_performance.csv", encoding = "cp949")
    # 마스터 데이터(국가코드, 국가명) country_master
    df_master = pd.read_csv("./country_master.csv", encoding = "cp949")
except FileNotFoundError :
    print("❌ CSV파일을 찾을 수 없습니다. 경로를 다시 확인해 주세요.")
    exit()

print(df_pref)
print(df_master)

# 1. merge 머지
df = pd.merge(df_pref, df_master, on="ctry_code", how = "left")
# print(df)

# 2. 대륙별 성과 분석 / 총 수출액 수입 합계
continent_states = df.groupby("continent")[["export_val", "import_val"]].sum()
# print(continent_states)

# 3. 무역수지 계산
continent_states["무역수지"] = continent_states["export_val"] - continent_states["import_val"]
print("대륙별 무역 성과 요약")
# print(continent_states)
best_continent = continent_states["무역수지"].idxmax() # idxmax = 제일 큰 수치의 열을 가져옴.
print(f"분석 결과 : {best_continent} 대륙과의 거래에서 가장 큰 무역 수지 흑자가 발생했습니다.")

# 4. FTA 효과 분석 - 평균 수출 단가(수출금액/중량)
df["평균수출단가"] = df["export_val"] / df["weight"]

# FTA 여부에 따른 평균 단가 비교
fta_ans = df.groupby("fta_status")["평균수출단가"].mean()
print("\n FTA 여부에 따른 평균 수출 단가 비교")
print(fta_ans)

# 시사점 도출
if fta_ans["Y"] > fta_ans["N"] :
    print("결과 : FTA 체결 국가의 평균 단가보다 더 높게 나타남.")
else :
    print("결과 : FTA 체결 국가의 평균 단가보다 더 낮게 나타남.")


# 5. 품목별 집중도 분석 - 수출 금액이 가장 큰 상위 2개 추출, 품목이 어느 국가에 수출되는지 분석
# 수출금액이 가장 큰 상위 2개

top2_hs = df.groupby("hs_code")["export_val"].sum().nlargest(2).index.tolist()
# nlargest / nsmallest / index.tolist(리스트 변환)
print(f"\n 수출 상위 2개 품목 : {top2_hs}")

# 해당 품목들의 국가별 수출 근황
top2_df = df[df["hs_code"].isin(top2_hs)]
country_focus = top2_df.groupby(["hs_code", "ctry_name"])["export_val"].sum().reset_index
print(country_focus)

# 날짜 데이터 월 정보 추출
df["ymd"] = pd.to_datetime(df["ymd"])
df["month"] = df["ymd"].dt.month
# print(df.head())

# 시각화 - 월별 수출입 추이 데이터 생성
monthly = df.groupby("month")[["export_val", "import_val"]].sum()
plt.figure(figsize=(12,6))
plt.plot(monthly.index, monthly["export_val"], label = "수출액", marker = "o", linewidth = 2)
plt.plot(monthly.index, monthly["import_val"], label = "수입액", marker = "s", linewidth = 2)

plt.title("월별 수출입 실적 추이")
plt.xlabel("월(month)")
plt.ylabel("금액")
plt.show()