<!-- Python Version -->
Python 3.10.8

<!-- Project Start -->

uvicorn main:app --reload


<!-- Migrations -->
<!-- Init Migrations -->

alembic init fileName

<!-- Create Migrations file  -->

alembic revision --autogenerate -m "initial migrations"

<!-- Migrations Up -->

alembic upgrade head



<!-- Need to set on migrations env.py file -->
<!-- from models.UserModel import Base -->
<!-- target_metadata = Base.metadata -->


sqlalchemy.url = postgresql+psycopg2://postgres:mihir@localhost:5432/Todo