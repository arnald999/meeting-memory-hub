from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base
from datetime import datetime

class Meeting(Base):
    __tablename__ = "meetings"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    date = Column(DateTime, default=datetime.utcnow)
    organizer_id = Column(Integer, ForeignKey("users.id"))

    organizer = relationship("User")
    transcripts = relationship("Transcript", back_populates="meeting")

