# Fetch Offer Search App
This web application simplifies the process of finding exciting offers by employing natural language processing (NLP) techniques. Users can easily discover the most relevant deals based on their search queries.

### Key Features
- **Offer Matching**: The app leverages TF-IDF vectorization and cosine similarity to match user queries with relevant offers.

-  User-Friendly Interface: A straightforward web interface allows users to input search queries effortlessly.

- Top 5 Offers: The app displays the top 5 relevant offers, making the decision-making process easier for users.

### Deployment
Access the live app on Heroku: [Fetch Offer App](https://fetchofferapp-844f25b2b0ba.herokuapp.com/)!

### How to Use
1. Visit the web app.
2. Enter your search query in the provided input box.
3. Click the "Search" button to see the top 5 relevant offers.

### Project Structure
- Data: Datasets for offers, categories, and brand categories are included.

- Model: Core functionality is implemented in model.py, handling offer matching and result presentation.

- Web App: The web app, built using Flask, is defined in app.py. HTML templates are stored in the templates folder, while CSS styles are in the static folder.

### Dependencies 
###### check requirements.txt
- Python 3.11.5
- Flask
- pandas
- scikit-learn
- numpy

### Local Development
1. Clone the repository.
2. Install required dependencies using pip install -r requirements.txt.
3. Run the app locally with python app.py.
4. Access the app in your browser at http://127.0.0.1:5000/.

### Acknowledgments
This project was developed as part of with the goal of the project was to create a web application that facilitates the search for relevant offers using natural language processing (NLP) techniques. The application allows users to input search queries, and it matches these queries with the most relevant offers from a dataset. The primary objectives included building a user-friendly interface, implementing offer matching using TF-IDF vectorization and cosine similarity, and presenting the top 5 relevant offers to users. The project aimed to simplify the process of discovering and accessing valuable deals for users.

