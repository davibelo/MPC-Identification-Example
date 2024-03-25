import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the CSV file
df = pd.read_csv('identificationTest.csv', delimiter=";", index_col=0)
df.columns = ['T_BOTTOM', 'V_REFLUX', 'C2LPG', 'C5LPG']
print(df)

# Number of columns to plot
num_columns = len(df.columns)

# Creating subplots
fig, axs = plt.subplots(num_columns, 1, figsize=(10, 6))  # Adjust figsize as needed

# Plotting each column on a separate subplot
for i, column in enumerate(df.columns):
    axs[i].plot(df.index, df[column])
    axs[i].set_title(column)
    axs[i].set_xlabel('Index')
    axs[i].set_ylabel('Values')

plt.tight_layout()  # Adjust layout to not overlap subplots
plt.show()
