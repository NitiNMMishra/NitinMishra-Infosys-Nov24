import pandas as pd
import matplotlib
import os
import numpy as np  # Import numpy for mathematical functions
matplotlib.use('Agg')  # Use non-interactive backend for saving plots
import matplotlib.pyplot as plt
import seaborn as sns

# Directory for saving the output graphs
output_dir = r"C:\Users\nitin\OneDrive\Documents\Infosys Springboard Internship Files\NitinMishra-Infosys-Nov24\python files\Output graphs"
os.makedirs(output_dir, exist_ok=True)  # Ensure output directory exists

# Load the dataset from the specified file path of the master dataset
file_path = r"C:\Users\nitin\OneDrive\Documents\Infosys Springboard Internship Files\NitinMishra-Infosys-Nov24\datasets\master_dataset\master_dataset.xlsx"
data = pd.read_excel(file_path)

# FEATURE ENGINEERING CODE
# Calculating metrics for analysis

# Calculating Click-Through Rate (CTR) as a percentage
data['CTR'] = (data['Clicks'] / data['Impressions']) * 100  # CTR helps us measure click efficiency

# Conversion Rate in order to show the percentage of impressions that led to sales
data['Conversion Rate'] = (data['Quantity'] / data['Impressions']) * 100

# Calculating sales per click in order to understand effectiveness
data['Sales Per Click'] = data['Quantity'] / data['Clicks']

# Get the day of the week for each corresponding date entry
data['Day of Week'] = data['Day Index'].dt.day_name()

# Calculating daily growth rate in quantity as a percentage
data['Quantity Growth'] = data['Quantity'].pct_change() * 100

# Handling any missing values or infinities that may affect analysis
data = data.fillna(0).replace([float('inf'), -float('inf')], 0)

# VISUALIZATIONS
plt.style.use('ggplot')  # Set the plotting style
plt.rcParams['figure.figsize'] = (12, 6)  # Set figure size for all plots

# 1. CTR Over Time Plot
plt.figure()
plt.plot(data['Day Index'], data['CTR'], label='CTR (%)')
plt.title('CTR Over Time')
plt.xlabel('Date')
plt.ylabel('CTR (%)')
plt.legend()
plt.grid(True)
plt.savefig(os.path.join(output_dir, 'ctr_over_time.png'))

# 2. Conversion Rate Over Time (CTR)
plt.figure()
plt.plot(data['Day Index'], data['Conversion Rate'], label='Conversion Rate (%)', color='orange')
plt.title('Conversion Rate Over Time')
plt.xlabel('Date')
plt.ylabel('Conversion Rate (%)')
plt.legend()
plt.grid(True)
plt.savefig(os.path.join(output_dir, 'conversion_rate_over_time.png'))

# 3. Sales Per Click Distribution
plt.figure()
plt.hist(data['Sales Per Click'], bins=20, alpha=0.7, color='purple', edgecolor='black')
plt.title('Distribution of Sales Per Click')
plt.xlabel('Sales Per Click')
plt.ylabel('Frequency')
plt.savefig(os.path.join(output_dir, 'sales_per_click_distribution.png'))

# 4. Average Quantity by Day of the Week
# Group by day of the week and calculate the average quantity sold on each day
average_quantity = data.groupby('Day of Week')['Quantity'].mean().reindex(
    ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
)
plt.figure()
average_quantity.plot(kind='bar', color='green', alpha=0.7, edgecolor='black')
plt.title('Average Quantity by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Average Quantity')
plt.savefig(os.path.join(output_dir, 'average_quantity_by_day.png'))

# 5. Day-over-Day Growth for Quantity
plt.figure()
plt.hist(data['Quantity Growth'], bins=20, alpha=0.7, color='blue', edgecolor='black')
plt.title('Day-over-Day Growth for Quantity')
plt.xlabel('Growth (%)')
plt.ylabel('Frequency')
plt.savefig(os.path.join(output_dir, 'quantity_growth_distribution.png'))

# 6. Clicks vs Quantity Scatter Plot
plt.figure()
plt.scatter(data['Clicks'], data['Quantity'], alpha=0.7, color='red')
plt.title('Clicks vs Quantity')
plt.xlabel('Clicks')
plt.ylabel('Quantity')
plt.grid(True)
plt.savefig(os.path.join(output_dir, 'clicks_vs_quantity.png'))

# 7. Impressions vs Quantity Scatter Plot
plt.figure()
plt.scatter(data['Impressions'], data['Quantity'], alpha=0.7, color='teal')
plt.title('Impressions vs Quantity')
plt.xlabel('Impressions')
plt.ylabel('Quantity')
plt.grid(True)
plt.savefig(os.path.join(output_dir, 'impressions_vs_quantity.png'))

# 8. Correlation Heatmap (In order to analyze relationships between key metrics)
correlation_matrix = data[['Clicks', 'Impressions', 'Quantity', 'CTR', 'Conversion Rate']].corr()
plt.figure()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.savefig(os.path.join(output_dir, 'correlation_heatmap.png'))

# 9. Monthly Trends (For Quantity, Clicks, and Impressions)
# Resampling data by month and summing up quantities
monthly_data = data.resample('MS', on='Day Index').sum()
plt.figure()
monthly_data[['Quantity', 'Clicks', 'Impressions']].plot()
plt.title('Monthly Trends for Quantity, Clicks, and Impressions')
plt.xlabel('Month')
plt.ylabel('Counts')
plt.legend()
plt.savefig(os.path.join(output_dir, 'monthly_trends.png'))

# 10. Weekday vs Weekend Analysis for Quantity
# Adding a new column to identify weekends
data['Weekend'] = data['Day of Week'].isin(['Saturday', 'Sunday']).astype(int)
weekday_weekend_avg = data.groupby('Weekend')[['Quantity', 'Clicks', 'Impressions']].mean()
plt.figure()
weekday_weekend_avg.plot(kind='bar')
plt.title('Weekday vs Weekend Average for Quantity, Clicks, and Impressions')
plt.xlabel('Weekend (0=Weekday, 1=Weekend)')
plt.ylabel('Average Counts')
plt.savefig(os.path.join(output_dir, 'weekday_weekend_analysis.png'))

# 11. Quarterly Trends
# Convert dates to quarters and summarize the data by quarter
data['Quarter'] = data['Day Index'].dt.to_period('Q')
quarterly_data = data.groupby('Quarter')[['Quantity', 'Clicks', 'Impressions']].sum()
plt.figure()
quarterly_data.plot()
plt.title('Quarterly Trends for Quantity, Clicks, and Impressions')
plt.xlabel('Quarter')
plt.ylabel('Counts')
plt.legend()
plt.savefig(os.path.join(output_dir, 'quarterly_trends.png'))

# 12. Log-Transformed Clicks and Impressions Distributions
# Using log transformations to visualize distributions better
data['Log Clicks'] = np.log1p(data['Clicks'])
data['Log Impressions'] = np.log1p(data['Impressions'])
plt.figure()
plt.hist(data['Log Clicks'], bins=20, alpha=0.7, color='skyblue', edgecolor='black')
plt.title('Log-Transformed Clicks Distribution')
plt.xlabel('Log Clicks')
plt.ylabel('Frequency')
plt.savefig(os.path.join(output_dir, 'log_clicks_distribution.png'))

plt.figure()
plt.hist(data['Log Impressions'], bins=20, alpha=0.7, color='salmon', edgecolor='black')
plt.title('Log-Transformed Impressions Distribution')
plt.xlabel('Log Impressions')
plt.ylabel('Frequency')
plt.savefig(os.path.join(output_dir, 'log_impressions_distribution.png'))

# 13. Box Plot for Outlier Detection in Clicks, Impressions, and Quantity
# Box plot to visualize outliers
plt.figure()
sns.boxplot(data=data[['Clicks', 'Impressions', 'Quantity']])
plt.title('Box Plot for Outlier Detection')
plt.savefig(os.path.join(output_dir, 'outliers_boxplot.png'))
