## Fetch Offer Search App
This web application simplifies the process of finding exciting offers by employing natural language processing (NLP) techniques. Users can easily discover the most relevant deals based on their search queries.

Key Features
Offer Matching: The app leverages TF-IDF vectorization and cosine similarity to match user queries with relevant offers.

User-Friendly Interface: A straightforward web interface allows users to input search queries effortlessly.

Top 5 Offers: The app displays the top 5 relevant offers, making the decision-making process easier for users.

Deployment
Access the live app on Heroku: Fetch Offer App.

How to Use
Visit the web app.
Enter your search query in the provided input box.
Click the "Search" button to see the top 5 relevant offers.
Project Structure
Data: Datasets for offers, categories, and brand categories are included.

Model: Core functionality is implemented in model.py, handling offer matching and result presentation.

Web App: The web app, built using Flask, is defined in app.py. HTML templates are stored in the templates folder, while CSS styles are in the static folder.

Dependencies
Python 3.x
Flask
pandas
scikit-learn
numpy
Local Development
Clone the repository.
Install required dependencies using pip install -r requirements.txt.
Run the app locally with python app.py.
Access the app in your browser at http://127.0.0.1:5000/.
Acknowledgments
This project was developed as part of [provide context if applicable].

License
This project is licensed under the MIT License - see the LICENSE.md file for details.