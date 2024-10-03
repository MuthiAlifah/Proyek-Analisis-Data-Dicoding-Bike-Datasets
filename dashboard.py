import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Load your dataset
df = pd.read_csv('dashboard/all_data.csv')

# Set up the title and subtitle
st.title("Bike Sharing Data Analysis Submission")
st.subheader("ML-14 Muthia Alifah Rahmi")

# 1. Background
st.markdown("""
### Background
""")
st.markdown(
    """
    <div style="background-color: #f0f0f0; padding: 10px; border-radius: 10px;">
    Bike sharing systems are a new generation of traditional bike rentals where the whole process, from membership, rental, and return, has become automatic. Through these systems, users can easily rent a bike from a particular location and return it to another. Currently, there are over 500 bike-sharing programs around the world with more than 500,000 bicycles. These systems play an important role in traffic, environmental, and health issues, making them an attractive topic for research.

    Unlike other transportation services like buses or subways, bike-sharing systems record the duration, departure, and arrival positions of each trip, creating a rich dataset for mobility sensing in cities. This allows important city events to be detected through data monitoring.
    </div>
    """, unsafe_allow_html=True)


# 2. Business Questions
st.markdown("""
### Business Questions
""")
st.markdown(
    """
    <div style="background-color: #f0f0f0; padding: 10px; border-radius: 10px;">
    Question 1: The company has limited funds. When should additional bikes be stocked?
  
    Question 2: What discount offers should the company provide?
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
### Answer 
""")


# 3. Question 1: When should additional bikes be stocked?
# Create two columns for side-by-side plotting
col1, col2 = st.columns(2)
# Plot 1: Bike Rentals per Hour for Each Season
with col1:
    st.subheader('Question 1 - Bike Rentals per Hour for Each Season')
    
    plt.figure(figsize=(12, 8))
    seasons = ['Musim 1', 'Musim 2', 'Musim 3', 'Musim 4']
    colors = ['maroon', 'orange', 'green', 'blue']

    # Loop for each seasons
    for i in range(4):
        season_data = df[df['season'] == (i + 1)]  # Filtered data by seasons
        avg_rentals_per_hr = season_data.groupby('hr')['cnt'].mean()  # Calculate avarage per hour
        
        plt.plot(avg_rentals_per_hr, color=colors[i], label=seasons[i], linewidth=2)

    plt.title('Bike Rentals per Hour for Each Season', fontsize=10)
    plt.xlabel('Hour (hr)', fontsize=8)
    plt.ylabel('Number of Bike Rentals (cnt)', fontsize=8)
    plt.legend(title='Season', fontsize=8)
    plt.grid()

    # Plotting
    plt.show()    
    st.pyplot(plt)

# Conclusion for Question 1
st.markdown("""
**Conclusion 1:** Based on the analysis, the highest bike rental traffic occurs in season 3 (fall) at 5:00 PM. Therefore, additional bikes should be stocked before season 3 (fall), preferably in season 2 (summer).
""")


# 4. Question 2: What discount offers should the company provide?
with col2:
    st.subheader('Question 2 - Comparison of Casual and Registered Users')

    # Counting the total of casual & registered 
    total_casual = df['casual'].sum()
    total_registered = df['registered'].sum()

    # Pie chart casual & registered 
    labels = ['Casual', 'Registered']
    sizes = [total_casual, total_registered]
    colors = ['maroon', 'orange']

    plt.figure(figsize=(8, 6))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, wedgeprops={'edgecolor': 'black'})
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    # Add title
    plt.title('Comparison of Casual and Registered Users', fontsize=10)

    # Plotting
    st.pyplot(plt)

# Conclusion for Question 2
st.markdown("""
**Conclusion 2:** The analysis shows that 18.83% of users are not yet registered. A recommended discount strategy is to offer a **"New User Discount"** to encourage casual users to register.
""")


# 5. Additional Analysis: Exploring Distribution of Temperature, Humidity, and Wind Speed
st.markdown("### Additional Analysis: Exploring Distribution of Temperature, Humidity, and Wind Speed")
# Plot distributions
plt.figure(figsize=(16, 6))

# Temperature distribution
plt.subplot(1, 3, 1)
plt.hist(df['temp'], bins=20, color='orange', edgecolor='black')
plt.title('Temperature Distribution', fontsize=14)
plt.xlabel('Normalized Temperature', fontsize=12)
plt.ylabel('Frequency', fontsize=12)

# Humidity distribution
plt.subplot(1, 3, 2)
plt.hist(df['hum'], bins=20, color='blue', edgecolor='black')
plt.title('Humidity Distribution', fontsize=14)
plt.xlabel('Normalized Humidity', fontsize=12)
plt.ylabel('Frequency', fontsize=12)

# Wind speed distribution
plt.subplot(1, 3, 3)
plt.hist(df['windspeed'], bins=20, color='green', edgecolor='black')
plt.title('Wind Speed Distribution', fontsize=14)
plt.xlabel('Normalized Wind Speed', fontsize=12)
plt.ylabel('Frequency', fontsize=12)

plt.tight_layout()
st.pyplot(plt)

# Conclusion for Additional Analysis
st.markdown("""
**Conclusion Additional Analysis:** 
- Temperature frequently falls between 0.3 and 0.7 (on a normalized scale), indicating a moderate range most of the time. The distribution is nearly symmetric.
- Humidity ranges between 0.5 and 0.8 (normalized scale), often on the higher side, with the distribution skewed towards higher humidity.
- Wind speed is usually low, with a peak between 0.1 and 0.2 (normalized scale), indicating calm conditions most of the time.
""")