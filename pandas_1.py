import pandas as pd
import numpy as np

dict_data = {"a" :1, "b":2, "c":3}
series_data = pd.Series(dict_data)
print(type(series_data))
print(series_data)

list_data = ["2026-01-19", 3.14, "abc", 100, True] # 인덱스 번호를 고유의 이름으로 처리
series_data = pd.Series(list_data)
print(type(series_data))
print(series_data)

dict_data = {"c0" : [1, 2, 3], "c1": [4, 5, 6], "c2": [7, 8, 9], "c3": [10, 11, 12], "c4": [13, 14, 15]}
df = pd.DataFrame(dict_data)
print(type(df))
print(df)

# pandas 데이터내용 확인
# .columns : 컬럼명 확인
# .head() : 데이터 상단의 5개행 출력
# .tail() : 데이터 하단의 5개행 출력 / () 내부에 숫자 입력 가능
# .shape() : 데이터의 행과 열의 크기 확인
# .info() : 데이터의 전반적인 정보 확인 / 행과 열의 크키, 컬럼명과 컬럼별 결측치, 데이터 타입 확인
# .type() : 데이터 타입 확인
# ./ 내가 있는 기준으로 하위폴더 이동 - ./data/sample.csv
# ../ 내가 있는 기준으로 상위폴더 이동 - ../data/sample.csv

# 파일 불러오기
# 형식 / 읽기 / 쓰기
# csv / read_csv() / to_csv()
# excel / read_excel() / to_excel()
# json / read_json() / to_json() = 자동화 파일
# html / read_html() / to_html()

titanic = pd.read_csv("Titanic-Dataset.csv")
# print(titanic) - 전체 출력
# print(titanic.columns)
print(titanic.head())
print(titanic.tail(10))
print(titanic.shape)
print(titanic.info())
print(type(titanic))


# pandas에서 특정 열을 선택
# 열 1개 선택 - Series 객체 반환
# 데이터 프레임의 열 데이터 1개만 선택할때 - 2가지 방식이 존재.
# 1. 대괄호[] 안에 열 이름을 따옴표로 함께 입력
# 2. 도트 . 다음에 열 이름을 입력
# 열 n개 선택 = Dataframe 객체 반환
# 데이터프레임의 열 데이터 n개 선택할때 - 이중대괄호[[]] 안에 열 이름을 따옴표로 함께 입력
# *** 만약에 열 1개를 데이터프레임 객체로 추출하려면 [[]] 사용 가능.


# pandas 데이터 필터링
# 1) 불린 인덱싱 true값을 가지는 행만 추출
# 2) .isin() : 각각의 요소가 데이터프레임/시리즈에 존재하는지 확인 후 true/false 반환
# 3) .isna() : 결측 값은 true, 결측 값이 아니면 false 반환 = 비어 있으면 true
# 4) .notna() : 결측 값은 false, 결측 값이 아니면 true 반환

double_columns = titanic
print(double_columns["Age"]>=35)

above35 = double_columns[double_columns["Age"]>=35]
print(above35.head()) # True 값만 추출

# 성별 남자만 추출
male = titanic[titanic["Sex"]=="male"]
print(male.head())
# print(titanic.head())

class_1 = (titanic[titanic["Pclass"].isin([1])])
print(class_1.head())

# print(double_columns.head())
age2040 = double_columns[double_columns["Age"].isin(np.arange(20,41))]
print(age2040.head())

# print(double_columns.head(7))
class_2 = double_columns["Age"].isna()
print(class_2.head(7)) # 비어있는 셀 true 반환

class_3= double_columns["Age"].notna()
print(class_2.head(7)) # 비어있는 셀 false 반환

# 결측 값을 제거하고 누락되지 않은 값을 확인
# 행제거
print(double_columns.head(10))
age5 = double_columns[double_columns["Age"].notna()]
print(age5.head(10))

# 결측치 제거
# .dropna(axis=0) == .dropna() 결측 값들이 들어 있는 행 전체 삭제
# .dropna(axis=1) 결측 값들이 들어 있는 열 전체 삭제

print(titanic.head())
print(titanic.dropna())

print(titanic.dropna(axis=1).head())


# pandas 이름과 인덱스로 특정 행과 열 선택
# .loc[] : 행이름과 열 이름 사용 / DataFrame객체.loc[행이름, 열이름]
# .iloc[] : 행번호와 열번호 사용 / DataFrame객체.iloc[행번호, 열번호]

name35 = titanic.loc[titanic["Age"]>=35, ["Name", "Age"]]
print(name35.head())

name35.iloc[[1,2,3], 0] = "No Name"
print(name35.head())


# pandas 데이터 통계
# .mean() : 평균값
# .median() : 중앙값
# .describe() : 다양한 통계랑 요약
    # mean, std, min, max, 25%, 50%, 75%...
# .agg() : 여러 개의 열에 다양한 함수 적용
# 모든 열에 여러 함수를 매핑 : group.객체.agg([함수1, 함수2, ...])
# 각 열마다 다른 함수를 매핑 : group.객체.agg({"열1": 함수1, "열2": 함수2, ...})
# .groupby() : 그룹별 집계
# .value_counts() : 값의 개수

print("---- 평균 나이 ----")
print(titanic["Age"].mean())

print("---- 중앙값 나이 ----")
print(titanic["Age"].median())

print("---- 나이에 대한 다양한 통계량 ----")
print(titanic["Age"].describe())

print("---- 나이와 요금 평균 및 표준편차 ----")
print(titanic[["Age", "Fare"]].agg(["mean", "std"]))

print("---- 열별 사용자 집계 ----")
agg_dict = {
    "Age": ["min", "max", "mean"],
    "Fare": ["median", "sum"]
}
print(titanic.agg(agg_dict))

print("---- 성별 기준으로 평균 나이 및 요금 ----")
print(titanic.groupby("Sex")[["Age", "Fare"]].mean())

print("---- 선실 등급별 승객 수 ----")
print(titanic["Pclass"].value_counts())

print("---- 성별 인원수 ----")
print(titanic["Sex"].value_counts())

print("---- 새로운 열 country 생성 USA ----")
titanic["Country"] = "USA"
print(titanic.head)

print("---- 기존의 열을 계산해서 새로운 열 생성 ---- ")
titanic["NewAge"] = titanic["Age"]+10
print(titanic)

#20세 미만이면 child, 아니면 adult.
titanic["Agegroup"] = "Adult"
titanic.loc[titanic["Age"]<20, "Agegroup"] = "Child"
print(titanic[["Age", "Agegroup"]].head(10))
print(titanic)

# 데이터 프레임의 마지막 인덱스 확인 후 행 추가
new_index = len(titanic)
print(new_index)
print(titanic.head())

titanic.loc[new_index] = [992, 1,1, "shin", "female", 53,0,0,"Pc123", 50.0, "C123", "S", "USA", 63, "Adult"]
new_data = pd.DataFrame({
   "Name" : ["kim", "lee"],
    "Age" : [22, 33],
    "Sex" : ["male", "female"],
    "Survived" : [1, 0]
})

titanic = pd.concat([titanic, new_data], ignore_index=True)
print(titanic.tail())

# titanic["Name"].str.startswith("Sa") # 문자열이 "Sa"로 시작하는지 여부 반환
# titanic["Age"].astype("str").str.startswith("2") # Age 열의 값을 문자열로 변환한 후 "2"로 시작하는지 여부 반환
# titanic["Age"].astype("str").str.startswith("^82")

# 파일 저장
titanic.to_csv("./sample1.csv", index=False)
titanic.to_excel("./sampele1.xlsx", index=False)
print("파일 저장 완료")