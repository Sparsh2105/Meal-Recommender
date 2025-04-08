# 🥗 AI Meal Recommender API

This is a FastAPI-based backend API that recommends meals based on user input like diet preference, cuisine type, and calorie range using the Spoonacular API.

---

## 🚀 Features

- 🔍 Meal recommendation based on filters
- ⚡ FastAPI backend for rapid development
- ✅ Input validation with Pydantic models
- 🔄 Integration with Spoonacular Recipe API
- 🧪 Testable via Swagger UI (`/docs`)
- 🌐 Ready for deployment

---

## 🧰 Technologies Used

| Tool              | Purpose                              |
|-------------------|--------------------------------------|
| **FastAPI**       | Web framework for building APIs      |
| **Pydantic**      | Data validation using Python models  |
| **Requests**      | For calling external REST APIs       |
| **Uvicorn**       | ASGI server for FastAPI              |
| **Spoonacular API** | External recipe data source       |
| **Python 3.10+**  | Primary programming language          |

---

## 📁 Folder Structure

```bash
meal-recommender-api/
├── main.py               # FastAPI app entry point
├── models.py             # Pydantic request model
├── routers/              # Route folder
│   └── meal.py           # Meal recommendation endpoint
├── requirements.txt      # Dependencies list
└── README.md             # Project documentation


