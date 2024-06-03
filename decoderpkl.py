import pickle

with open('pracownicy.pkl', 'rb') as file:
    print(pickle.load(file))