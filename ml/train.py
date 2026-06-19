from ml.model import train_model
import pandas as pd
import joblib

df = pd.read_csv(r"D:\Download Content\office_analytics\data\processed\processed_data.csv")

model = train_model(df)
joblib.dump(model, r"D:\Download Content\office_analytics\models\model.pkl")

print("model trained and saved successfully!")