# import streamlit as st
import pandas as pd
import numpy as np

# pandas(pd)를 이용해 csv를 읽을 것임.
trade = pd.read_csv("./raw_trade_data.csv", encoding='cp949')
# print(trade)

# 1. hs 85 시작하는 것
print(trade.info())
cond_hs = trade["hs_code"].astype(str).str.startswith("85")
print(cond_hs.head())

# 2. 미국 + 베트남
cond_country = trade["국가명"].isin(["미국","베트남"])
print(cond_country)

# 3. 수출금액 0원인 데이터 제거
print(trade.head(10))
cond_value = trade["수출금액"]>0
print(cond_value)

# 4. 최종 결합
# step1 = trade[cond_hs]
# step2 = step1[cond_country]
# step3 = step2[cond_value]

step3 = trade[cond_hs & cond_country & cond_value]

print("상위 10개 데이터 확인")
print(step3.head(10))

# trade.to_csv("저장할 파일명.csv",)


# 2번 문제 - for문 / 쉬운 방법

# 1. 중량 컬럼 결측치 처리
print(trade.head(15))
hs_mean = trade.groupby("hs_code")["중량"].mean() # 같은 hs코드를 묶어주는 역할.
print(hs_mean)

for hs in hs_mean.index :
    # 1. 현재 순서의 HS코드에 해당하는 평균값을 가져오기
    avg_va1 = hs_mean[hs]
    # 2. 원본 데이터에서 해당 HS코드이면서 중량이 비어있는 행만 찾기
    target = (trade["hs_code"] == hs & trade["중량"].isna())
    # 3. 해당되는 칸에만 평균값 대입
    trade.loc[target, "중량"] = avg_va1

# trade.loc[trade["중량"].isna()]=0

# 2. 수입 수출 바꿔 주기
trade.loc[trade["수출입구분"] == "Export", "수출입구분"] = "수출"
trade.loc[trade["수출입구분"] == "Import", "수출입구분"] = "수입"

# 3. 수출금액 단위 변화 - 원=>백만달러 - (금액/1470)/1000000
exchange_rate = 1470
trade["수출금액_M_USD"] = (trade["수출금액"]/1470/1000000)


# 4. 데이터 타입 확인 + 최종확인
print("\n ----- [최종 데이터 확인] -----")
print(trade.dtypes)

print("\n ----- [클렌징 결과 샘플 확인] -----")
print(trade[["날짜", "hs_code", "수출입구분", "수출금액_M_USD"]].head())

# 5. 저장 파일 만들기
trade.to_csv("./cleaned_trade_data.csv", encoding = "cp949")
print("과제 2 완료 'cleaned_trade_data.csv'가 저장되었습니다.✅")