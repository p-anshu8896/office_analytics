def calculate_kpis(df):
    kpis = {}

    kpis['total_sales'] = df['sales_amount'].sum()
    kpis['average_sales'] = df['sales_amount'].mean()
    kpis['attendance_rate'] = (df['status'] =="present").mean()

    return kpis