from sklearn.metrics import confusion_matrix

y_true = [1, 0, 1, 0,0,1,1]
y_pred = [1, 1, 1, 0,1,0,1]

cm = confusion_matrix(y_true, y_pred)
print(cm)

#confusion matrix format:

#[[TN FP]
# [FN TP]]

#true positive = cm[0][0] ,y_true=1, y_pred=1
#true negative = cm[1][1] ,y_true=0, y_pred=0
#false positive = cm[0][1] ,y_true=0, y_pred=1
#false negative = cm[1][0] ,y_true=1, y_pred=0