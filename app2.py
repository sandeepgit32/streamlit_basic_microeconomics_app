import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Dummy data for ice-cream sales
data = {
    "Price (in $)": [1, 2, 3, 4, 5, 6, 7],
    "Quantity Demanded (in scoops)": [70, 60, 50, 40, 30, 20, 10],
    "Quantity Supplied (in scoops)": [10, 20, 30, 40, 50, 60, 70]
}
df = pd.DataFrame(data)

# Equilibrium point for illustration
equilibrium_price = 4
equilibrium_quantity = 40

# User inputs for price floor and price ceiling
price_floor = st.slider("Set Price Floor (in $)", min_value=4, max_value=7, value=5)
price_ceiling = st.slider("Set Price Ceiling (in $)", min_value=1, max_value=4, value=3)

# Plotting with Plotly
fig = go.Figure()

# Add demand curve with increased line thickness
fig.add_trace(go.Scatter(x=df["Quantity Demanded (in scoops)"], y=df["Price (in $)"], 
                         mode='lines', name='Demand', line=dict(color='blue', width=3)))
# Add supply curve with increased line thickness
fig.add_trace(go.Scatter(x=df["Quantity Supplied (in scoops)"], y=df["Price (in $)"], 
                         mode='lines', name='Supply', line=dict(color='green', width=3)))

# Add price floor line with bold annotation
fig.add_hline(y=price_floor, line_dash="dash", line_color='red', 
               annotation_text=f"<b>Price Floor = ${price_floor}</b>", 
               annotation_position="top left", 
               annotation_font=dict(size=14, color='red', family='Arial'))

# Add price ceiling line with bold annotation
fig.add_hline(y=price_ceiling, line_dash="dash", line_color='purple', 
               annotation_text=f"<b>Price Ceiling = ${price_ceiling}</b>", 
               annotation_position="bottom left", 
               annotation_font=dict(size=14, color='purple', family='Arial'))

# Add equilibrium point
fig.add_hline(y=equilibrium_price, line_dash="dot", line_color="black")
fig.add_vline(x=equilibrium_quantity, line_dash="dot", line_color="black")
fig.add_trace(go.Scatter(x=[equilibrium_quantity], y=[equilibrium_price], 
                         mode="markers", marker=dict(color="black", size=12), name="Equilibrium"))

# Layout settings with figure size
fig.update_layout(
    title="Effects of Price Floor and Price Ceiling on the Ice Cream Market",
    xaxis_title="Quantity (in scoops)",
    yaxis_title="Price (in $)",
    legend_title="Legend",
    template="plotly_white",
    margin=dict(l=60, r=60, t=60, b=60),
    height=550,
    width=700,
)

# Update axis titles and tick labels with specific font size
fig.update_xaxes(title_font=dict(size=16, color='black', family='Arial'),
                 tickfont=dict(size=18, color='black'))
fig.update_yaxes(title_font=dict(size=16, color='black', family='Arial'),
                 tickfont=dict(size=18, color='black'))

# Display the plot
st.plotly_chart(fig)
