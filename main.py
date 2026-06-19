from pipeline.extract import extract_all
from pipeline.cleaning import clean_data
from pipeline.transform import transform
from pipeline.load import load_data
from database.db import save_to_db
from analysis.eda import run_eda
from analysis.kpi import calculate_kpis

att, tasks, sales = extract_all()
att, tasks, sales = clean_data(att, tasks, sales)

df = transform(att, tasks, sales)

load_data(df)
save_to_db(df)

run_eda(df)
kpis = calculate_kpis(df)

print("KPIs:", kpis)