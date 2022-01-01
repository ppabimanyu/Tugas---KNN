from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler


def split(data):
    # X = data.drop(columns=["Target", "file"])
    X = data.drop(columns=['file',
                           'energy_0',
                           'homogenity_0',
                           'entrophy_0',
                           'contras_0',
                           # 'energy_45',
                           # 'homogenity_45',
                           # 'entrophy_45',
                           # 'contras_45',
                           # 'energy_90',
                           # 'homogenity_90',
                           # 'entrophy_90',
                           # 'contras_90',
                           # 'energy_135',
                           # 'homogenity_135',
                           # 'entrophy_135',
                           # 'contras_135',
                           'Target'])
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
    return preds, y_test, X_test
