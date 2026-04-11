#This is the Data Analysis Folder, by me, Aditya Narayan.  
##What I've done is as follows: 
*Used the cleaned churn csv file from the Data Engineering Section. We have swapped the column "Multiple Lines" back to the original with its 3 options
*This file is then put through the following steps
  -Some column titles are changed, as are some mappings. You can see these in the output files, they are self-explanatory
  -any categorical columns are both:
    +Label Encoded: as in a column with values ("yes", "no", "maybe") becomes (1, 2, 3)
    +One-Hot Encoded: as in the same column is split into three columns titles Yes, No and Maybe with a "yes" having the value 1 in the Yes column  
    and 0 and 0 in the No and Maybe Columns
  -Total Charges and Monthly Charges are log-normalized (min-max)
  -Two new columns: OnlineExtras (['Onlinesecurity'] + ['Onlinebackup'] + ['Deviceprotection'] + ['Techsupport']) and StreamingExtras (['Streamingtv'] + ['Streamingmovies'])  
  are created
  -using the one-hot encoded values a correlation matrix is calculated, and the visualizations from that have also been uploaded. THESE VISUALS SHOULD BE RECREATED IN POWERBI/TABLEAU FOR THEM TO LOOK BETTER
  -Only rows with Churned Users are filtered, and then these are used to create clusters (k = 5). The cluster outputs attached to the churned set of customers is also uploaded in churned_customers_clusters.csv
  -the clusters summary is uploaded in cluster_summary.csv
  -the clusters are calculated using label encoded values
  -finally, the one-hot encoded values are used again to create a finetuned logistic regression predictor model. 
  -the Log Regression models metrics are stored in the file: logistic_regression_results.csv
  -I also had Claude create a set of 40 values, 20 of which are customers who will churn and 20 who won't BASED ON THE CLUSTERING RESULTS.
  -the results of this sample data is in the file: logistic_regression_sample_results.csv
* these files can be used to visualize this data as needed. Vanessa's code also has outputs which can be visualized, if needed. You can ask her for that

