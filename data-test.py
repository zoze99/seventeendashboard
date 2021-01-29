import pandas as pd

st = pd.read_csv('svt_songtype.csv')


# 원하는 키워드로 TOP5 추천받기
print(st.sort_values('청량', ascending=False).head())

# 4분할 그래프 제작 위한 x축, y축 데이터열 추가
st['xAxis'] = st['아련'] - st['신남']
st['yAxis'] = st['청량'] - st['다크']
print(st.sort_values('청량', ascending=False).head())

