from sklearn.linear_model import LogisticRegression

def train_model(df):
    x = df[['task_assigned', 'work_hours']]
    y = df['productivity']

    model = linearRegression()
    model.fit(x, y)
    return model