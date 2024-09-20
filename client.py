import requests
import asyncio
import aiohttp


async def main():

    async with aiohttp.ClientSession() as session:
        response = await session.post("http://127.0.0.1:8080/advertisement/",
                                      json={
                                          'title': 'title111',
                                          'description': 'description1',
                                          'user': 1
                                      }
                                      )
        print(response.status)
        print(await response.text())

    async with aiohttp.ClientSession() as session:
        response = await session.patch("http://127.0.0.1:8080/advertisement/1",
                                      json={
                                          'title': 'title11122'
                                      }
                                      )
        print(response.status)
        print(await response.text())

    async with aiohttp.ClientSession() as session:
        response = await session.delete("http://127.0.0.1:8080/advertisement/1")
        print(response.status)
        print(await response.text())

    async with aiohttp.ClientSession() as session:
        response = await session.get("http://127.0.0.1:8080/advertisement/7")
        print(response.status)
        print(await response.text())

asyncio.run(main())




# response3 = requests.delete(
#     'http://127.0.0.1:5000/advertisements/1',
# )
#
# print(response.status_code)
# print(response.json())