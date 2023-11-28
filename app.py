from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__, template_folder='templates')  # Change 'template' to 'templates'

# Import your functions and necessary libraries
from model import get_relevant_offers_df, preprocess_text, tfidf_matrix, offers_df

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']

        if user_input:
            # Get relevant offers
            result_df = get_relevant_offers_df(user_input, tfidf_matrix, offers_df)

            # Display results
            return render_template('index.html', result_df=result_df.to_html())
    
    return render_template('index.html', result_df=None)

if __name__ == '__main__':
    app.run(debug=True)
