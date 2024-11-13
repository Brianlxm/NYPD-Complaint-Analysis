# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.6
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Load NYPD Complaint Data

# %%
import pandas as pd

# %% tags=["parameters"]
upstream = None
product = {
    'officers': '../products/officers_processed.csv',
    'complaints': '../products/complaints_processed.csv',
    'allegations': '../products/allegations_processed.csv',
    'penalties': '../products/penalties_processed.csv'
}

# %% [markdown]
# ## Load the Data from CSV Files

# %%
# Load each CSV file into a pandas DataFrame
officers_df = pd.read_csv('../data/Civilian_Complaint_Review_Board__Police_Officers.csv')
complaints_df = pd.read_csv('../data/Civilian_Complaint_Review_Board__Complaints_Against_Police_Officers.csv')
allegations_df = pd.read_csv('../data/Civilian_Complaint_Review_Board__Allegations_Against_Police_Officers.csv')
penalties_df = pd.read_csv('../data/Civilian_Complaint_Review_Board__Penalties.csv')

# %%
# Display the first few rows of each dataset
print(officers_df.head())
print(complaints_df.head())
print(allegations_df.head())
print(penalties_df.head())

# %% [markdown]
# ## Save the Loaded Data to the Specified Product Paths

# %%
# Save each DataFrame to the respective product paths
officers_df.to_csv(product['officers'], index=False)
complaints_df.to_csv(product['complaints'], index=False)
allegations_df.to_csv(product['allegations'], index=False)
penalties_df.to_csv(product['penalties'], index=False)
