
import streamlit as st
import matplotlib.pyplot as plt

# Function to calculate future value
def calculate_future_value(principal, rate, years):
    return principal * ((1 + rate / 100) ** years)

# Streamlit UI
st.title("Lumpsum Investment Future Value Calculator")

# User input
principal = st.number_input("Enter Lumpsum Investment Amount (INR)", min_value=1000, value=100000)
cagr = st.number_input("Enter Expected CAGR (%)", min_value=0.0, value=12.0)

years_list = [10, 20, 25]

# Future values
future_values = [calculate_future_value(principal, cagr, y) for y in years_list]
investments = [principal for _ in years_list]
gains = [fv - principal for fv in future_values]

# Display results
st.subheader("Future Value Estimates")
for y, fv, g in zip(years_list, future_values, gains):
    st.write(f"📈 After {y} years: ₹{fv:,.2f} (Gain: ₹{g:,.2f})")

# Plotting
fig, ax = plt.subplots()
ax.plot(years_list, future_values, marker='o', label="Future Value", color='green')
ax.plot(years_list, investments, '--', label="Invested Amount", color='blue')
ax.set_xlabel("Years")
ax.set_ylabel("Value (INR)")
ax.set_title("Investment Growth Over Time")
ax.legend()
ax.grid(True)

# Show graph
st.pyplot(fig)
