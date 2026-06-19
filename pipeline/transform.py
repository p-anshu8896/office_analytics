import pandas as pd
def transform(att, tasks, sales):
    df = att.merge(tasks, on='employee_id', how='left').merge(sales, on='employee_id', how='left')
    df = df.merge(sales, on=['employee_id', 'date'], how='left')

    df.fillna(0, inplace = True)


    # Feature Engineering
    df['productivity'] = df['tasks_completed'] / (df['tasks_assigned'] + 1)
    df['work_hours'] = 9 # simplified assumption of 9 hours work day


    return df