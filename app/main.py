# app/main.py
from fastapi import FastAPI
from app.core.config import settings
# from app.api.v1.api import api_router # We will create this later

app = FastAPI(title=settings.PROJECT_NAME)

@app.get("/")
async def root():
    return {"message": "Welcome to BeautyBase AI!"}

# app.include_router(api_router, prefix=settings.API_V1_STR) # We'll uncomment this later

# Optional: Add a startup event to ensure pgvector is enabled
from sqlalchemy import text
from app.db.session import SessionLocal

@app.on_event("startup")
async def startup_event():
    # This is a good place to ensure extensions are created, etc.
    # Though the pgvector/pgvector Docker image should handle this.
    # For safety, or if not using the specialized image, you might add:
    db = SessionLocal()
    try:
        # Check if pgvector extension is enabled, and enable it if not.
        # This requires superuser privileges initially if run from application.
        # Better to ensure it's enabled during DB provisioning (like in Dockerfile or by admin)
        # However, the `pgvector/pgvector` image handles this for us.
        # We can still check if it's there.
        result = db.execute(text("SELECT * FROM pg_extension WHERE extname = 'vector'")).fetchone()
        if not result:
            print("WARNING: pgvector extension not found. Ensure it is enabled in your PostgreSQL database.")
            # If you have superuser and want to try creating it (not ideal from app code):
            # db.execute(text("CREATE EXTENSION IF NOT EXISTS vector;"))
            # db.commit()
            # print("Attempted to create pgvector extension. Please verify.")
        else:
            print("pgvector extension is enabled.")
    except Exception as e:
        print(f"Error during startup check for pgvector: {e}")
    finally:
        db.close()