def run_eda(df):
    print(df.describe())
    print(df['department'].value_counts())
    print(df.groupby('region')['sales_amount'].sum())
   