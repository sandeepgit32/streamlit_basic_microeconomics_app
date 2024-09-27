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
Welcome to an imaginary Ice Cream Market! Here, we’ll learn how prices are set in the ice cream market. We'll explore how the **price** of ice cream affects the amount people who want to **buy** (demand) and the amount sellers who want to **sell** (supply). 
Let’s dive into this journey step by step!
""")

# Demand changes with price
st.subheader("🍨 How Does Demand Change with Price?")

st.write("""
On a hot summer day at the park, the ice cream stand attracts many visitors. The price of the ice cream decides how many of them will buy the ice cream and in what quantity.

- If the price is low, more people will want to buy ice cream (high demand).
- If the price is high, fewer people will buy it (low demand).

This relationship shows the **law of demand**, which states that, *all other things being constant* (like consumer preferences, income, and the prices of other goods), the quantity demanded of ice cream decreases as the price increases. The following table shows an example of how demand for ice cream changes with price.
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

col1, col2, col3 = st.columns([1, 12, 1])

with col2:
    # Plotting demand curve only
    plt.figure(figsize=(6, 4))
    plt.plot(df["Quantity Demanded (in scoops)"], df["Price (in $)"], label="Demand curve", color='blue', linewidth=3, alpha=0.4)
    plt.xlabel("Quantity Demanded (in scoops)")
    plt.ylabel("Price (in $)")
    # plt.title("Demand Curve for Ice Cream")
    plt.grid(alpha=0.3)
    plt.legend(fontsize=7, loc='best')
    plt.scatter(df["Quantity Demanded (in scoops)"], df["Price (in $)"], color='blue', s=40, alpha=0.4)
    # Highlight the operating point
    plt.scatter(quantity_demanded, price, color='blue', s=100, zorder=5, label='Current demand')
    # Add annotation for the demand value
    plt.annotate(
        f'{price}$',
        xy=(quantity_demanded, price),
        xytext=(quantity_demanded-1, price-0.4),
        fontsize=9,
        verticalalignment='center'
    )
    plt.annotate(
        f'{quantity_demanded} scoops',
        xy=(quantity_demanded, price),
        xytext=(quantity_demanded + 2, price),
        fontsize=9,
        verticalalignment='center'
    )
    plt.legend(fontsize=7, loc='best')
    st.pyplot(plt)

st.markdown("""
<div style="border: 2px solid #D9E7FF; background-color: #D9E7FF; padding: 10px; border-radius: 5px; margin: 10px 160px; box-shadow: 2px 2px 5px rgba(0.2, 0.2, 0.2, 0.5);">
    <img src="https://img.icons8.com/ios-filled/50/000000/pin.png" alt="Pin" style="width: 20px; height: 20px; margin-right: 10px;">
    <strong>Law of Demand</strong> - The quantity demanded of a product decreases as the price increases, all other things being constant.
</div>
""", unsafe_allow_html=True)
st.write("")

# Supply changes with price
st.subheader("🍨 How Does Supply Change with Price?")

st.write("""
Now, let’s consider the sellers at the ice cream stand. The price of ice cream also affects how much ice cream sellers want to make and sell.

- If the price is high, sellers want to supply more ice cream (high supply).
- If the price is low, sellers will supply less ice cream (low supply).

The reason is because when the price is high, the seller can earn more profit, which incentivizes increased production. Conversely, when prices are low, the potential profits decrease, which discourages production. Sellers may choose to produce less because it may not be worth the cost or effort, leading to lower supply.

This relationship shows the **law of supply**, which states that, *all other things being constant* (like production costs, technology, and the number of people), the quantity supplied of ice cream increases as the price increases. The following table shows an example of how supply of ice cream changes with price.
""")

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
""" + df[["Price (in $)", "Quantity Supplied (in scoops)"]].to_html(index=False), unsafe_allow_html=True)


st.write("")

st.write("""
Let's look at the graph below to see how supply changes with price.
""")

# Number input for price
price = st.number_input("Enter the Price of Ice Cream (in $) ", min_value=1, max_value=7, value=4)
# Calculate the corresponding quantity demanded and supplied based on the price
quantity_supplied = df.loc[df["Price (in $)"] == price, "Quantity Supplied (in scoops)"].values[0]
# Update data based on user input
df.loc[df["Price (in $)"] == price, "Quantity Supplied (in scoops)"] = quantity_supplied

cpl1, col2, col3 = st.columns([1, 12, 1])
with col2:
    # Plotting supply curve only
    plt.figure(figsize=(6, 4))
    plt.plot(df["Quantity Supplied (in scoops)"], df["Price (in $)"], label="Supply curve", color='green', linewidth=3, alpha=0.4)
    plt.xlabel("Quantity Supplied (in scoops)")
    plt.ylabel("Price (in $)")
    # plt.title("Supply Curve for Ice Cream")
    plt.grid(alpha=0.3)
    plt.scatter(df["Quantity Supplied (in scoops)"], df["Price (in $)"], color='green', s=50, alpha=0.4)
    # Highlight the operating points
    plt.scatter(quantity_supplied, price, color='green', s=100, zorder=5, label='Current supply')
    plt.legend(fontsize=7, loc='best')
    # Add annotation for the supply value
    plt.annotate(
        f'{price}$',
        xy=(quantity_supplied, price),
        xytext=(quantity_supplied - 1, price+0.4),
        fontsize=9,
        verticalalignment='center'
    )
    plt.annotate(
        f'{quantity_supplied} scoops',
        xy=(quantity_supplied, price),
        xytext=(quantity_supplied + 2, price),
        fontsize=9,
        verticalalignment='center'
    )
    st.pyplot(plt)


st.markdown("""
<div style="border: 2px solid #D9E7FF; background-color: #D9E7FF; padding: 10px; border-radius: 5px; margin: 10px 160px; box-shadow: 2px 2px 5px rgba(0.2, 0.2, 0.2, 0.5);">
    <img src="https://img.icons8.com/ios-filled/50/000000/pin.png" alt="Pin" style="width: 20px; height: 20px; margin-right: 10px;">
    <strong>Law of Supply</strong> - The quantity supplied of a product increases as the price increases, all other things being constant.
</div>
""", unsafe_allow_html=True)
st.write("")

# Surplus situation
st.subheader("🍨 What Happens If the Price is Too High?")

st.write("""
Now, let’s imagine a situation where the price of ice cream is set **too high**, at **$6**. 
At this price, the quantity supplied is **60 scoops**, but the quantity demanded is only **20 scoops**. 
This means there are **40 scoops** more than people want to buy. This is called a **surplus**.

Let’s take a look at the graph below to see this surplus.
""")

# Number input for price
price = st.number_input("Enter the Price of Ice Cream (in $)  ", min_value=4, max_value=7, value=6)
# Calculate the corresponding quantity demanded and supplied based on the price
quantity_demanded = df.loc[df["Price (in $)"] == price, "Quantity Demanded (in scoops)"].values[0]
quantity_supplied = df.loc[df["Price (in $)"] == price, "Quantity Supplied (in scoops)"].values[0]
# Update data based on user input
df.loc[df["Price (in $)"] == price, "Quantity Demanded (in scoops)"] = quantity_demanded
df.loc[df["Price (in $)"] == price, "Quantity Supplied (in scoops)"] = quantity_supplied

col1, col2, col3 = st.columns([1, 12, 1])

with col2:
    # Plotting demand and supply curves
    plt.figure(figsize=(6, 4))
    plt.plot(df["Quantity Demanded (in scoops)"], df["Price (in $)"], label="Demand curve", color='blue', linewidth=3, alpha=0.4)
    plt.plot(df["Quantity Supplied (in scoops)"], df["Price (in $)"], label="Supply curve", color='green', linewidth=3, alpha=0.4)
    plt.xlabel("Quantity (in scoops)")
    plt.ylabel("Price (in $)")
    # plt.title("Demand and Supply Curves for Ice Cream")
    plt.grid(alpha=0.3)
    plt.legend(fontsize=7, loc='best')
    plt.scatter(df["Quantity Demanded (in scoops)"], df["Price (in $)"], color='blue', s=40, alpha=0.4)
    plt.scatter(df["Quantity Supplied (in scoops)"], df["Price (in $)"], color='green', s=40, alpha=0.4)
    
    # Highlight the operating points
    plt.scatter(quantity_demanded, price, color='blue', s=100, zorder=5)
    plt.scatter(quantity_supplied, price, color='green', s=100, zorder=5)
    
    # Add annotation for the demand value
    plt.annotate(
        f'{quantity_demanded} scoops',
        xy=(quantity_demanded, price),
        xytext=(quantity_demanded + 2, price),
        fontsize=9,
        verticalalignment='center'
    )
    
    # Add annotation for the supply value
    plt.annotate(
        f'{quantity_supplied} scoops',
        xy=(quantity_supplied, price),
        xytext=(quantity_supplied + 2, price),
        fontsize=9,
        verticalalignment='center'
    )
    
    # Shade the surplus and shortage area
    if quantity_demanded > quantity_supplied:
        plt.fill_betweenx([price - 0.1, price + 0.1], quantity_supplied, quantity_demanded, color='red', alpha=0.2, label=f'Shortage: {quantity_demanded - quantity_supplied} scoops')
    elif quantity_supplied > quantity_demanded:
        plt.fill_betweenx([price - 0.1, price + 0.1], quantity_demanded, quantity_supplied, color='purple', alpha=0.2, label=f'Surplus: {quantity_supplied - quantity_demanded} scoops')
    
    plt.legend(fontsize=7, loc='center left')
    st.pyplot(plt)


st.markdown("""
<div style="border: 2px solid #D9E7FF; background-color: #D9E7FF; padding: 10px; border-radius: 5px; margin: 10px 160px; box-shadow: 2px 2px 5px rgba(0.2, 0.2, 0.2, 0.5);">
    <img src="https://img.icons8.com/ios-filled/50/000000/pin.png" alt="Pin" style="width: 20px; height: 20px; margin-right: 10px;">
    <strong>Surplus</strong> occurs for a product when the price is set too <strong>low</strong>, resulting in the quantity demanded exceeding the quantity supplied.
</div>
""", unsafe_allow_html=True)
st.write("")

# Shortage situation
st.subheader("🍨 What Happens If the Price is Too Low?")

st.write("""
Now, let’s imagine a situation where the price of ice cream is set **too low**, at **$2**. 
At this price, the quantity demanded is **60 scoops**, but the quantity supplied is only **20 scoops**. 
This means there are **40 scoops** more people want than sellers can provide. This is called a **shortage**.

Let’s take a look at the graph below to see this shortage.
""")

# Number input for price
price = st.number_input("Enter the Price of Ice Cream (in $)   ", min_value=1, max_value=4, value=2)
# Calculate the corresponding quantity demanded and supplied based on the price
quantity_demanded = df.loc[df["Price (in $)"] == price, "Quantity Demanded (in scoops)"].values[0]
quantity_supplied = df.loc[df["Price (in $)"] == price, "Quantity Supplied (in scoops)"].values[0]
# Update data based on user input
df.loc[df["Price (in $)"] == price, "Quantity Demanded (in scoops)"] = quantity_demanded
df.loc[df["Price (in $)"] == price, "Quantity Supplied (in scoops)"] = quantity_supplied

col1, col2, col3 = st.columns([1, 12, 1])

with col2:
    # Plotting demand and supply curves
    plt.figure(figsize=(6, 4))
    plt.plot(df["Quantity Demanded (in scoops)"], df["Price (in $)"], label="Demand curve", color='blue', linewidth=3, alpha=0.4)
    plt.plot(df["Quantity Supplied (in scoops)"], df["Price (in $)"], label="Supply curve", color='green', linewidth=3, alpha=0.4)
    plt.xlabel("Quantity (in scoops)")
    plt.ylabel("Price (in $)")
    # plt.title("Demand and Supply Curves for Ice Cream")
    plt.grid(alpha=0.3)
    plt.legend(fontsize=7, loc='best')
    plt.scatter(df["Quantity Demanded (in scoops)"], df["Price (in $)"], color='blue', s=40, alpha=0.4)
    plt.scatter(df["Quantity Supplied (in scoops)"], df["Price (in $)"], color='green', s=40, alpha=0.4)
    
    # Highlight the operating points
    plt.scatter(quantity_demanded, price, color='blue', s=100, zorder=5)
    plt.scatter(quantity_supplied, price, color='green', s=100, zorder=5)
    
    # Add annotation for the demand value
    plt.annotate(
        f'{quantity_demanded} scoops',
        xy=(quantity_demanded, price),
        xytext=(quantity_demanded + 2, price),
        fontsize=9,
        verticalalignment='center'
    )
    
    # Add annotation for the supply value
    plt.annotate(
        f'{quantity_supplied} scoops',
        xy=(quantity_supplied, price),
        xytext=(quantity_supplied + 2, price),
        fontsize=9,
        verticalalignment='center'
    )
    
    # Shade the surplus and shortage area
    if quantity_demanded > quantity_supplied:
        plt.fill_betweenx([price - 0.1, price + 0.1], quantity_supplied, quantity_demanded, color='red', alpha=0.2, label=f'Shortage: {quantity_demanded - quantity_supplied} scoops')
    elif quantity_supplied > quantity_demanded:
        plt.fill_betweenx([price - 0.1, price + 0.1], quantity_demanded, quantity_supplied, color='purple', alpha=0.2, label=f'Surplus: {quantity_supplied - quantity_demanded} scoops')

    
    plt.legend(fontsize=7, loc='center left')
    st.pyplot(plt)


st.markdown("""
<div style="border: 2px solid #D9E7FF; background-color: #D9E7FF; padding: 10px; border-radius: 5px; margin: 10px 160px; box-shadow: 2px 2px 5px rgba(0.2, 0.2, 0.2, 0.5);">
    <img src="https://img.icons8.com/ios-filled/50/000000/pin.png" alt="Pin" style="width: 20px; height: 20px; margin-right: 10px;">
    <strong>Sortage</strong> occurs for a product when the price is set too <strong>high</strong>, resulting in the quantity supplied exceeding the quantity demanded.
</div>
""", unsafe_allow_html=True)
st.write("")

# Bringing Supply and Demand Together
st.subheader("🍨 Bringing Supply and Demand Together")

st.write("""
What we have seen:
- At low prices, the demand is high but supply is low, resulting in a **shortage**.
- At high prices, the supply is high but demand is low, leading to a **surplus**.

""")

st.write("""
When there is a **surplus** or **shortage**, sellers and buyers react:
- If there's a surplus (too much ice cream at high prices), sellers will lower their prices to sell more as they want to clear their stock.
- If there's a shortage (too little ice cream at low prices), sellers will raise their prices as they want to maximize their revenue because they know there will be customers who can pay higher price.

Somewhere in the middle, the amount people want to buy equals the amount sellers want to sell. This is called **equilibrium**. The market will naturally move towards this point where everyone is happy!
""")

col1, col2, col3 = st.columns([1, 12, 1])

with col2:
    # Plotting both demand and supply curves for equilibrium
    plt.figure(figsize=(6, 4))
    plt.plot(df["Quantity Demanded (in scoops)"], df["Price (in $)"], label="Demand curve", color='blue', linewidth=3, alpha=0.4)
    plt.plot(df["Quantity Supplied (in scoops)"], df["Price (in $)"], label="Supply curve", color='green', linewidth=3, alpha=0.4)

    # Highlighting the equilibrium point
    equilibrium_price = 4  # From the data
    equilibrium_quantity = 40  # From the data
    plt.scatter([equilibrium_quantity], [equilibrium_price], color='k', zorder=5, label='Equilibrium Point', s=70)

    plt.xlabel("Quantity (in scoops)")
    plt.ylabel("Price (in $)")
    # plt.title("Supply and Demand: Moving Towards Equilibrium")
    # plt.axhline(equilibrium_price, color='red', linestyle='--', linewidth=1, alpha=0.4)
    # plt.axvline(equilibrium_quantity, color='red', linestyle='--', linewidth=1, alpha=0.4)
    plt.legend(fontsize=7, loc='center left')
    plt.grid(alpha=0.3)

    # Add annotation for the demand value
    plt.annotate(
        f'Equilibrium price = {equilibrium_price}$',
        xy=(equilibrium_quantity, equilibrium_price),
        xytext=(equilibrium_quantity - 8, equilibrium_price + 0.5),
        fontsize=9,
        verticalalignment='center'
    )
    
    # Add annotation for the supply value
    plt.annotate(
        f'Equilibrium quantity = {equilibrium_quantity} scoops',
        xy=(equilibrium_quantity, equilibrium_price),
        xytext=(equilibrium_quantity + 2, equilibrium_price),
        fontsize=9,
        verticalalignment='center'
    )

    # Display the final plot
    st.pyplot(plt)

st.markdown("""
<div style="border: 2px solid #D9E7FF; background-color: #D9E7FF; padding: 10px; border-radius: 5px; margin: 10px 160px; box-shadow: 2px 2px 5px rgba(0.2, 0.2, 0.2, 0.5);">
    <img src="https://img.icons8.com/ios-filled/50/000000/pin.png" alt="Pin" style="width: 20px; height: 20px; margin-right: 10px;">
    <strong>Surpluses</strong> prompt sellers to lower prices, while <strong>shortages</strong> encourage them to raise prices. Ultimately, these adjustments lead to an <strong>equilibrium price</strong> where the quantity demanded equals the quantity supplied.
</div>
""", unsafe_allow_html=True)
st.write("")


# External factors affecting demand
st.subheader("🍨 What Happens If Demand Increases Due to External Factors?")

st.write("""
Sometimes, demand for ice cream can change due to external factors. For example, if a popular event is happening nearby (like a concert or festival), more people may want ice cream, increasing the demand even at the same price. 

Imagine that the new quantity demanded at each price increases by 20 scoops due to the event. Let’s see how this change affects the demand curve. 
""")

# Adjusting the demand data
df['New Quantity Demanded (in scoops)'] = df['Quantity Demanded (in scoops)'] + 20

col1, col2, col3 = st.columns([1, 12, 1])

with col2:
    # Plotting both original and new demand curves
    plt.figure(figsize=(6, 4))
    plt.plot(df["Quantity Demanded (in scoops)"], df["Price (in $)"], label="Original Demand", color='blue', linestyle='--', linewidth=3, alpha = 0.4)  # Dotted line for original demand
    plt.plot(df["New Quantity Demanded (in scoops)"], df["Price (in $)"], label="Increased Demand", color='blue', linewidth=3, alpha = 0.4)  # Solid line for new demand
    plt.xlabel("Quantity (in scoops)")
    plt.ylabel("Price (in $)")
    # plt.title("Effect of External Factors on Demand for Ice Cream")
    plt.legend(fontsize=7, loc='best')
    plt.grid(alpha=0.3)
    plt.scatter(df["Quantity Demanded (in scoops)"], df["Price (in $)"], color='blue', s=50)
    plt.scatter(df["New Quantity Demanded (in scoops)"], df["Price (in $)"], color='blue', s=50)

    # Add annotations for each original demand point
    for i in range(len(df)):
        plt.annotate(
            f'{df["Quantity Demanded (in scoops)"][i]} scoops ⟶',
            xy=(df["Quantity Demanded (in scoops)"][i], df["Price (in $)"][i]),
            xytext=(df["Quantity Demanded (in scoops)"][i] + 2, df["Price (in $)"][i]),
            fontsize=9,
            verticalalignment='center'
        )

    # Add annotations for each new demand point
    for i in range(len(df)):
        plt.annotate(
            f'{df["New Quantity Demanded (in scoops)"][i]} scoops',
            xy=(df["New Quantity Demanded (in scoops)"][i], df["Price (in $)"][i]),
            xytext=(df["New Quantity Demanded (in scoops)"][i] + 2, df["Price (in $)"][i]),
            fontsize=9,
            verticalalignment='center'
        )
    # Display the demand change plot
    st.pyplot(plt)

st.write("""
As you can see from the graph:
- The **dotted blue curve** represents the original demand for ice cream.
- The **solid blue curve** shows how demand increases due to external factors, like a popular event.
""")

# External factors affecting demand: Decrease
st.subheader("🍨 What Happens If Demand Decreases Due to External Factors?")

st.write("""
Sometimes, demand for ice cream can decrease due to external factors. For example, if the weather is particularly cold or if a competing ice cream shop opens nearby, fewer people may want ice cream, decreasing the demand even at the same price.

Imagine that the new quantity demanded at each price decreases by 20 scoops due to these factors. Let’s see how this change affects the demand curve.
""")

# Adjusting the demand data for decrease
df['Decreased Quantity Demanded (in scoops)'] = df['Quantity Demanded (in scoops)'] - 20

# Drop the last row to avoid negative values
df1 = df.copy()
df1 = df1.drop(df1.index[-1]).reset_index(drop=True)

col1, col2, col3 = st.columns([1, 12, 1])
with col2:
    # Plotting both original and decreased demand curves
    plt.figure(figsize=(6, 4))
    plt.plot(df1["Quantity Demanded (in scoops)"], df1["Price (in $)"], label="Original Demand", color='blue', linestyle='--', linewidth=3, alpha=0.4)  # Dotted line for original demand
    plt.plot(df1["Decreased Quantity Demanded (in scoops)"], df1["Price (in $)"], label="Decreased Demand", color='blue', linewidth=3, alpha=0.4)  # Solid line for decreased demand
    plt.xlabel("Quantity (in scoops)")
    plt.ylabel("Price (in $)")
    # plt.title("Effect of External Factors on Demand for Ice Cream")
    plt.legend(fontsize=7, loc='best')
    plt.grid(alpha=0.3)
    plt.scatter(df1["Quantity Demanded (in scoops)"], df1["Price (in $)"], color='blue', s=50)
    plt.scatter(df1["Decreased Quantity Demanded (in scoops)"], df1["Price (in $)"], color='blue', s=50)

    # Add annotations for each original demand point
    for i in range(len(df1)):
        plt.annotate(
            f'{df1["Quantity Demanded (in scoops)"][i]} scoops',
            xy=(df1["Quantity Demanded (in scoops)"][i], df1["Price (in $)"][i]),
            xytext=(df1["Quantity Demanded (in scoops)"][i] + 2, df1["Price (in $)"][i]),
            fontsize=9,
            verticalalignment='center'
        )
        
    # Add annotations for each new demand point
    for i in range(len(df1)):
        plt.annotate(
            f'{df1["Decreased Quantity Demanded (in scoops)"][i]} scoops ⟵',
            xy=(df1["Decreased Quantity Demanded (in scoops)"][i], df1["Price (in $)"][i]),
            xytext=(df1["Decreased Quantity Demanded (in scoops)"][i] + 2, df1["Price (in $)"][i]),
            fontsize=9,
            verticalalignment='center'
        )
    # Display the demand change plot
    st.pyplot(plt)

st.write("""
As you can see from the graph:
- The **dotted blue curve** represents the original demand for ice cream.
- The **solid blue curve** shows how demand decreases due to external factors, like colder weather or increased competition.
""")


# Effect of increased demand on equilibrium
st.subheader("🍨 Impact of Increased/Decreased Demand on Equilibrium Price")

st.write("""
- When demand for ice cream increases (like during a special event), more people want to buy ice cream at every price level. This leads to a shift in the demand curve to the right, which can increase the equilibrium price.
- When demand for ice cream decreases (like during a cold snap), fewer people want to buy ice cream at every price level. This leads to a shift in the demand curve to the left, which can decrease the equilibrium price.

Let's visualize how this change affects the equilibrium point.
""")

# User input for demand shift
demand_shift = st.slider("Demand Shift (in scoops)", min_value=-40, max_value=40, value=0, step=10)

# Calculate new demand based on the shift
df["New Quantity Demanded (in scoops)"] = df["Quantity Demanded (in scoops)"] + demand_shift

# Function to find the intersection point
def find_intersection(df):
    for i in range(len(df) - 1):
        if (df["New Quantity Demanded (in scoops)"][i] >= df["Quantity Supplied (in scoops)"][i] and
            df["New Quantity Demanded (in scoops)"][i + 1] <= df["Quantity Supplied (in scoops)"][i + 1]) or \
           (df["New Quantity Demanded (in scoops)"][i] <= df["Quantity Supplied (in scoops)"][i] and
            df["New Quantity Demanded (in scoops)"][i + 1] >= df["Quantity Supplied (in scoops)"][i + 1]):
            # Linear interpolation to find the exact intersection point
            x1, y1 = df["New Quantity Demanded (in scoops)"][i], df["Price (in $)"][i]
            x2, y2 = df["New Quantity Demanded (in scoops)"][i + 1], df["Price (in $)"][i + 1]
            x3, y3 = df["Quantity Supplied (in scoops)"][i], df["Price (in $)"][i]
            x4, y4 = df["Quantity Supplied (in scoops)"][i + 1], df["Price (in $)"][i + 1]
            
            # Calculate intersection point
            denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
            if denom == 0:
                continue  # Lines are parallel
            
            intersect_x = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / denom
            intersect_y = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / denom
            
            return intersect_x, intersect_y
    return None, None

# Find the new equilibrium point
new_equilibrium_quantity, new_equilibrium_price = find_intersection(df)

col1, col2, col3 = st.columns([1, 12, 1])

with col2:
    # Plotting original and new demand and supply curves
    plt.figure(figsize=(6, 4))
    plt.plot(df["Quantity Demanded (in scoops)"], df["Price (in $)"], label="Original Demand", color='blue', linestyle='--', linewidth=3, alpha=0.4)  # Dotted line for original demand
    plt.plot(df["New Quantity Demanded (in scoops)"], df["Price (in $)"], label="New Demand", color='blue', linewidth=3, alpha=0.4)  # Solid line for new demand
    plt.plot(df["Quantity Supplied (in scoops)"], df["Price (in $)"], label="Supply", color='green', linewidth=3, alpha=0.4)

    # Highlighting equilibrium points
    plt.scatter([equilibrium_quantity], [equilibrium_price], color='k', label='Original Equilibrium', s=50)
    if new_equilibrium_quantity is not None and new_equilibrium_price is not None:
        plt.scatter([new_equilibrium_quantity], [new_equilibrium_price], color='red', label=f'New Equilibrium ({new_equilibrium_price}$, {int(new_equilibrium_quantity)})', s=50)

    plt.xlabel("Quantity (in scoops)")
    plt.ylabel("Price (in $)")
    # plt.title("Shift in Demand and Its Impact on Equilibrium")
    plt.legend(fontsize=7, loc='best')
    plt.grid(alpha=0.3)

    # Add annotations for each new demand point
    for i in range(len(df)):
        plt.annotate(
            f'{df["Quantity Demanded (in scoops)"][i]}',
            xy=(df["Quantity Demanded (in scoops)"][i], df["Price (in $)"][i]),
            xytext=(df["Quantity Demanded (in scoops)"][i] + 2, df["Price (in $)"][i]),
            fontsize=9,
            verticalalignment='center'
        )
        plt.annotate(
            f'{df["New Quantity Demanded (in scoops)"][i]}',
            xy=(df["New Quantity Demanded (in scoops)"][i], df["Price (in $)"][i]),
            xytext=(df["New Quantity Demanded (in scoops)"][i] + 2, df["Price (in $)"][i]),
            fontsize=9,
            verticalalignment='center'
        )

    # Display the equilibrium change plot
    st.pyplot(plt)

st.write("""
In the chart:
- The **dotted blue curve** represents the original demand for ice cream.
- The **solid blue curve** shows the new demand after the event, which shifts to the right or left.
- The **green line** represents the supply curve.

As a result of the increased demand, the equilibrium point shifts:
- The original equilibrium point is marked in **black**, where the original demand and supply intersect.
- The new equilibrium point is marked in **red**, where the new demand intersects with the same supply curve.

This shift indicates that at the new equilibrium, the price of ice cream is higher in the event of an increased demand, lower in the event of an decreased demand. This demonstrating how markets respond to changes in consumer behavior!
""")

st.markdown("""
<div style="border: 2px solid #D9E7FF; background-color: #D9E7FF; padding: 10px; border-radius: 5px; margin: 10px 160px; box-shadow: 2px 2px 5px rgba(0.2, 0.2, 0.2, 0.5);">
    <img src="https://img.icons8.com/ios-filled/50/000000/pin.png" alt="Pin" style="width: 20px; height: 20px; margin-right: 10px;">
    <ul> 
        <li>
            <strong>When demand for a product increases</strong>—whether due to an exciting event or changing consumer preferences—the <strong>equilibrium price rises</strong>.
        </li>
        <li>
            <strong>When demand for a product decreases</strong>—whether due to colder weather or increased competition—the <strong>equilibrium price falls</strong>.
        </li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.write("")


# External factors affecting supply
st.subheader("🍨 What Happens If Supply Increases Due to External Factors?")

st.write("""
Sometimes, supply of ice cream can change due to external factors. For instance, if a new supplier enters the market or if production costs decrease, sellers may be willing to supply more ice cream at the same price.

Imagine that the new quantity supplied at each price increases by 20 scoops due to these factors. Let’s see how this change affects the supply curve.
""")

# Adjusting the supply data
df['New Quantity Supplied (in scoops)'] = df['Quantity Supplied (in scoops)'] + 20

col1, col2, col3 = st.columns([1, 12, 1])
with col2:
    # Plotting both original and new supply curves
    plt.figure(figsize=(6, 4))
    plt.plot(df["Quantity Supplied (in scoops)"], df["Price (in $)"], label="Original Supply", color='green', linestyle='--', linewidth=3, alpha=0.4)  # Dotted line for original supply
    plt.plot(df["New Quantity Supplied (in scoops)"], df["Price (in $)"], label="Increased Supply", color='green', linewidth=3, alpha=0.4)  # Solid line for new supply
    plt.xlabel("Quantity (in scoops)")
    plt.ylabel("Price (in $)")
    # plt.title("Effect of External Factors on Supply for Ice Cream")
    plt.legend(fontsize=7, loc='best')
    plt.grid(alpha=0.3)
    plt.scatter(df["Quantity Supplied (in scoops)"], df["Price (in $)"], color='green', s=50)
    plt.scatter(df["New Quantity Supplied (in scoops)"], df["Price (in $)"], color='green', s=50)

    # Add annotations for each original supply point
    for i in range(len(df)):
        plt.annotate(
            f'{df["Quantity Supplied (in scoops)"][i]} scoops ⟶',
            xy=(df["Quantity Supplied (in scoops)"][i], df["Price (in $)"][i]),
            xytext=(df["Quantity Supplied (in scoops)"][i] + 2, df["Price (in $)"][i]),
            fontsize=9,
            verticalalignment='center'
        )

    # Add annotations for each new supply point
    for i in range(len(df)):
        plt.annotate(
            f'{df["New Quantity Supplied (in scoops)"][i]} scoops',
            xy=(df["New Quantity Supplied (in scoops)"][i], df["Price (in $)"][i]),
            xytext=(df["New Quantity Supplied (in scoops)"][i] + 2, df["Price (in $)"][i]),
            fontsize=9,
            verticalalignment='center'
        )
    # Display the supply change plot
    st.pyplot(plt)

st.write("""
As you can see from the graph:
- The **dotted green curve** represents the original supply of ice cream.
- The **solid green curve** shows how supply increases due to external factors, like new suppliers entering the market.
""")

# External factors affecting supply: Decrease
st.subheader("🍨 What Happens If Supply Decreases Due to External Factors?")

st.write("""
Sometimes, the supply of ice cream can decrease due to external factors. For example, if the cost of ingredients rises or if there's a shortage of workers, sellers may be willing to supply less ice cream at the same price.

Imagine that the new quantity supplied at each price decreases by 20 scoops due to these factors. Let’s see how this change affects the supply curve.
""")

# Adjusting the supply data for decrease
df['Decreased Quantity Supplied (in scoops)'] = df['Quantity Supplied (in scoops)'] - 20

# Drop the first row to avoid negative values
df1 = df.copy()
df1 = df1.drop(df1.index[0]).reset_index(drop=True)

col1, col2, col3 = st.columns([1, 12, 1])
with col2:
    # Plotting both original and decreased supply curves
    plt.figure(figsize=(6, 4))
    plt.plot(df1["Quantity Supplied (in scoops)"], df1["Price (in $)"], label="Original Supply", color='green', linestyle='--', linewidth=3, alpha=0.4)  # Dotted line for original supply
    plt.plot(df1["Decreased Quantity Supplied (in scoops)"], df1["Price (in $)"], label="Decreased Supply (after event)", color='green', linewidth=3, alpha=0.4)  # Solid line for decreased supply
    plt.xlabel("Quantity (in scoops)")
    plt.ylabel("Price (in $)")
    # plt.title("Effect of External Factors on Supply for Ice Cream")
    plt.legend(fontsize=7, loc='best')
    plt.grid(alpha=0.3)
    plt.scatter(df1["Quantity Supplied (in scoops)"], df1["Price (in $)"], color='green', s=50)
    plt.scatter(df1["Decreased Quantity Supplied (in scoops)"], df1["Price (in $)"], color='green', s=50)

    # Add annotations for each original supply point
    for i in range(len(df1)):
        plt.annotate(
            f'{df1["Quantity Supplied (in scoops)"][i]} scoops',
            xy=(df1["Quantity Supplied (in scoops)"][i], df1["Price (in $)"][i]),
            xytext=(df1["Quantity Supplied (in scoops)"][i] + 2, df1["Price (in $)"][i]),
            fontsize=9,
            verticalalignment='center'
        )

    # Add annotations for each decreased supply point
    for i in range(len(df1)):
        plt.annotate(
            f'{df1["Decreased Quantity Supplied (in scoops)"][i]} scoops ⟵',
            xy=(df1["Decreased Quantity Supplied (in scoops)"][i], df1["Price (in $)"][i]),
            xytext=(df1["Decreased Quantity Supplied (in scoops)"][i] + 2, df1["Price (in $)"][i]),
            fontsize=9,
            verticalalignment='center'
        )

    # Display the supply decrease plot
    st.pyplot(plt)

st.write("""
As you can see from the graph:
- The **dotted green curve** represents the original supply of ice cream.
- The **solid green curve** shows how supply decreases due to external factors, like increased production costs.
""")


# Effect of increased supply on equilibrium
st.subheader("🍨 Impact of Increased/Decreased Supply on Equilibrium Price")

st.write("""
- When the supply of ice cream increases (like during a bumper harvest), more sellers are willing to sell ice cream at every price level. This leads to a shift in the supply curve to the right, which can decrease the equilibrium price.
- When the supply of ice cream decreases (like during a supply chain disruption), fewer sellers are willing to sell ice cream at every price level. This leads to a shift in the supply curve to the left, which can increase the equilibrium price.

Let's visualize how this change affects the equilibrium point.
""")

# User input for supply shift
supply_shift = st.slider("Supply Shift (in scoops)", min_value=-40, max_value=40, value=10, step=10)

# Calculate new supply based on the shift
df["New Quantity Supplied (in scoops)"] = df["Quantity Supplied (in scoops)"] + supply_shift

# Function to find the intersection point
def find_intersection_supply(df):
    for i in range(len(df) - 1):
        if (df["New Quantity Supplied (in scoops)"][i] >= df["Quantity Demanded (in scoops)"][i] and
            df["New Quantity Supplied (in scoops)"][i + 1] <= df["Quantity Demanded (in scoops)"][i + 1]) or \
           (df["New Quantity Supplied (in scoops)"][i] <= df["Quantity Demanded (in scoops)"][i] and
            df["New Quantity Supplied (in scoops)"][i + 1] >= df["Quantity Demanded (in scoops)"][i + 1]):
            # Linear interpolation to find the exact intersection point
            x1, y1 = df["New Quantity Supplied (in scoops)"][i], df["Price (in $)"][i]
            x2, y2 = df["New Quantity Supplied (in scoops)"][i + 1], df["Price (in $)"][i + 1]
            x3, y3 = df["Quantity Demanded (in scoops)"][i], df["Price (in $)"][i]
            x4, y4 = df["Quantity Demanded (in scoops)"][i + 1], df["Price (in $)"][i + 1]
            
            # Calculate intersection point
            denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
            if denom == 0:
                continue  # Lines are parallel
            
            intersect_x = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / denom
            intersect_y = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / denom
            
            return intersect_x, intersect_y
    return None, None

# Find the new equilibrium point
new_equilibrium_quantity_supply, new_equilibrium_price_supply = find_intersection_supply(df)

col1, col2, col3 = st.columns([1, 12, 1])

with col2:
    # Plotting original and new supply curves
    plt.figure(figsize=(6, 4))
    plt.plot(df["Quantity Supplied (in scoops)"], df["Price (in $)"], label="Original Supply", color='green', linestyle='--', linewidth=3, alpha=0.4)  # Dotted line for original supply
    plt.plot(df["New Quantity Supplied (in scoops)"], df["Price (in $)"], label="New Supply", color='green', linewidth=3, alpha=0.4)  # Solid line for new supply
    plt.plot(df["Quantity Demanded (in scoops)"], df["Price (in $)"], label="Demand", color='blue', linewidth=3, alpha=0.4)

    # Highlighting equilibrium points
    plt.scatter([equilibrium_quantity], [equilibrium_price], color='k', label='Original Equilibrium', s=50)
    if new_equilibrium_quantity_supply is not None and new_equilibrium_price_supply is not None:
        plt.scatter([new_equilibrium_quantity_supply], [new_equilibrium_price_supply], color='red', label=f'New Equilibrium ({new_equilibrium_price_supply}$, {int(new_equilibrium_quantity_supply)})', s=50)

    plt.xlabel("Quantity (in scoops)")
    plt.ylabel("Price (in $)")
    # plt.title("Shift in Supply and Its Impact on Equilibrium")
    plt.legend(fontsize=7, loc='best')
    plt.grid(alpha=0.3)

    # Add annotations for each supply point
    for i in range(len(df)):
        plt.annotate(
            f'{df["Quantity Supplied (in scoops)"][i]}',
            xy=(df["Quantity Supplied (in scoops)"][i], df["Price (in $)"][i]),
            xytext=(df["Quantity Supplied (in scoops)"][i] + 2, df["Price (in $)"][i]),
            fontsize=9,
            verticalalignment='center'
        )

    # Add annotations for each new supply point
    for i in range(len(df)):
        plt.annotate(
            f'{df["New Quantity Supplied (in scoops)"][i]}',
            xy=(df["New Quantity Supplied (in scoops)"][i], df["Price (in $)"][i]),
            xytext=(df["New Quantity Supplied (in scoops)"][i] + 2, df["Price (in $)"][i]),
            fontsize=9,
            verticalalignment='center'
        )

    # Display the supply change plot
    st.pyplot(plt)

st.write("""
In the chart:
- The **dotted green curve** represents the original supply of ice cream.
- The **solid green curve** shows the new supply after the event, which shifts to the right or left.
- The **blue line** represents the demand curve.

As a result of the increased or decreased supply, the equilibrium point shifts:
- The original equilibrium point is marked in **black**, where the original supply and demand intersect.
- The new equilibrium point is marked in **red**, where the new supply intersects with the same demand curve.

This shift indicates that at the new equilibrium, the price of ice cream is lower in the event of an increased supply and higher in the event of a decreased supply. This demonstrates how markets respond to changes in supply conditions!
""")

st.markdown("""
<div style="border: 2px solid #D9E7FF; background-color: #D9E7FF; padding: 10px; border-radius: 5px; margin: 10px 160px; box-shadow: 2px 2px 5px rgba(0.2, 0.2, 0.2, 0.5);">
    <img src="https://img.icons8.com/ios-filled/50/000000/pin.png" alt="Pin" style="width: 20px; height: 20px; margin-right: 10px;">
    <ul> 
        <li>
            <strong>When supply of a product increases</strong>—whether due to a bumper harvest or improved production techniques—the <strong>equilibrium price falls</strong>.
        </li>
        <li>
            <strong>When supply of a product decreases</strong>—whether due to supply chain disruptions or increased production costs—the <strong>equilibrium price rises</strong>.
        </li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.write("")


st.subheader("🍨 Government Interventions - Price Floor and Ceiling")


st.write("""
Sometimes governments intervene to control prices. Let's see how two interventions – **price ceilings** and **price floors** – affect the market and what unintended consequences may arise:

- If the government thinks ice cream sellers are not getting proper price for their ice cream, it might impose a **price floor** above the equilibrium price, for example, at $5. While sellers would love to sell at such a high price, buyers aren't willing to purchase as much. This leads to a surplus of 20 scoops, with unsold ice cream piling up. Sellers may be tempted to sell scoops illegally below the floor price, creating **black market** conditions.

- On the other hand, if the government thinks ice cream is too expensive for everyone to afford, it may set a **price ceiling** below the equilibrium price, say  at $3. While this makes ice cream cheaper for buyers, it creates a shortage of 20 scoopps because at such a low price, sellers aren't willing to supply enough scoops. This scarcity can lead to **black markets**, where people sell ice cream illegally at higher prices.
""")

# User inputs for price floor and price ceiling
price_floor = st.slider("Set Price Floor (in $)", min_value=4, max_value=7, value=5)
price_ceiling = st.slider("Set Price Ceiling (in $)", min_value=1, max_value=4, value=3)

# Calculate the corresponding quantity demanded and supplied based on the price_floor and price_ceiling
quantity_demanded_at_price_floor = df.loc[df["Price (in $)"] == price_floor, "Quantity Demanded (in scoops)"].values[0]
quantity_supplied_at_price_floor = df.loc[df["Price (in $)"] == price_floor, "Quantity Supplied (in scoops)"].values[0]
shortage = quantity_supplied_at_price_floor - quantity_demanded_at_price_floor

quantity_demanded_at_price_ceiling = df.loc[df["Price (in $)"] == price_ceiling, "Quantity Demanded (in scoops)"].values[0]
quantity_supplied_at_price_ceiling = df.loc[df["Price (in $)"] == price_ceiling, "Quantity Supplied (in scoops)"].values[0]
surplus = quantity_demanded_at_price_ceiling - quantity_supplied_at_price_ceiling

# price_floor = 5
# price_ceiling = 3

col1, col2, col3 = st.columns([1, 12, 1])
with col2:
    # Plotting the demand and supply curves with price floor and price ceiling
    plt.figure(figsize=(6, 4))

    # Demand curve
    plt.plot(df["Quantity Demanded (in scoops)"], df["Price (in $)"], label="Demand", color='blue', linewidth=3, alpha=0.4)
    # Supply curve
    plt.plot(df["Quantity Supplied (in scoops)"], df["Price (in $)"], label="Supply", color='green', linewidth=3, alpha=0.4)

    # Price floor line
    plt.axhline(y=price_floor, color='magenta', linestyle='-', linewidth=1.5, alpha=0.4)
    plt.text(8, price_floor + 0.16, "Price Floor = 5$", color='magenta', fontsize=8, va='center')
    plt.text(8, price_floor - 0.2, f"Shortage = {shortage} scoops", color='magenta', fontsize=8, va='center')

    # Price ceiling line
    plt.axhline(y=price_ceiling, color='purple', linestyle='-', linewidth=1.5, alpha=0.4)
    plt.text(8, price_ceiling + 0.16, "Price Ceiling = 3$", color='purple', fontsize=8, va='center')
    plt.text(8, price_ceiling - 0.2, f"Surplus = {surplus} scoops", color='purple', fontsize=8, va='center')


    # Equilibrium line
    # plt.axvline(x=equilibrium_quantity, color='red', linestyle='--', linewidth=1)
    # plt.axhline(y=equilibrium_price, color='red', linestyle='--', linewidth=1)
    plt.scatter([equilibrium_quantity], [equilibrium_price], color='red', zorder=5, label='Equilibrium Point', s=50)

    # Labels and title
    plt.xlabel("Quantity (in scoops)")
    plt.ylabel("Price (in $)")
    # plt.title("Effects of Price Floor and Price Ceiling on the Ice Cream Market")
    plt.legend(fontsize=7, loc='best')
    plt.grid(alpha=0.3)

    # Display the plot
    st.pyplot(plt)

# Explanation of effects

st.markdown("""
<div style="border: 2px solid #D9E7FF; background-color: #D9E7FF; padding: 10px; border-radius: 5px; margin: 10px 160px; box-shadow: 2px 2px 5px rgba(0.2, 0.2, 0.2, 0.5);">
    <img src="https://img.icons8.com/ios-filled/50/000000/pin.png" alt="Pin" style="width: 20px; height: 20px; margin-right: 10px;">
    Government interventions can have unintended consequences on the market:
    <ul>
    <li><strong>Price Ceiling</strong> - If set below equilibrium, it creates a <strong>shortage</strong> as fewer sellers participate. A <strong>black market</strong> may emerge where ice cream is resold at higher prices.</li>
    <li><strong>Price Floor</strong> - If set above equilibrium, it leads to a <strong>surplus</strong> since buyers purchase less. This can drive sellers to the <strong>black market</strong>, selling below the floor.</li>
</ul>
</div>
""", unsafe_allow_html=True)
st.write("")


# # Tax impact section
# st.subheader("🍨 Effect of Tax on Supply and Demand")

# st.write("""
# When a tax is imposed on ice cream sellers, it increases their costs. This typically leads to a leftward shift in the supply curve, resulting in a higher equilibrium price and lower equilibrium quantity.

# Let's visualize how this change affects the equilibrium point.
# """)

# # User input for tax amount
# tax_amount = 1

# # Calculate new supply quantities based on tax
# df["Quantity Supplied After Tax (in scoops)"] = df["Quantity Supplied (in scoops)"] - tax_amount * 10  # Adjust quantity for tax impact

# # Plotting the demand and supply curves with tax effect
# plt.figure(figsize=(6, 4))

# # Demand curve
# plt.plot(df["Quantity Demanded (in scoops)"], df["Price (in $)"], label="Demand", color='blue', linewidth=3)
# # Original supply curve
# plt.plot(df["Quantity Supplied (in scoops)"], df["Price (in $)"], label="Original Supply", color='green', linestyle='--', linewidth=3)
# # Supply curve after tax
# plt.plot(df["Quantity Supplied After Tax (in scoops)"], df["Price (in $)"], label="Supply After Tax", color='orange', linewidth=3)

# # Highlighting equilibrium points
# plt.scatter([equilibrium_quantity], [equilibrium_price], color='k', label='Original Equilibrium Point', s=50)
# new_equilibrium_price = 4.5  # Adjusted equilibrium price
# new_equilibrium_quantity = 35  # Adjusted equilibrium quantity

# # Labels and title
# plt.xlabel("Quantity (in scoops)")
# plt.ylabel("Price (in $)")
plt.title("Effects of Tax on Ice Cream Market")
# plt.axhline(new_equilibrium_price, color='red', linestyle='--', linewidth=1)
# plt.axvline(new_equilibrium_quantity, color='red', linestyle='--', linewidth=1)
# plt.scatter([new_equilibrium_quantity], [new_equilibrium_price], color='red', label='New Equilibrium Point', s=50)
# plt.legend(fontsize=7, loc='best')
# plt.grid(alpha=0.3)

# # Display the plot
# st.pyplot(plt)

# st.write("""
# In the chart:
# - The **blue curve** represents the demand for ice cream.
# - The **dotted green curve** shows the original supply of ice cream.
# - The **orange curve** shows the new supply after the tax is imposed.

# As a result of the tax:
# - The original equilibrium point is marked in **black**, where the original demand and supply intersect.
# - The new equilibrium point is marked in **red**, where the new supply intersects with the same demand curve.

# This shift indicates that at the new equilibrium, the price of ice cream is higher due to the tax, demonstrating how markets respond to taxation!
# """)

# st.markdown("""
# <div style="border: 2px solid #D9E7FF; background-color: #D9E7FF; padding: 10px; border-radius: 5px; margin: 10px 160px; box-shadow: 2px 2px 5px rgba(0.2, 0.2, 0.2, 0.5);">
#     <img src="https://img.icons8.com/ios-filled/50/000000/pin.png" alt="Pin" style="width: 20px; height: 20px; margin-right: 10px;">
#     When a tax is imposed, it not only raises the price for consumers but also reduces the quantity sold in the market.
# </div>
# """, unsafe_allow_html=True)

# st.write("")