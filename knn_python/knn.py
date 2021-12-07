from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler


def split(data):
    X = data.drop(columns=["Target", "file"])
    y = data.Target
    return X, y


def predict_knn(train, test, k):
    X_train, y_train = split(train)
    X_test, y_test = split(test)

    scaler = MinMaxScaler()
    scaler.fit(X_train)

    X_train_scaled = scaler.transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train_scaled, y_train)
    preds = knn.predict(X_test_scaled)
    return preds, y_test
