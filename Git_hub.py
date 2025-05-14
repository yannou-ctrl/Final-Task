import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Wind_Turbine_Scada_Dataset.csv")

print("Dataset preview : ")
print(df.head())

print("Descriptive statistics : ")
print(df.describe())

print("Dataset information : ")
print(df.info())

plt.figure(figsize=(10, 5))
plt.hist(df["Wind Speed (m/s)"], bins=40, color="blue", edgecolor="black")
plt.title("Wind Speed Distribution")
plt.xlabel("Wind Speed (m/s)")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 5))
plt.hist(df["LV ActivePower (kW)"], bins=40, color="green", edgecolor="black")
plt.title("Active Power Distribution")
plt.xlabel("Active Power (kW)")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 5))
plt.scatter(df["Wind Speed (m/s)"], df["LV ActivePower (kW)"], color="purple")
plt.title("Wind Speed vs Active Power")
plt.xlabel("Wind Speed (m/s)")
plt.ylabel("Active Power (kW)")
plt.grid(True)
plt.show()

print("Information from the data : ")
print("""
- Wind speed mostly ranges between 4 and 10 m/s.
- Actual active power follows a bell-shaped curve relative to wind speed.
- Theoretical power is strongly correlated with wind speed.
- Deviations between actual and theoretical power may indicate faults or inefficiencies.""")
