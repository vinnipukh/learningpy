import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score,KFold

df = pd.read_csv("train.csv")
df = df.drop(columns=["PassengerId","Name","Ticket","Cabin"])

df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
df["Fare"] = df["Fare"].fillna(df["Fare"].median())

df = pd.get_dummies(df,columns=["Sex","Pclass","Embarked"],drop_first=True,dtype=int)

X = df.drop(columns="Survived")
y = df["Survived"]

X_train,X_test,y_train,y_test= train_test_split(X,y,test_size=0.3,random_state=0,stratify=y)

print(f"Eğitim seti boyutu: {X_train.shape}")
print(f"Test seti boyutu: {X_test.shape}")

#print(df.head())

model = KNeighborsClassifier(n_neighbors=1)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model.fit(X_train,y_train)
y_pred = model.predict(X_test)

print(f"Accuracy Score: {accuracy_score(y_test,y_pred)}")
print(confusion_matrix(y_test,y_pred))

scaler_cv = StandardScaler()
X_scaled = scaler_cv.fit_transform(X)

model_cv = KNeighborsClassifier(n_neighbors=11)
kf = KFold(n_splits=5,shuffle=True,random_state=0)
scores = cross_val_score(model_cv, X_scaled, y, cv=kf)

print(f"Her katman için skorlar: {scores}")
print(f"Ortalama Başarı: {scores.mean():.2f} (+/- {scores.std() * 2:.2f})")
