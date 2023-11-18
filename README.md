# Customer Segmentation for the Implementation of New Marketing Campaigns

## GOAL

Customer segmentation is crucial for various marketing strategies, as it allows for targeted approaches based on specific customer groups, enhancing precision and effectiveness in reaching the intended audience. 
In addition to simply having the data, one must also know how to extract information from it. A company provides its customers' information for segmentation to enhance the implementation of marketing strategies.

## PROJECT DESCRIPTION

The project included exploratory data analysis (EDA), preparing the data, grouping data points, and understanding these groups. The clustering utilized the KMeans algorithm, validated through the silhouette score. Visualizing and interpreting these clusters yielded valuable insights for focused marketing efforts and product improvement. This approach is adaptable to other customer datasets, making it a flexible tool within the retail sector.

## EXPLORATORY DATA ANALYSIS .INSIGHTS 

An integral exploration of the initial data is vital for comprehending the dataset's arrangement, attributes, and possible anomalies prior to advancing into subsequent analysis or modeling stages. 

### *AGE 
On average, customers are a mean of 39 years old, with a range of 18 to 70. About a quarter are under 29 (25th percentile), with a median age of 36. Furthermore, most customers, about 75%, are below 49 (75th percentile); indicating a predominantly youthful clientele. The standard deviation of around 14 suggests a reasonably wide range of ages. ![](https://github.com/Bautistao2/Mall-Customers-Segmentation/blob/main/images/Age.jpg)

### *ANNUAL INCOME DISTRIBUTION
 The customers' average annual income is approximately $60.5k, with a standard deviation of around $26.3k, suggesting a significant range in incomes. The lowest recorded income is $15k, while the highest is $137k. The 25th percentile represents an income of $41.5k, the median is $61.5k, and the 75th percentile corresponds to an income of $78k.![](https://github.com/Bautistao2/Mall-Customers-Segmentation/blob/main/images/Annual%20Income.jpg)

### *SPENDING SCORE DISTRIBUTION
 The average spending score is 50.2, with a standard deviation of about 25.8, indicating a broad range of spending behavior. The lowest score recorded is 1, while the highest is 99. The 25th percentile corresponds to a score of 34.75, the median is 50, and the 75th percentile represents a score of 73.![](https://github.com/Bautistao2/Mall-Customers-Segmentation/blob/main/images/Spending%20Score.jpg)


## CLUSTERS 

The identified clusters offer a distinct view of various customer groups delineated by their income and spending patterns. A simplified summary is presented below:![](https://github.com/Bautistao2/Mall-Customers-Segmentation/blob/main/images/clusters.jpg)



Another valuable source of information is to classify customers according to their age and spending score, using the clusters previously identified.![]