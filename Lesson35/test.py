import asyncio
import aiofiles
import aiohttp


async def get_classes():
    async with aiohttp.ClientSession() as session:
        resp = await session.request(method="GET", url="https://www.dnd5eapi.co/api/classes/")
        return resp

async def get_list_monsters():
    async with aiohttp.ClientSession() as session:
        resp = await session.request(method="GET", url="https://www.dnd5eapi.co/api/spells/?name=Acid+Arrow")
        return resp

async def write_to_file(file_name, resp):
    async with aiofiles.open(file_name, "w") as file:
        text = await resp.text()
        await file.write(text)

async def main():
    classes_resp = await get_classes()
    monster_resp = await get_list_monsters()
    await write_to_file("classes.txt", classes_resp)
    await write_to_file("monsters.txt", monster_resp)



if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
