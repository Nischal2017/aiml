from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets

#* Load dataset
iris = datasets.load_iris()
print("Loaded Dataset")
x_train, x_test, y_train, y_test = train_test_split(iris.data,iris.target,test_size = 0.1)
print("Train Test Split is as follows")
print(f"Training Split : {x_train.shape},{y_train.shape}")
print(f"Testing Split : {x_test.shape},{y_test.shape}")

for i in range(0,len(iris.target_names)):
    print(f"Label {i} : {str(iris.target_names[i])}")

classifier = KNeighborsClassifier(n_neighbors=1)
classifier.fit(x_train,y_train)
y_pred = classifier.predict(x_test)

for i in range(0,len(x_test)):
    print(f"Sample {str(x_test[i])} Actual Label: {str(y_test[i])} Predicted Label: {str(y_pred[i])}")

print("Classification Score ", classifier.score(x_test,y_test))

from sklearn.metrics import confusion_matrix, classification_report

print("Confusion Matrix")
print(confusion_matrix(y_test,y_pred))
print("Accuracy Metrics")
print(classification_report(y_test, y_pred))