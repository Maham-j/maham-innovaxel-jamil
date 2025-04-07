
# 🔗 URL Shortener API

A lightweight URL shortening service built with **Flask** and **SQLite**. Generate short links, update them, track visits, and delete when done — all via API.

---

## ⚙️ Tech Stack
- 🐍 Python (Flask)
- 🗃️ SQLite (via SQLAlchemy)
- 📬 RESTful API

---

## 🚀 Features
- ✂️ Shorten long URLs
- 🔁 Redirect to original URL
- ✏️ Update existing short links
- 📊 Track access counts
- 🗑️ Delete short URLs

---

## ▶️ Getting Started

1. **Clone the repo**  
   ```bash
   git clone <repo-url>
   cd url_shortener
   ```

2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**  
   ```bash
   python app.py
   ```

4. Server runs at:  
   🌐 `http://127.0.0.1:5000`

---

## 📮 API Endpoints

| Method | Route                             | Functionality           |
|--------|-----------------------------------|--------------------------|
| POST   | `/shorten`                        | Create a short URL       |
| GET    | `/shorten/<short_code>`           | Retrieve original URL    |
| PUT    | `/shorten/<short_code>`           | Update the URL           |
| DELETE | `/shorten/<short_code>`           | Delete the short URL     |
| GET    | `/shorten/<short_code>/stats`     | Get visit count          |

---

## 🧪 Example (PowerShell)

```powershell
curl -Method POST http://127.0.0.1:5000/shorten `
-Headers @{"Content-Type"="application/json"} `
-Body '{"url":"https://www.google.com"}'
```

---

## 📂 Folder Structure
```
url_shortener/
├── app.py
├── database.py
├── routes.py
├── models.py
└── requirements.txt
```

---

## 👩‍💻 Author

Made with 💻 by **[MAHAM JAMIL]**

---

