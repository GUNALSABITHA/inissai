from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base


load_dotenv()

DB_HOST='localhost'
DB_PORT=5432
DB_USER='postgres'
DB_PASSWORD='root'
DB_NAME='innisai'

SYNC_URL= (
    f"postgresql+psycopg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
ASYNC_URL = (
    f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# Engines
engine = create_engine(SYNC_URL,pool_pre_ping=True)
async_engine = create_async_engine(ASYNC_URL, pool_pre_ping=True)


SyncSessionLocal = sessionmaker(
    bind=engine,
    autoflush = False,
)

AsyncSessionLocal = async_sessionmaker(
    bind=async_engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)



Base = declarative_base()

def init_models():
    try:
        Base.metadata.create_all(bind=engine, checkfirst=True)
    except Exception as e:
        print(f"Error initializing models: {e}")



