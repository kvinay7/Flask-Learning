# **MODULE 1 — Introduction**

## **1. Overview**

* Flask is a Python Microframework for building web applications. It includes only essential tools (very lightweight, minimal setup, flexible).
* Built on:
  * **Jinja2** → templating
  * **Werkzeug** → routing + HTTP
  * Flask does NOT enforce project structure.

---

## **2. Installing Flask & Starting Project**

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

**macOS / Linux**:

```bash
export FLASK_APP=flashcards.py
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

## **5. Building Links Using url_for**

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

