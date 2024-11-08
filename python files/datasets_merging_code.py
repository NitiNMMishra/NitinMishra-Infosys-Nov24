import pandas as pd  # Import the pandas library for data manipulation and analysis

# Load each Excel file into a DataFrame
google_clicks = pd.read_excel(r'C:\Users\nitin\OneDrive\Documents\Infosys Springboard Internship Files\NitinMishra-Infosys-Nov24\datasets\ProductA_google_clicks.xlsx')
fb_impressions = pd.read_excel(r'C:\Users\nitin\OneDrive\Documents\Infosys Springboard Internship Files\NitinMishra-Infosys-Nov24\datasets\ProductA_fb_impressions.xlsx')
quantity = pd.read_excel(r'C:\Users\nitin\OneDrive\Documents\Infosys Springboard Internship Files\NitinMishra-Infosys-Nov24\datasets\ProductA.xlsx')

# Merge the three DataFrames on the common column "Day Index"
# This combines all data into a single master dataset
master_dataset = google_clicks.merge(fb_impressions, on="Day Index").merge(quantity, on="Day Index")

# Save the merged dataset to an Excel file in the specified directory
master_dataset.to_excel("C:/Users/nitin/OneDrive/Documents/Infosys Springboard Internship Files/NitinMishra-Infosys-Nov24/datasets/master_dataset/master_dataset.xlsx", index=False)

# Print a confirmation message when the process is complete
print("Done")
