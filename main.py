import asyncio

from aiogram import Bot, Dispatcher
from handlers import router
from config import token

async def main():
    bot = Bot(token=token)
    dp = Dispatcher()
    dp.include_router(router)
    await asyncio.gather(
        dp.start_polling(bot)
    )

if __name__ == "__main__":
    print("Бот включен")
    asyncio.run(main())
