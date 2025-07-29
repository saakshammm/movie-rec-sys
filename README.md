# 🎬 Movie Recommendation Engine

This is a simple movie recommender system built using content-based filtering. It recommends 8 similar movies based on your selection and displays their posters fetched from TMDB.

🔗 **Live Demo:**  
👉 [https://saakshammm-movie-rec-sys.hf.space](https://saakshammm-movie-rec-sys.hf.space)

---

## 🔧 Features

- Select a movie from a dropdown list  
- Get 8 similar movies with posters  
- Posters fetched live using the TMDB API  
- Works entirely in the browser (via Streamlit)  
- Clean 2-row, 4-column layout

---

## 🚀 How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/saakshammm/movie-rec-sys.git
cd movie-rec-sys
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add your TMDB API key
Create a .env file in the root directory:
```bash
TMDB_API_KEY=your_tmdb_api_key_here
```
### 4. Start the app
```bash
streamlit run app.py
```
## 📦 Dataset and Artifacts
All required files (CSV + pickle) are hosted publicly here:
[📂 [movie-rec]](https://huggingface.co/datasets/saakshammm/movie-rec/tree/main)
Includes:
```angular181html
tmdb_5000_movies.csv
tmdb_5000_credits.csv
movie_list.pkl
similarity.pkl
```

## 📁 Project Structure
```bash
.
├── app.py
├── data/
│   ├── tmdb_5000_credits.csv
│   └── tmdb_5000_movies.csv
├── artifacts/
│   ├── movie_list.pkl
│   └── similarity.pkl
├── requirements.txt
├── .env               
└── README.md
```

## 🌐 Deployment
This app is deployed via Hugging Face Spaces:
🔗 https://saakshammm-movie-rec-sys.hf.space

If deploying elsewhere (e.g., Streamlit Cloud):
* Push your repo to GitHub
* Add your API key as a secret (e.g., TMDB_API_KEY)
* Streamlit or other services will load it securely

## 🧠 Built With
```bash
Streamlit
Scikit-learn
NLTK
Pandas
Requests
The Movie Database (TMDB) API
Pickle
```

## 📸 Example
Select a movie -> Get recommendations -> See poster previews instantly.

![img.png](img.png)

![img_1.png](img_1.png)

## 🔐 Note on Security
Your TMDB API key is loaded securely from environment variables using python-dotenv.
Never hardcode your API keys in public files.

## 👤 Author
Saksham Kumar
[🔗 Hugging Face Profile](https://huggingface.co/saakshammm)
