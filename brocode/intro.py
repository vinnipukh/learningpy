import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import seaborn as sns

df = pd.read_csv("mydata.csv")
df = df.drop(columns=["No","Name"])

df["Type2"] = df["Type2"].fillna("None")

df = pd.get_dummies(df, columns=["Type1","Type2"])

X = df.drop(columns=["Legendary"])
y = df["Legendary"]

X_train,X_test, y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=0,stratify=y)

print(f"Eğitim seti boyutu: {X_train.shape}")
print(f"Test seti boyutu: {X_test.shape}")

print(df.head())

model = KNeighborsClassifier(n_neighbors=1)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model.fit(X_train,y_train)
y_pred =model.predict(X_test)

print(f"Accuracy on test set: {accuracy_score(y_test, y_pred):.2f}")
print(confusion_matrix(y_test, y_pred))

pca = PCA(n_components=2)
X_pca=pca.fit_transform(X_train)
pca_df = pd.DataFrame(data=X_pca,columns=["PC1","PC2"])
pca_df["Legendary"] = y_train.values

plt.figure(figsize=(6,8))
sns.scatterplot(x="PC1",y="PC2",hue="Legendary", data = pca_df,palette="viridis")
plt.title('Pokémon Dataset - PCA (2 Bileşen)')
plt.show()


