from flask import Flask, render_template, request
import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

app = Flask(__name__)

# Load the dataset
df = pd.read_csv("C:/6th sem project/Medicine/Preprocessed_Medicine_Details.csv")
df.columns = df.columns.str.lower()

# Function to search for medicine
def search_medicine(name, top_n=5):
    if name.strip() == "":
        return []

    medicine_names = df["medicine name"].tolist()
    matches = process.extract(name, medicine_names, limit=top_n, scorer=fuzz.token_sort_ratio)

    similar_medicines = []
    for match in matches:
        if match[1] > 50:
            result = df[df["medicine name"] == match[0]]
            similar_medicines.append(result.iloc[0].to_dict())
        if len(similar_medicines) >= top_n:
            break

    if len(similar_medicines) < top_n:
        for match in matches:
            if len(similar_medicines) < top_n:
                result = df[df["medicine name"] == match[0]]
                similar_medicines.append(result.iloc[0].to_dict())

    return similar_medicines

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    query = ""
    if request.method == 'POST':
        query = request.form['medicine_name']
        results = search_medicine(query)
    return render_template('index.html', results=results, query=query)

if __name__ == '__main__':
    app.run(debug=True)
