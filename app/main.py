from fastapi import FastAPI
from app.database.db import Base, engine
from app.api import You, faculty, courses, enrollments

Base.metadata.create_all(bind=engine)

app = FastAPI(title="CampusHub ERP")

app.include_router(You.router)
app.include_router(faculty.router)
app.include_router(courses.router)
app.include_router(enrollments.router)

@app.get("/")
def home():
    return {"message": "Welcome to CampusHub ERP"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

