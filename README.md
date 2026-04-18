# 📘 MySQL Practice 102

This project is a simple **Flask-based web application** that connects to a **Supabase database** and displays data from a table called ```instruments```.

---

## 🚀 Features

- Connects to Supabase using environment variables
- Fetches data from a database table
- Displays results dynamically in a web page
- Built with Flask for simplicity and learning purposes

---

## 🛠️ Technologies Used

- Python
- Flask
- Supabase Python Client
- dotenv (for environment variables)

---

## 📂 Project Structure

```
MySQL-Practice-102/
│
├── app.py              # Main Flask application
├── .env               # Environment variables (not included in repo)
├── requirements.txt   # Dependencies
└── README.md          # Project documentation
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```
git clone https://github.com/Kaveeshamalindi/MySQL-Practice-102.git
cd MySQL-Practice-102
```

### 2. Create a Virtual Environment (Optional but Recommended)

```
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a .env file in the root directory and add:

```
SUPABASE_URL=your_supabase_url
SUPABASE_PUBLISHABLE_KEY=your_supabase_key
```

### 5. Run the Application

```
python app.py
```

### 6. Open in Browser

Go to:

```
http://127.0.0.1:5000/
```

You should see a list of instruments fetched from your database.

### 📌 Example Output

```
Instruments
- violin
- viola
- cello
- drums
- flute
- trumpet
```

---

## 📖 How It Works


- The app connects to Supabase using credentials stored in ```.env```
- It queries the ```instruments``` table
- Data is returned and displayed as a simple HTML list

---

## ⚠️ Notes

- Ensure your Supabase table is named ```instruments```
- The table should have a column named ```name```
- Never expose your API keys publicly

--- 

## 🤝 Contributing

Feel free to fork this repository and improve it!

---

## 📄 License

This project is for educational purposes.

---


