import pandas as pd
from ekstraksi_fitur import ekstrak
from knn import predict_knn

# path_train = glob("filtered_data_fix/train/*/*.jpg")
path_test = input("Patch File : ")
k = int(input("n_neighbors : "))

print(path_test)
# train = ekstrak(path_train)
train = pd.read_csv("train.csv")
test = ekstrak([path_test])

preds, y_test, X_test = predict_knn(train, test, k)
# print(test)
print(' ')
for label in X_test.columns:
    print(f"{label} = {X_test[label][0]}")
print(' ')

print(f"target={y_test[0]} | predict={preds[0]}  -----  True  -----") if y_test[0] == preds[0] else print(
    f"target={y_test[0]} | predict={preds[0]}  -----  False  -----")
