import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(
    page_icon="🍨",
    page_title="Ice Cream Market"
)

# Dummy data for ice-cream sales
data = {
    "Price (in $)": [1, 2, 3, 4, 5, 6, 7],
    "Quantity Demanded (in scoops)": [70, 60, 50, 40, 30, 20, 10],
    "Quantity Supplied (in scoops)": [10, 20, 30, 40, 50, 60, 70]
}

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Streamlit app
st.title("🍨 Ice Cream Market - Supply and Demand")

st.write("""
Welcome to the Ice Cream Market! Here, we’ll learn how prices are set in the ice cream market. We'll explore how the **price** of ice cream affects the amount people who want to **buy** (demand) and the amount sellers who want to **sell** (supply). 
Let’s dive into this journey step by step!
""")

# Display the demand data in table
st.write("""
<style>
    table {
        margin-left: auto;
        margin-right: auto;
        width: 50%; /* Adjust width as needed */
    }
    td, th {
        text-align: center;
        padding: 8px;
    }
</style>
""" + df[["Price (in $)", "Quantity Demanded (in scoops)"]].to_html(index=False), unsafe_allow_html=True)

# Add a line break
st.write("")

st.write("""    
Let's look at the graph below to see how demand changes with the price.
""")

# Number input for price
price = st.number_input("Enter the Price of Ice Cream (in $)", min_value=1, max_value=7, value=4)
# Calculate the corresponding quantity demanded and supplied based on the price
quantity_demanded = df.loc[df["Price (in $)"] == price, "Quantity Demanded (in scoops)"].values[0]
# Update data based on user input
df.loc[df["Price (in $)"] == price, "Quantity Demanded (in scoops)"] = quantity_demanded

# Plotting demand curve only
plt.figure(figsize=(7, 5))
plt.plot(df["Quantity Demanded (in scoops)"], df["Price (in $)"], label="Demand (People want to buy)", color='blue', linewidth=2, alpha=0.4)
plt.xlabel("Quantity Demanded (in scoops)")
plt.ylabel("Price (in $)")
plt.title("Demand Curve for Ice Cream")
plt.grid(alpha=0.3)
plt.legend(fontsize=7, loc='best')
plt.scatter(df["Quantity Demanded (in scoops)"], df["Price (in $)"], color='blue', s=40, alpha=0.4)
# Highlight the operating point
plt.scatter(quantity_demanded, price, color='k', s=100, zorder=5, label='Operating Point')
# Add annotation for the demand value
plt.annotate(
    f'{quantity_demanded} scoops',
    xy=(quantity_demanded, price),
    xytext=(quantity_demanded + 2, price),
    fontsize=9,
    verticalalignment='center'
)
plt.legend(fontsize=7, loc='best')

st.pyplot(plt)

# Interactive input for external factors
external_factor = st.number_input("Enter the change in quantity demanded due to external factors (e.g., event)", value=20)

# Adjusting the demand data based on external factors
df['New Quantity Demanded (in scoops)'] = df['Quantity Demanded (in scoops)'] + external_factor

# Plotting both original and new demand curves
plt.figure(figsize=(7, 5))
plt.plot(df["Quantity Demanded (in scoops)"], df["Price (in $)"], label="Original Demand", color='blue', linestyle='--', linewidth=2)  # Dotted line for original demand
plt.plot(df["New Quantity Demanded (in scoops)"], df["Price (in $)"], label="New Demand (after event)", color='blue', linewidth=2)  # Solid line for new demand
plt.xlabel("Quantity Demanded (in scoops)")
plt.ylabel("Price (in $)")
plt.title("Effect of External Factors on Demand for Ice Cream")
plt.legend(fontsize=7, loc='best')
plt.grid(alpha=0.3)
plt.scatter(df["Quantity Demanded (in scoops)"], df["Price (in $)"], color='blue', s=50)
plt.scatter(df["New Quantity Demanded (in scoops)"], df["Price (in $)"], color='blue', s=50)

# Display the demand change plot
st.pyplot(plt)

st.write("""
As you can see from the graph:
- The **dotted blue curve** represents the original demand for ice cream.
- The **solid blue curve** shows how demand increases due to external factors, like a popular event.
""")