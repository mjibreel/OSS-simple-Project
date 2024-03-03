import pandas as pd
from pandas import Series, DataFrame
data_df = pd.read_csv('2019_kbo_for_kaggle_v2.csv')

# (1)
yearList=[2015, 2016, 2017, 2018]
propList=[('H', 'hits'), ('avg', 'batting average'), ('HR', 'homerun'), ('OBP', 'on-base percentage')]

for year in yearList:
  top10subset=data_df.loc[(data_df.year==year), ['year', 'batter_name', 'H', 'avg', 'HR', 'OBP']]
  for (prop, propName) in propList:
    print('Top 10 players in', propName, 'in', year)
    print(top10subset.sort_values(by=prop, ascending=False).head(10).set_index(prop).loc[:,'batter_name'], '\n')

# (2)
positionList=['포수', '1루수', '2루수', '3루수', '유격수', '좌익수', '중견수', '우익수']

for position in positionList:
  highestWarSubset = data_df.loc[(data_df.year == 2018)&(data_df.cp == position), ['batter_name', 'cp', 'war']]
  print(position, 'with the highest war in 2018')
  print(highestWarSubset.sort_values(by='war', ascending=False).head(1).set_index('war').loc[:,'batter_name'], '\n')

# (3)
print('Highest correlation with salary')
print(data_df.loc[:, ['R', 'H', 'HR', 'RBI', 'SB', 'war', 'avg', 'OBP', 'SLG']].corrwith(data_df.salary).sort_values(ascending=False).head(1))