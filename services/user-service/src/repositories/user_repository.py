from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.models.user import User 
from uuid import UUID
from datetime import datetime

# Data access layer for User entities; wraps SQLAlchemy queries used by the service layer.
class UserRepository:
    def __init__(self, db: AsyncSession):
        self._db = db

    # Fetch a user by email; returns None if no match is found.
    async def get_by_email(self, email: str):
        result = await self._db.execute(
            select(User).where(User.email == email)
        )
        return result.scalar_one_or_none()

    # Fetch a user by primary key; returns None if no match is found.
    async def get_by_id(self, id: UUID):
        result = await self._db.execute(
            select(User).where(User.id == id)
        )
        return result.scalar_one_or_none()

    # Persist a new user and commit immediately.
    async def create(self, user: User):
        self._db.add(user)
        await self._db.commit()
        return user

    # Apply a partial update (only the keys present in `data`) to an existing user.
    async def update(self, user_id: UUID, data: dict):
        user = await self.get_by_id(user_id)
        for key, value in data.items():
            setattr(user, key, value)
        await self._db.commit()
        return user
    