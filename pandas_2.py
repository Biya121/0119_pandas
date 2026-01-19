import pandas as pd
import numpy as np 

df = pd.read_csv('raw_trade_data.csv', encoding='cp949') 
# 한국어인코딩 : cp949, euc-kr, utf-8, utf-8-sig
# print(df)

# 1) HS코드 앞 2자리 '85'인 데이터 추출
# print(df.info()) int64
semiconductor_df = df[df["hs_code"].astype("str").str.startswith("85")]

# 2) 국가명
target_countries = ["미국", "베트남"]
filtered_df = semiconductor_df[semiconductor_df["국가명"].isin(target_countries)]
#filtered_df = df["국가명"].isin["미국", "베트남"]

# 3) 수출금액이 0보다 큰 데이터 추출
final_report = filtered_df[filtered_df["수출금액"] > 0]
# final_report = df["수출금액"] > 0

# step 1 : df[semiconductor_df]
# step 2 : step1[filtered_df]
# step 3 : step2[final_report]

print("--- 상위 10개 ---")
print(final_report.head(10))

final_report.to_csv("semiconductor_report.csv", index=False) # 한글로 깨질 시 인코딩 추가
print("\n분석 결과가 저장되었습니다.")


