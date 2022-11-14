import pandas as pd

df = pd.read_csv("jongno_미용.csv")

df1 = df.loc[(df['지원학과'] == '뷰티아트과')]

print(df1.head())

df1.to_csv('jongno_b.csv')