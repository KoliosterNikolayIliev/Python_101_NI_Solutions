# import pathlib
# import logging
#
# file_path = pathlib.Path("hello.txt")
#
# try:
#     with file_path.open(mode="r") as file:
#         file.write("Hello, World!")
# except OSError as error:
#     logging.error("Writing to file %s failed due to: %s", file_path, error)
#     logging.error(f"Writing to file {file_path} failed due to: {error}")

#
# import os
#
# with os.scandir('../../../../') as entries:
#     for entry in entries:
#         print(entry.name, "->", entry.stat().st_size, "bytes")


# import aiohttp
#
# import asyncio
#
#
# async def check(url):
#
#     async with aiohttp.ClientSession() as session:
#
#         async with session.get(url) as response:
#
#             print(f"{url}: status -> {response.status}")
#
#             html = await response.text()
#
#             print(f"{url}: type -> {html[:17].strip()}")
#
#
# async def main():
#
#     await asyncio.gather(
#
#         check("https://realpython.com"),
#
#         check("https://pycoders.com"),
#
#     )
#
#
# asyncio.run(main())
#
# def pesho():
#     return('works')
#
# print(pesho(1000))

# def printer(*args, **kwargs):
#     name = kwargs.get('name')
#     if name:
#         return name
#     else:
#         return 'not entered'
#
# print(printer())
