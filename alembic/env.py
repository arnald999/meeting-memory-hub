import os
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from sqlalchemy import create_engine
from alembic import context
from dotenv import load_dotenv

# 1️⃣ Load .env from project root
project_root = os.path.dirname(os.path.dirname(__file__))
load_dotenv(os.path.join(project_root, ".env"))

# 2️⃣ Import settings and models
from app.core.config import settings
from app.core.database import Base
from app.models import user, meeting, transcript, slide  # Import all models here

# 3️⃣ Alembic Config object
config = context.config

# 4️⃣ Logging
fileConfig(config.config_file_name)

# 5️⃣ Metadata for 'autogenerate'
target_metadata = Base.metadata

# ------------------------
# Offline Migrations
# ------------------------
def run_migrations_offline():
    """Run migrations without a DB connection"""
    url = settings.DATABASE_URL
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

# ------------------------
# Online Migrations
# ------------------------
def run_migrations_online():
    """Run migrations with a DB connection"""
    connectable = create_engine(settings.DATABASE_URL, poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

# ------------------------
# Entry Point
# ------------------------
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
