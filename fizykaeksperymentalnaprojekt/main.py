import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import xgboost as xgb
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

df = pd.read_excel('./../3D_ML.xlsx')

X = df[['Moc', 'Prędkość skanowania', 'grubość wartswy']]
y = df['porowatosc']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

reg = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100, learning_rate=0.1, max_depth=5, random_state=0)

reg.fit(X_train, y_train)

print(reg.predict(X_test))