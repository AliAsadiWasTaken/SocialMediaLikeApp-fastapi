# from fastapi.testclient import TestClient
# from app.config import settings
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# import pytest
# from app.database import get_db, Base
# from app.main import app

# SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test'

# engine = create_engine(SQLALCHEMY_DATABASE_URL)

# TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# def override_get_db():
#     db = TestingSessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @pytest.fixture()
# def session():
#     Base.metadata.drop_all(bind=engine)
#     Base.metadata.create_all(bind=engine)
#     db = TestingSessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()



# @pytest.fixture()
# def client(session):
#     def get_override_db():
#         db = TestingSessionLocal()
#         try:
#             yield db
#         finally:
#             db.close()
#     app.dependency_overrides[get_db] = override_get_db
#     yield TestClient(app)
