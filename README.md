# Flask-Learning

# **MODULE 1 — Introduction**

## **1. Overview**

* Flask is a Python Microframework for building web applications. It includes only essential tools (Very lightweight, minimal setup, flexible).
* Built on:
  * **Jinja2** → templating
  * **Werkzeug** → routing + HTTP
  * Flask does NOT enforce project structure.

---

## **2. Installing Flask & Starting Project **

* Use a **virtual environment** (`venv` or PyCharm auto-venv).
* Install Flask:
  ```bash
  python -m pip install flask
  ```
* Create project folder + `app.py`.

---

## **3. Creating First Web Page**

* Minimal Flask application:

  ```python
  from flask import Flask
  app = Flask(__name__)

  @app.route("/")   # maps URL → function (view function).
  def welcome():
      return "Welcome to my Flash Cards application"
  ```

---

## **4. Running Flask Development Server**

Set environment variables:

### macOS / Linux:

```bash
export FLASK_APP=flashcards.py
export FLASK_ENV=development
flask run
```

### Windows:

```cmd
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
```

* Visit: http://127.0.0.1:5000
* Debug enabled by `FLASK_ENV=development`.
* Try alternative run:

  ```bash
  python -m flask run
  ```

---

## **5. Flow of Control**

* Flask waits for HTTP requests → not sequential Python execution.
* Each browser visit triggers a **new GET request**.
* View function executes **every time** page loads.
* Example: `/date` route returning current timestamp.

---

## **6. How Flask Maps URLs to View Functions**

* Use:

  ```python
  import app
  app.app.url_map
  ```
* Lists:

  * URL rules
  * Methods (`GET`, `HEAD`, `OPTIONS`)
  * View function names
* Flask’s default `/static/<filename>` rule serves static files.

---

# ⭐ **MODULE 2 — MODEL-TEMPLATE-VIEW PATTERN (19m 49s)**

## **1. Introducing MTV (1m 41s)**

Flask separates:

* **Model** → Data
* **Template** → UI (HTML)
* **View** → Python function that returns the response

---

## **2. Jinja Templates (5m 29s)**

* Stored inside `/templates` folder.
* Use `render_template()`:

  ```python
  return render_template("home.html")
  ```
* Templates support variables, loops, conditions.

---

## **3. Jinja Variables (3m 24s)**

Python:

```python
return render_template("card.html", card=card)
```

HTML:

```html
<p>{{ card.question }}</p>
```

* Jinja variables use `{{ ... }}` syntax.

---

## **4. Review – Jinja Templates (2m 40s)**

Key points:

* `{{ ... }}` → variables
* `{% ... %}` → logic (if, for, include)
* Templates are clean, separate from Python logic.

---

## **5. Model Layer (3m 16s)**

Simple model:

```python
cards = [
    {"question": "Hola", "answer": "Hello"},
    ...
]
```

Data → passed into templates.

---

## **6. Review – MTV (3m 18s)**

* Separation of concerns → cleaner code.
* View = controller in many frameworks.
* Templates keep UI separate from logic.

---

# ⭐ **MODULE 3 — ADDING LOGIC (28m 56s)**

## **1. Logic Overview (1m 24s)**

* Logic can be inside:

  * Views
  * Templates

---

## **2. URL Parameters (5m 33s)**

```python
@app.route("/card/<int:id>")
def show(id):
    return str(id)
```

Dynamic URLs → show specific card.

---

## **3. Building Links Using url_for (4m 28s)**

```html
<a href="{{ url_for('show', id=3) }}">Card 3</a>
```

* Helps avoid hard-coded links.
* Automatically adjusts paths.

---

## **4. Jinja If Statements (2m 10s)**

```html
{% if score > 5 %}
    <p>Great job!</p>
{% endif %}
```

---

## **5. Jinja For Loops (5m 0s)**

```html
{% for card in cards %}
    <li>{{ card.question }}</li>
{% endfor %}
```

---

## **6. Serving a REST API (3m 47s)**

```python
from flask import jsonify
@app.route("/api/cards")
def api_cards():
    return jsonify(cards)
```

* Returns JSON.
* Used for mobile or frontend apps.

---

## **7. Review (6m 33s)**

Learned:

* Dynamic links
* URL parameters
* JSON API
* Template logic

---

# ⭐ **MODULE 4 — USER INTERACTION (24m 44s)**

## **1. Intro to Forms (54s)**

* Allow user input (e.g., add a new flashcard).

---

## **2. Jinja Form Templates (4m 6s)**

Example form:

```html
<form method="POST">
    <input name="question">
</form>
```

---

## **3. POST Requests in Views (2m 37s)**

```python
from flask import request

if request.method == "POST":
    question = request.form["question"]
```

---

## **4. Redirect After Submit (4m 13s)**

```python
return redirect(url_for("welcome"))
```

* Prevents double submissions.
* Good UX.

---

## **5. Deleting Cards (5m 5s)**

* Example CRUD operation
* Use form submission to delete flashcard.

---

## **6. Forms & Security (3m 28s)**

* Validate input
* Never trust user input
* CSRF tokens (Flask-WTF) recommended

---

## **7. Review (4m 18s)**

* Forms
* POST requests
* Redirects
* Deleting items
* Security basics

---

# ⭐ **MODULE 5 — STYLING & TEMPLATE INHERITANCE (9m 43s)**

## **1. Intro (51s)**

* Use CSS + base templates to style entire app.

---

## **2. Adding Stylesheet (3m 6s)**

CSS stored in `/static/style.css`
Link inside template:

```html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
```

---

## **3. Template Inheritance (3m 38s)**

`base.html`:

```html
{% block content %}{% endblock %}
```

Child template:

```html
{% extends "base.html" %}
{% block content %}
<h1>Flashcards</h1>
{% endblock %}
```

---

## **4. Review (2m 6s)**

* DRY templates
* Clean UI
* Reusable layout with inheritance

---

# ⭐ **MODULE 6 — DEPLOYING FLASK (11m 55s)**

## **1. Intro (2m 19s)**

* Development server ≠ Production ready
* Use WSGI server like Gunicorn

---

## **2. Deploying on Linux with Gunicorn (5m 46s)**

Commands:

```bash
pip install gunicorn
gunicorn flashcards:app
```

* Nginx recommended as reverse proxy
* Run app on cloud (AWS/Ubuntu)

---

## **3. Review (3m 48s)**

* Deployment workflow:
  virtualenv → code → Gunicorn → Nginx → domain → HTTPS
* Final step for making Flask app live.

---

# 🎯 **FINAL OUTPUT**

You have complete notes covering:

* Basics → Templates → MVC → Logic → REST → Forms → CSS → Deployment
* Entire Pluralsight course converted to **exam-ready and interview-ready content**

---

If you want, I can also generate:

📄 **PDF Version**
📚 **Flashcards Project (Full Code)**
📝 **Practice Questions for Each Module**
🧪 **Assignments + Mini Projects**

Just tell me!
