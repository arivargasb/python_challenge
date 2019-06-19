# Import Dependencies
import pandas as pd

# Create a DataFrame of frames using a dictionary of lists
frame_df = pd.DataFrame({
    "Frame": ["Ornate", "Classical", "Modern", "Wood", "Cardboard"],
    "Price": [15.00, 12.50, 10.00, 5.00, 1.00],
    "Sales": [100, 200, 150, 300, "N/A"]
})
frame_df

# Create a DataFrame of paintings using a list of dictionaries
painting_df = pd.DataFrame([
    {"Painting": "Mona Lisa (Knockoff)", "Price": 25,
     "Popularity": "Very Popular"},
    {"Painting": "Van Gogh (Knockoff)", "Price": 20, "Popularity": "Popular"},
    {"Painting": "Starving Artist", "Price": 10, "Popularity": "Average"},
    {"Painting": "Toddler Drawing", "Price": 1, "Popularity": "Not Popular"}
])
painting_df