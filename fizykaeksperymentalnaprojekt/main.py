import pandas as pd
import matplotlib.pyplot as plt
import xgboost as xgb
from sklearn.model_selection import train_test_split

df = pd.read_excel('./../3D_ML.xlsx')

X = df[['Moc', 'Prędkość skanowania', 'grubość wartswy']]
y = df['porowatosc']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

reg = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100, learning_rate=0.1, max_depth=5, random_state=0)
reg.fit(X_train, y_train)

predictions = reg.predict(X_test)

y_pred = y.copy()
y_pred.iloc[-20:] = predictions[:20]

plt.figure(figsize=(12, 4))
plt.scatter(df['Moc'], df['porowatosc'], label='Dane z pomiaru')
plt.scatter(df['Moc'].iloc[-20:], y_pred.iloc[-20:], label='Predykcja')
plt.xlabel('Moc [W]')
plt.ylabel('Porowatosc')
plt.title('Porowatosc w zaleznosci od mocy')
plt.legend()
plt.show()

plt.figure(figsize=(12, 4))
plt.scatter(df['Prędkość skanowania'], df['porowatosc'], label='Dane z pomiaru')
plt.scatter(df['Prędkość skanowania'].iloc[-20:], y_pred.iloc[-20:], label='Predykcja')
plt.xlabel('Prędkość skanowania')
plt.ylabel('Porowatosc')
plt.title('Porowatosc w zaleznosci od prędkości skanowania')
plt.legend()
plt.show()

plt.figure(figsize=(12, 4))
plt.scatter(df['grubość wartswy'], df['porowatosc'], label='Dane z pomiaru')
plt.scatter(df['grubość wartswy'].iloc[-20:], y_pred.iloc[-20:], label='Predykcja')
plt.xlabel('Grubość warstwy')
plt.ylabel('Porowatosc')
plt.title('Porowatosc w zaleznosci od grubości warstwy')
plt.legend()
plt.show()

plt.figure(figsize=(15,6))
plt.plot(df.index, df['porowatosc'], 'o', label='Dane z pomiaru')
plt.plot(df.index[-20:], y_pred.iloc[-20:], 'o', label='Predykcja')
plt.xlabel('Index')
plt.ylabel('Porowatosc')
plt.title('Porowatość w zależności kolejności pomiaru (dowód niezależności pomiaru od parametrów mocy, prędkości skanowania i grubości warstwy')
plt.legend()
plt.show()
