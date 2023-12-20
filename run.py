import asyncio

from main.app import dp
from main.bot import bot


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
