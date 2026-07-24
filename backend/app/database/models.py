from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, Float
from datetime import datetime
from app.database.database import Base



class Email(Base):

    __tablename__ = "emails"

    id = Column(
        Integer,
        primary_key=True
    )

    message_id = Column(
        String,
        unique=True,
        nullable=False
    )

    sender = Column(
        String
    )

    subject = Column(
        String
    )

    body = Column(
        Text
    )

    category = Column(
        String
    )

    importance = Column(
        String
    )

    urgency = Column(
        String
    )

    priority = Column(
        String
    )

    score = Column(
        Integer
    )

    decision = Column(
        String
    )

class Notification(Base):

    __tablename__ = "notifications"


    id = Column(
        Integer,
        primary_key=True
    )


    email_subject = Column(
        String
    )


    message = Column(
        Text
    )


    status = Column(
        String
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )




class AgentLog(Base):

    __tablename__ = "agent_logs"


    id = Column(
        Integer,
        primary_key=True
    )


    status = Column(
        String
    )


    last_scan = Column(
        String
    )


    processed_emails = Column(
        Integer
    )


    last_action = Column(
        String
    )


    processing_time = Column(
        String
    )


    created_at = Column(
        String,
        default=lambda: str(datetime.now())
    )

class AgentSetting(Base):

    __tablename__ = "agent_settings"


    id = Column(
        Integer,
        primary_key=True
    )


    model = Column(
        String,
        default="gemini"
    )


    temperature = Column(
        Float,
        default=0.7
    )


    max_emails = Column(
        Integer,
        default=100
    )


    auto_action = Column(
        Boolean,
        default=True
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

class User(Base):

    __tablename__ = "users"


    id = Column(
        Integer,
        primary_key=True
    )


    username = Column(
        String,
        unique=True,
        nullable=False
    )


    email = Column(
        String,
        unique=True,
        nullable=False
    )


    hashed_password = Column(
        String,
        nullable=False
    )


    is_active = Column(
        Boolean,
        default=True
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )