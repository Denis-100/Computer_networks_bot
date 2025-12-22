from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, FSInputFile

import keyboard as kb

router = Router()

@router.message(Command("menu"))
async def start_meny(message: Message):
    await message.answer("Меню", reply_markup=kb.networks)

class LocalNetworks:
    @staticmethod
    @router.message(F.text == "Локальная сеть")
    async def local_networks(message: Message):
        await message.answer("Что хотите узнать?", reply_markup=kb.local_networks)

    @staticmethod
    @router.callback_query(F.data == "local_info")
    async def local_info(callback: CallbackQuery):
        await callback.answer()
        await callback.message.answer("Локальная сеть (LAN - Local Area Network) - это сеть, "
                                      "которая соединяет компьютеры в одном месте, например "
                                      "в доме, школе или офисе. В таких сетях можно быстро "
                                      "передавать файлы, и использовать одни устройства, "
                                      "например принтер. Скорость передачи данных "
                                      "от 100 МБ/с до 10 ГБ/с")

    @staticmethod
    @router.callback_query(F.data == "local_schema")
    async def local_schema(callback: CallbackQuery):
        await callback.answer()
        photo = FSInputFile("image_networks/Локальная сеть.png")
        await callback.message.answer_photo(photo=photo)

class GlobalNetworks:
    @staticmethod
    @router.message(F.text == "Глобальная сеть")
    async def local_networks(message: Message):
        await message.answer("Что хотите узнать?", reply_markup=kb.global_networks)

    @staticmethod
    @router.callback_query(F.data == "global_info")
    async def local_info(callback: CallbackQuery):
        await callback.answer()
        await callback.message.answer("Глобальная сеть (WAN - Wide Area Network) - это сеть, "
                                      "которая связывает компьютеры, находящиеся далеко друг "
                                      "от друга, например в разных городах, или странах. "
                                      "Самый большой пример такой сети - интернет. Скорость "
                                      "передачи данных от 1МБ/с до 100 МБ/с. "
                                      "(некоторые сети могут достигать 1 ГБ/с)")

    @staticmethod
    @router.callback_query(F.data == "global_schema")
    async def local_schema(callback: CallbackQuery):
        await callback.answer()
        photo = FSInputFile("image_networks/Глобальная сеть.png")
        await callback.message.answer_photo(photo=photo)

class CityNetworks:
    @staticmethod
    @router.message(F.text == "Городская сеть")
    async def local_networks(message: Message):
        await message.answer("Что хотите узнать?", reply_markup=kb.city_networks)

    @staticmethod
    @router.callback_query(F.data == "city_info")
    async def local_info(callback: CallbackQuery):
        await callback.answer()
        await callback.message.answer("Городская сеть (MAN - Metropolitan Area Network) - это "
                                      "что-то среднее между локальной и глобальной сетью, она "
                                      "соединяет компьютеры по всему городу или большому району. "
                                      "Такой вид сети часто используют компании, у которых "
                                      "несколько филиалов в одном городе. Скорость передачи "
                                      "данных от 10 МБ/с до 1 ГБ /с.")

    @staticmethod
    @router.callback_query(F.data == "city_schema")
    async def local_schema(callback: CallbackQuery):
        await callback.answer()
        photo = FSInputFile("image_networks/Городская сеть.png")
        await callback.message.answer_photo(photo=photo)

class PersonalNetworks:
    @staticmethod
    @router.message(F.text == "Персональная сеть")
    async def local_networks(message: Message):
        await message.answer("Что хотите узнать?", reply_markup=kb.personal_networks)

    @staticmethod
    @router.callback_query(F.data == "personal_into")
    async def local_info(callback: CallbackQuery):
        await callback.answer()
        await callback.message.answer("Персональная сеть (PAN - Personal Area Network) - "
                                      "это небольшая сеть, которая соединяет устройства, "
                                      "которые находятся рядом с одним человеком. Например, "
                                      "когда телефон соединяется с наушниками через Bluetooth. "
                                      "Скорость передачи данных от 1МБ/с до 3 МБ/с "
                                      "у Bluetooth 4.0, 5.0. (Скорость у Bluetooth 5.0+ до 50МБ/с)")

    @staticmethod
    @router.callback_query(F.data == "personal_schema")
    async def local_schema(callback: CallbackQuery):
        await callback.answer()
        photo = FSInputFile("image_networks/Персональная сеть.png")
        await callback.message.answer_photo(photo=photo)

class VPNNetworks:
    @staticmethod
    @router.message(F.text == "Виртуальная частная сеть")
    async def local_networks(message: Message):
        await message.answer("Что хотите узнать?", reply_markup=kb.vpn_networks)

    @staticmethod
    @router.callback_query(F.data == "vpn_info")
    async def local_info(callback: CallbackQuery):
        await callback.answer()
        await callback.message.answer("Виртуальная частная сеть (VPN - Virtual Private Network) - это сеть, "
                                      "которая перенаправляет ваш IP-адрес через удаленный сервер другого "
                                      "провайдера. В итоге ваш интернет провайдер и другие лица не видят, "
                                      "что вы делаете в интернете, какие сайты посещаете. Скорость передачи "
                                      "данных зависит от скорости вашего интернета, загруженности серверов, "
                                      "расстояния до VPN сервера и мощности шифрования. В среднем, если у вас "
                                      "скорость интернета 100 МБ/с, то с VPN будет около 40-80 МБ/с.")

    @staticmethod
    @router.callback_query(F.data == "vpn_schema")
    async def local_schema(callback: CallbackQuery):
        await callback.answer()
        photo = FSInputFile("image_networks/ВПН.png")
        await callback.message.answer_photo(photo=photo)

@router.message()
async def handlers_message(message: Message):
    await message.answer("Привет\nНапиши '/menu' для открытия меню!")
