import sys
from sqlalchemy import text
sys.path.append(".")

from app.core.database import engine

try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        print("✅ Database connected successfully:", result.scalar())
except Exception as e:
    print("❌ Database connection failed:", e)
