# app/models/product.py
from sqlalchemy import Column, Integer, String, Text, Float
from sqlalchemy.dialects.postgresql import JSONB # For other structured data
# from pgvector.sqlalchemy import Vector # We'll use this later for embeddings

from app.db.session import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True, nullable=False)
    brand = Column(String(100))
    category = Column(String(100))
    description = Column(Text, nullable=True)
    price = Column(Float, nullable=True)
    image_url = Column(String(500), nullable=True)
    # Add other metadata fields as needed
    # e.g., skin_type_compatibility = Column(JSONB)
    # We will add the embedding vector column later once we confirm pgvector setup