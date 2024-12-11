from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score, confusion_matrix
from sklearn.metrics import confusion_matrix


def model_evaluate(x_train, y_train, x_test, y_test,model):
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    c = confusion_matrix(y_test,y_pred)
    print(f'accuracy:{accuracy}, recall:{recall}, precision:{precision}, f1:{f1} ')
    print(f'confusion matrix:\n {c}')
    return accuracy, recall, precision, f1, c


