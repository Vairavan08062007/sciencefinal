import asyncio
from app.database import Base, engine
# Import all model files to ensure they are registered in Base.metadata
import app.models
import app.models_vitals
import app.models_meds

async def init_db():
    print("Creating all tables in database...")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Tables created successfully.")

if __name__ == "__main__":
    asyncio.run(init_db())
