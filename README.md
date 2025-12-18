# **MODULE 1 — Introduction**

## **1. Overview**

* Flask is a Python Microframework for building web applications. It includes only essential tools (very lightweight, minimal setup, flexible).
* Built on:
  * **Jinja2** → templating
  * **Werkzeug** → routing + HTTP
  * Flask does NOT enforce project structure.

---

## **2. Installing Flask**

* Use a **virtual environment** (`venv` or PyCharm auto-venv).
* Install Flask:
  ```bash
  python -m pip install flask
  ```
* Create project folder + `app.py`.

---

## **3. Creating Web Page**

* Minimal Flask application:

  ```python
  from flask import Flask
  app = Flask(__name__)

  @app.route("/")   # maps URL → function (view function).
  def welcome():
      return "Welcome to my Flash Cards application"
  ```

---

## **4. Running Flask**

Set environment variables:

**macOS / Linux**:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

**Windows**:

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
* Flask’s default `/static/<filename>` rule serves static files.
* Example: `/date` route returning current timestamp.

---

# **MODULE 2 — MTV PATTERN**

## **1. Introducing MTV**

Flask separates:

* **Model** → Data
* **Template** → UI (HTML)
* **View** → Python function that returns the response

---

## **2. Model Layer**

Simple model:

```python
cards = [
    {"question": "Hola", "answer": "Hello"},
    ...
]
```

Data → passed into templates.

---

## **3. Jinja Templates**

* Stored inside `/templates` folder.
* Use `render_template()`:

```python
return render_template("card.html", card=card)
```

HTML:

```html
<p>{{ card.question }}</p>
```

* Jinja variables use `{{ ... }}` syntax.
* `{% ... %}` → logic (if, for, include)

---

## **4. URL Parameters**

```python
@app.route("/card/<int:id>")
def show(id):
    return str(id)
```

---

## **5. Building Links**

```html
<a href="{{ url_for('show', id=3) }}">Card 3</a>
```

* Helps avoid hard-coded links.
* Automatically adjusts paths.
  
---

# **MODULE 3 — ORM**

## **1. What is ORM?**

ORM is a technique that lets:

* Represent **database tables as Python classes**
* Represent **rows as Python objects**
* Interact with the database using **Python code instead of SQL**

| ORM Concept    | Meaning                       |
| -------------- | ----------------------------- |
| Entity / Model | Python class mapped to table  |
| Table          | Database table                |
| Column         | Table column                  |
| Primary Key    | Unique row identifier         |
| Session        | Unit of work / DB interaction |
| Query          | Fetching data                 |
| Relationship   | Table relationships           |
| Transaction    | Commit / rollback             |

---

## **2. Defining an Entity**

All ORM models inherit from a **Base class**.

```bash
pip install sqlalchemy
```

**Example: User Entity**

```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    email = Column(String(100), unique=True)
```

---

## **3. What is a Session?**

* A **transactional workspace**
* Tracks objects
* Writes changes to DB

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///app.db")

Session = sessionmaker(bind=engine)
session = Session()

try:
    session.add(obj)
    session.commit()
except:
    session.rollback()
    raise
finally:
    session.close()
```

---

## **4. CRUD Operations**

**CREATE**

```python
user = User(name="John", email="john@mail.com")
session.add(user)
session.commit()
```

**READ (Query)**

```python
users = session.query(User).all()
```

**GET**:

```python
user = session.query(User).filter_by(id=1).first()
```

**UPDATE**

```python
user.name = "John Updated"
session.commit()
```

**DELETE**

```python
session.delete(user)
session.commit()
```

**Filter**

```python
session.query(User).filter(User.name == "John")
```

**Filter by**

```python
session.query(User).filter_by(name="John")
```

**Like**

```python
User.name.like("%oh%")
```

---

## **5. Relationships**

**One-to-Many Example**

```python
class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True)
    books = relationship("Book", back_populates="author")

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey("authors.id"))
    author = relationship("Author", back_populates="books")
```

---

# **MODULE 4 — REST API**

## **1. What is REST?**

**REST (Representational State Transfer)** is an architectural style for building **web services**. REST APIs allow **clients** (browser, mobile app, frontend, other services) to interact with a backend using **HTTP**.

**Key Principles of REST**

* Client–Server separation
* Stateless communication
* Resource-based URLs
* Standard HTTP methods
* Uses HTTP status codes
* Data usually exchanged as **JSON**

---

## **2. HTTP Terminology**

| HTTP Method | CRUD   | Meaning          |
| ----------- | ------ | ---------------- |
| GET         | Read   | Fetch data       |
| POST        | Create | Add new data     |
| PUT         | Update | Replace existing |
| PATCH       | Update | Partial update   |
| DELETE      | Delete | Remove data      |

| Code | Meaning      | When to Use       |
| ---- | ------------ | ----------------- |
| 200  | OK           | Successful GET    |
| 201  | Created      | Resource created  |
| 204  | No Content   | Successful delete |
| 400  | Bad Request  | Invalid input     |
| 401  | Unauthorized | Auth required     |
| 403  | Forbidden    | No permission     |
| 404  | Not Found    | Resource missing  |
| 500  | Server Error | Internal error    |

---

## **3. Creating REST APIs**

**Basic JSON Response**

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/ping")
def ping():
    return jsonify({"message": "pong"})
```

**GET**

```python
@app.route("/users", methods=["GET"])
def get_users():
    users = [
        {"id": 1, "name": "John"},
        {"id": 2, "name": "Jane"}
    ]
    return jsonify(users), 200
```

**GET (Path Parameter)**

```python
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    return jsonify({"id": user_id, "name": "John"}), 200
```

**POST (Create)**

```python
from flask import request

@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    user = {
        "id": 1,
        "name": data["name"]
    }
    return jsonify(user), 201
```

**PUT (Update)**

```python
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.json
    return jsonify({
        "id": user_id,
        "name": data["name"]
    }), 200
```

**DELETE**

```python
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    return "", 204
```

---

## **4. ORM Inside REST APIs**

```python
@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    user = User(name=data["name"], email=data["email"])
    session.add(user)
    session.commit()

    user = session.query(User).get(user.id)
    if not user:
        return jsonify({"error": "User not Added"}), 404
    return jsonify({"id": user.id}), 201
```

---

## **5. Project Structure**

```
app/
 ├── routes/
 │    └── user_routes.py
 ├── services/
 │    └── user_service.py
 ├── repositories/
 │    └── user_repository.py
 ├── models/
 │    └── user.py
 └── app.py
```

---

