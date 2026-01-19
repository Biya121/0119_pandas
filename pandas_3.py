print("\n ------ 과제 2 시작 ------")

import pandas as pd
import numpy as np  

df = pd.read_csv('raw_trade_data.csv', encoding='cp949')

# 1) hs코드별 중량의 평균
hs_mean = df.groupby("hs_code")["중량"].mean()

# 중량이 비어있는(.isna()) 행
df.loc[df["중량"].isna(), "중량"] = mean_weight

# loc으로 행열 설정해 변경
df.loc[df["수출입구분"] == "Import", "수출입구분"] = "수입"
df.loc[df["수출입구분"] == "Export", "수출입구분"] = "수출"

df["수출금액_M_USD"] = (df["수출금액"] / 1470) / 1000000

print("--- 데이터 정보 요약 ---")
df.info()

print("\n--- 데이터 상위 5개 ---")
print(df.head()) 

df.to_csv("./cleaned_trade_data.csv", index=False)