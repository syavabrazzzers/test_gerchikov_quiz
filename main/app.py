from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from gerchikov.router import router as gerchikov_router
from main.db import db
from mbriggs.router import router as mbriggs_router

dp = Dispatcher(storage=MemoryStorage())


def on_startup():
    db.create_table()
    db.create_table_bookmarks()


dp.startup.register(on_startup)


dp.include_router(gerchikov_router)
dp.include_router(mbriggs_router)
