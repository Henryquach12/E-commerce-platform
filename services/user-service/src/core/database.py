from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from src.core.config import settings


class Base(DeclarativeBase):
    pass


# Create_async_engine uses an async driver (e.g. asyncpg) so DB calls don't block the event loop.
engine = create_async_engine(settings.DATABASE_URL)

SessionLocal = sessionmaker(
    engine,
    # Swap the default sync Session for AsyncSession so all ORM operations are awaitable.
    class_=AsyncSession,
    # Prevent SQLAlchemy from expiring attributes after commit, which would trigger lazy loads
    # that fail in async context (no implicit I/O allowed outside an active session).
    expire_on_commit=False
)

async def get_db():
    # Async context manager ensures the session is closed even if an exception is raised.
    async with SessionLocal() as session:
        # Yield turns this into a FastAPI dependency; the session stays open until the request ends.
        yield session
