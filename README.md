# Mock-up Data Workshop

A hands-on playground for generating test data in multiple ways and using it from Robot Framework.

The project contains four independent examples—each in its own directory—illustrating different techniques and libraries:

| Example | Purpose | Key Libraries |
|---------|---------|---------------|
| `01-faker` | Generate standalone fake data in Python or directly from Robot Framework keywords | `faker`, `robotframework-faker` |
| `02-factory_boy` | Use **factory_boy** to build Python/Robot data factories without a database | `factory-boy`, `faker` |
| `03-sqlalchemy` | Basic SQLAlchemy ORM demo (Customer table) with Robot keywords for add/query/delete | `sqlalchemy`, `faker` |
| `04-sqlalchemy_factory` | Combine **factory_boy** `SQLAlchemyFactory` with ORM to seed/query a real DB from Robot | `sqlalchemy`, `factory-boy`, `faker` |

---

## 1. Prerequisites

* **Python ³ˣ** (3.10 or newer recommended)
* Build tools for C-extensions (only required for some DB drivers)

---

## 2. Installation

Clone the repository and create a virtual environment (recommended):

```bash
git clone <repo-url>
cd mockup_data_workshop
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

Install all Python dependencies:

```bash
# Using requirements.txt
pip install -r requirements.txt

# — OR — if you prefer Poetry (pyproject.toml)
poetry install
```

The `requirements.txt` currently lists:

```text
robotframework
robotframework-faker
robotframework-pythonlibcore
sqlalchemy
psycopg2-binary      # Only needed if you switch DATABASE_URL to PostgreSQL
factory-boy
faker
```

> **Tip** – If you want PostgreSQL support, also install `psycopg2-binary` (already in the list) and set `DATABASE_URL` accordingly.

---

## 3. Running the Examples

All examples can be run from the project root.

### 3.1 Faker (no DB)

```bash
# Python demo – prints JSON to stdout
python 01-faker/faker_python_demo.py --count 5 --locale en_US

# Robot demo – generates fake data in tests
robot 01-faker/faker_robot_demo.robot
```

### 3.2 factory_boy (no DB)

```bash
# Python CLI (prints users)
python -m 02-factory_boy.factories --count 3

# Robot demo
robot 02-factory_boy/factory_robot_demo.robot
```

### 3.3 SQLAlchemy ORM

```bash
robot 03-sqlalchemy/sqlalchemy_robot_demo.robot
```

The suite will create an SQLite DB file (`03-sqlalchemy/db.db`) in the same folder. If you want to point it to another database, set an environment variable before running:

```bash
export DATABASE_URL=postgresql+psycopg2://user:pass@localhost:5432/mydb
```

### 3.4 SQLAlchemy + factory_boy

```bash
robot 04-sqlalchemy_factory/robot_demo.robot
```

As above, the test creates its own SQLite file (`04-sqlalchemy_factory/db.db`) unless `DATABASE_URL` is overridden.

---

## 4. Troubleshooting

* **“No keyword with name …”** – Make sure the `Library` path in the `.robot` file is correct relative to the directory you run `robot` from. Try running from the project root as shown above.
* **`sqlite3.OperationalError: no such table`** – Delete the `*.db` file and re-run the suite, or ensure your `DATABASE_URL` points to a writable database.

---

## 5. Contributing

Feel free to open issues or PRs to add new examples, databases, or data-generation techniques.

---

Happy mocking! 🎉
