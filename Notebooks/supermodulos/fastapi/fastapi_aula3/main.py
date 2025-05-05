from fastapi import FastAPI
from app.routes.user import router
from app.db.session import Base, engine


app = FastAPI()
app.include_router(router, prefix='/api')

Base.metadata.create_all(bind=engine)
