import streamlit as st
import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# Load preprocessed dataset
df = pd.read_csv("C:/6th sem project/Medicine/Preprocessed_Medicine_Details.csv")

# Normalize column names
df.columns = df.columns.str.lower()

# Custom CSS for styling and animations
st.markdown(
    """
    <style>
    .title {
        text-align: center;
        font-size: 40px;
        color: #2a9d8f;
        font-weight: bold;
        animation: fadeIn 2s ease-out;
    }
    .section-header {
        color: #264653;
        font-size: 25px;
        font-weight: bold;
        padding-top: 20px;
        padding-bottom: 10px;
    }
    .subsection-header {
        color: #2a9d8f;
        font-size: 18px;
        font-weight: bold;
    }
    .medicine-box {
        background-color: #e9c46a;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 15px;
        animation: fadeInBox 1s ease-out;
        cursor: pointer;
    }
    .medicine-box:hover {
        background-color: #f4a261;
        transform: scale(1.05);
    }
    .img-style {
        border-radius: 10px;
        width: 100px;
        height: 100px;
        object-fit: cover;
    }
    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }
    @keyframes fadeInBox {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Streamlit Title and Instructions
st.markdown(
    '<div class="title">MedSense - Medicine Information Finder</div>',
    unsafe_allow_html=True,
)
st.write(
    """
    Enter a medicine name below to get detailed information including composition, uses, side effects, reviews, and more.
    """
)

# User input for medicine name
medicine_name_input = st.text_input("Enter Medicine Name", "")


# Function to search for similar medicines
def search_medicine(name, top_n=5):
    """Search for a medicine by name and return its details based on fuzzy matching."""
    if name.strip() == "":
        return []

    medicine_names = df["medicine name"].tolist()
    # Extract top N matches with fuzzywuzzy
    matches = process.extract(
        name, medicine_names, limit=top_n, scorer=fuzz.token_sort_ratio
    )

    # If fewer than 'top_n' results match strongly enough, keep retrieving other matches
    similar_medicines = []
    for match in matches:
        if match[1] > 50:  # Lowered threshold to ensure minimum 5 results
            # Get the matched medicine details
            result = df[df["medicine name"] == match[0]]
            similar_medicines.append(result)
        if len(similar_medicines) >= top_n:
            break

    # If fewer than 'top_n' results, keep adding even with lower scores
    if len(similar_medicines) < top_n:
        for match in matches:
            if len(similar_medicines) < top_n:
                result = df[df["medicine name"] == match[0]]
                similar_medicines.append(result)

    return similar_medicines


# Display search results when the user enters a name
if medicine_name_input:
    results = search_medicine(medicine_name_input)

    if results:
        st.subheader(f"Similar Medicines to '{medicine_name_input}':")
        # Creating columns for organized results
        cols = st.columns(3)
        for i, result in enumerate(results):
            medicine_name = result.iloc[0]["medicine name"]
            # Display medicine details in a structured box
            with cols[i % 3]:
                st.markdown(f'<div class="medicine-box">', unsafe_allow_html=True)
                st.write(f"**Match {i + 1}:** {medicine_name}")
                st.write(f"**Composition**: {result.iloc[0]['composition']}")
                st.write(f"**Uses**: {result.iloc[0]['uses']}")
                st.write(f"**Side Effects**: {result.iloc[0]['side_effects']}")
                st.write(f"**Manufacturer**: {result.iloc[0]['manufacturer']}")
                st.write(
                    f"**Excellent Review %**: {result.iloc[0]['excellent review %']}"
                )
                st.write(f"**Average Review %**: {result.iloc[0]['average review %']}")
                st.write(f"**Poor Review %**: {result.iloc[0]['poor review %']}")
                st.image(
                    result.iloc[0]["image url"],
                    caption=f"Image of {medicine_name}",
                    use_column_width=True,
                )
                st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.write("No matching medicines found. Try a different name.")

# Add a footer or some extra information
st.markdown(
    """
    ---
    Built with ❤️ using Streamlit
    """
)

# Run the Streamlit app
if __name__ == "__main__":
    st.set_page_config(
        page_title="MedSense - Medicine Information Finder", page_icon="💊"
    )
