import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

#--------DATA PREP-----------------------


df = pd.read_csv('telco_churn_cleaned.csv')
df = df.drop(columns=['customerID'])
#if total charges is 0, replace it with the monthly charges
#this is interesting because it means the dataset includes customers who have just been signed on, as their tenure is 0 too, and have only been billed for their first month.
df['TotalCharges'] = df.apply(lambda row: row['MonthlyCharges'] if row['TotalCharges'] == 0 else row['TotalCharges'], axis=1)
#replace column names - MultipleLines, InternetService, PaymentMethod with MultLines, IntService, PayMethod
df.columns = df.columns.str.replace('MultipleLines', 'Mult Lines')
df.columns = df.columns.str.replace('InternetService', 'Int Service')
df.columns = df.columns.str.replace('PaymentMethod', 'Pay Method')
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
df.columns = [cols.title() for cols in df.columns]
# #map gender to male = 1 and female = 0
# df['Gender'] = df['Gender'].map({'Male': 1, 'Female': 0})
# df['Gender'] = df['Gender'].astype(int)
# label_cols = ['Mult Lines', 'Int Service', 'Pay Method', 'Contract']
# for col in label_cols:
#     le = LabelEncoder()
#     df[col] = le.fit_transform(df[col])
#     #print the mapping of the original values to the encoded values for each column
#     mapping = dict(zip(le.classes_, le.transform(le.classes_)))
#     print(f'{col} mapping: {mapping}')


categorical_cols = df.select_dtypes(include=['object']).columns
#use one hot encoding to convert categorical variables into numerical format
encoder = OneHotEncoder(drop=None, sparse_output=False)
encoded_cols = encoder.fit_transform(df[categorical_cols]).astype(int)
encoded_df = pd.DataFrame(encoded_cols, columns=encoder.get_feature_names_out(categorical_cols))
#replace the _ with a : in the column names
encoded_df.columns = [col.replace('_', ':') for col in encoded_df.columns]
#caplitalize the first letter of each word in the column names
encoded_df.columns = [col.title() for col in encoded_df.columns]
encoded_df.columns = [col.replace(' ', '') for col in encoded_df.columns]

#combine the encoded columns with the original dataframe
df = pd.concat([df.drop(columns=categorical_cols), encoded_df], axis=1)

#take the ln of total charges and monthly charges to reduce the skewness of the data
df['Totalcharges'] = np.log(df['Totalcharges'])
df['Monthlycharges'] = np.log(df['Monthlycharges'])
#normalize these two columns using min-max normalization
df['Totalcharges'] = (df['Totalcharges'] - df['Totalcharges'].min()) / (df['Totalcharges'].max() - df['Totalcharges'].min())
df['Monthlycharges'] = (df['Monthlycharges'] - df['Monthlycharges'].min()) / (df['Monthlycharges'].max() - df['Monthlycharges'].min())

#---------DATA ANALYSIS-----------------------
#create a new column: OnlineExtras, where for each row: add values from columns OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, and divide by 4 to get the average value of these columns for each row
df['OnlineExtras'] = (df['Onlinesecurity'] + df['Onlinebackup'] + df['Deviceprotection'] + df['Techsupport'])
#StreamingExtras, where for each row: add values from columns StreamingTV and StreamingMovies, and divide by 2 to get the average value of these columns for each row
df['StreamingExtras'] = (df['Streamingtv'] + df['Streamingmovies'])

# #create a correlation matrix
#correlation_matrix = df.corr()
#output the correlation matix to a csv file
##correlation_matrix.to_csv('correlation_matrix.csv')
#plot the correlation matrix, coolwarm grey should be at 0, red should be at 1 and blue should be at -1
# plt.figure(figsize=(20, 20))
# sns.heatmap(correlation_matrix, annot=False, cmap='coolwarm', linewidths=0.5)
# plt.title('Correlation Matrix')
# plt.show()
#plot the correlation matrix for just churn and the other columns
# plt.figure(figsize=(10, 10))
# sns.heatmap(correlation_matrix[['Churn']], vmax=1, vmin=-1, annot=True, cmap='coolwarm', linewidths=0.5)
# plt.title('Correlation Matrix for Churn')
# plt.show()
# plt.figure(figsize=(10, 10))
# sns.heatmap(correlation_matrix[['Churn']].sort_values('Churn', ascending=False), vmax=1, vmin=-1, annot=True, cmap='coolwarm', linewidths=0.5)
# plt.title('Correlation Matrix for Churn')
# plt.show()


#plot the correlation matrix for just churn vs the new columns
# plt.figure(figsize=(10, 10))
# sns.heatmap(correlation_matrix[['Churn', 'OnlineExtras', 'StreamingExtras']], vmax=1, vmin=-1, annot=True, cmap='coolwarm', linewidths=0.5)
# plt.title('Correlation Matrix for Churn vs Online Extras and Streaming Extras') 
# plt.show()

#------Clustering-----------------------
# from sklearn.cluster import KMeans
# churned_df = df[df['Churn'] == 1]
# churned_df = churned_df.drop(columns=['Churn'])
# churned_df['Tenure'] = np.log(churned_df['Tenure'] + 1)
# churned_df['Tenure'] = (churned_df['Tenure'] - churned_df['Tenure'].min()) / (churned_df['Tenure'].max() - churned_df['Tenure'].min())
# clustering_cols = ['Tenure', 'Monthlycharges', 'OnlineExtras', 'StreamingExtras', 'Gender', 'Seniorcitizen', 'Mult Lines', 'Int Service', 'Pay Method', 'Contract', 'Paperlessbilling']


# # #print the unique values of the columns in clustering_cols
# # for col in clustering_cols:
# #     print(f'{col}: {churned_df[col].unique()}')

# # #use the elbow method to find the optimal number of clusters
# # inertia = []
# # for i in range(1, 13):
# #     kmeans = KMeans(n_clusters=i, random_state=42)
# #     kmeans.fit(churned_df[clustering_cols])
# #     inertia.append(kmeans.inertia_)
# # plt.figure(figsize=(10, 6))
# # plt.plot(range(1, 13), inertia, marker='o')
# # plt.title('Elbow Method for Optimal Number of Clusters')
# # plt.xlabel('Number of Clusters')
# # plt.ylabel('Inertia')
# # plt.xticks(range(1, 13))
# # plt.grid()
# # plt.show()


# #k = 5 
# kmeans = KMeans(n_clusters=5, random_state=42)
# churned_df['Cluster'] = kmeans.fit_predict(churned_df[clustering_cols])
# #assign the cluster labels to each row in churned_df
# churned_df['Cluster'] = kmeans.labels_
# #output the cluster labels to a csv file
# churned_df.to_csv('churned_customers_clusters.csv', index=False)

# #print the number of customers in each cluster
# print(churned_df['Cluster'].value_counts())
# #print the average value of each column for each cluster
# print("Average values for each cluster:")
# print(churned_df.groupby('Cluster')[clustering_cols].mean())
# mode_cols = ['Gender', 'Seniorcitizen', 'Mult Lines', 'Int Service', 'Pay Method', 'Contract', 'Paperlessbilling', 'OnlineExtras', 'StreamingExtras']
# avg_mode_cols = ['Tenure', 'Monthlycharges']
# print("Mode values for each cluster:")
# #combine the average and mode values for each cluster into one dataframe
# cluster_summary = pd.concat([churned_df.groupby('Cluster')[avg_mode_cols].mean(), churned_df.groupby('Cluster')[mode_cols].agg(lambda x: x.mode()[0])], axis=1)
# print("Cluster summary:")
# print(cluster_summary)
# #output the cluster summary to a csv file
# cluster_summary.to_csv('cluster_summary.csv')


#-------Logistic Regression-----------------------
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.model_selection import GridSearchCV
#using churn as the target variable and the rest of the columns as features, split the data into training and testing sets with a test size of 20% and a random state of 42
X = df.drop(columns=['Churn'])
y = df['Churn']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#use grid search to find the best hyperparameters for logistic regression
param_grid = {
    'C': [0.01, 0.1, 1, 10, 100],
    'penalty': ['l1', 'l2'],
    'solver': ['liblinear']
}
grid = GridSearchCV(LogisticRegression(), param_grid, refit=True, verbose=0)
grid.fit(X_train, y_train)
#best hyperparameters
print("Best Hyperparameters:", grid.best_params_)
#use the best hyperparameters to train the logistic regression model
best_logistic = grid.best_estimator_
best_logistic.fit(X_train, y_train)
#make predictions on the test set
y_pred = best_logistic.predict(X_test)
#evaluate the model
print("Classification Report:")
print(classification_report(y_test, y_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("Accuracy Score:", accuracy_score(y_test, y_pred))
#print the coefficients of the logistic regression model
coefficients = pd.DataFrame({'Feature': X.columns, 'Coefficient': best_logistic.coef_[0]})
print("Coefficients of the Logistic Regression Model:")
print(coefficients.sort_values(by='Coefficient', ascending=False))
#print the above metrics and coefficients to a csv file
with open('logistic_regression_results.csv', 'w') as f:
    f.write("Best Hyperparameters:\n")
    f.write(str(grid.best_params_) + "\n\n")
    f.write("Classification Report:\n")
    f.write(classification_report(y_test, y_pred) + "\n\n")
    f.write("Confusion Matrix:\n")
    f.write(str(confusion_matrix(y_test, y_pred)) + "\n\n")
    f.write("Accuracy Score:\n")
    f.write(str(accuracy_score(y_test, y_pred)) + "\n\n")
    f.write("Coefficients of the Logistic Regression Model:\n")
    coefficients.to_csv(f, index=False)


#load the file churn_sample_data.csv and make predictions on it using the logistic regression model, output the predictions. drop the customerID column from the sample data. Use the churn column present to evaluate the model's performance on the sample data, and print the classification report, confusion matrix, and accuracy score for the sample data.
sample_df = pd.read_csv('churn_sample_data.csv')
sample_df = sample_df.drop(columns=['CustomerID'])
#columns in the sample data are:Seniorcitizen	Partner	Dependents	Tenure	Phoneservice	Onlinesecurity	Onlinebackup	Deviceprotection	Techsupport	Streamingtv	Streamingmovies	Paperlessbilling	Has_Streaming	Totalcharges	Monthlycharges	Gender:Male	Gender:Female	MultLines:No	MultLines:NoPhoneService	MultLines:Yes	IntService:Dsl	IntService:FiberOptic	IntService:No	PayMethod:BankTransfer	PayMethod:CreditCard	PayMethod:ElectronicCheck	PayMethod:MailedCheck	Contract:Month-To-Month	Contract:OneYear	Contract:TwoYear	OnlineExtras	StreamingExtras Churn
#rearrange the columns in the sample data to match the order of the columns in the training data
sample_df = sample_df[X.columns.tolist() + ['Churn']]


#make predictions on the sample data
sample_X = sample_df.drop(columns=['Churn'])

sample_y = sample_df['Churn']
sample_pred = best_logistic.predict(sample_X)
#evaluate the model on the sample data
print("Classification Report for Sample Data:")
print(classification_report(sample_y, sample_pred))
print("Confusion Matrix for Sample Data:")
print(confusion_matrix(sample_y, sample_pred))
print("Accuracy Score for Sample Data:", accuracy_score(sample_y, sample_pred))
#print the predictions and metrics to a csv file
with open('logistic_regression_sample_results.csv', 'w') as f:
    f.write("Predictions for Sample Data:\n")
    f.write(str(sample_pred) + "\n\n")
    f.write("Classification Report for Sample Data:\n")
    f.write(classification_report(sample_y, sample_pred) + "\n\n")
    f.write("Confusion Matrix for Sample Data:\n")
    f.write(str(confusion_matrix(sample_y, sample_pred)) + "\n\n")
    f.write("Accuracy Score for Sample Data:\n")
    f.write(str(accuracy_score(sample_y, sample_pred)) + "\n\n")
    
