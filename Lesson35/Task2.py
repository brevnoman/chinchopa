import asyncio
import aiohttp
import aiofiles
import json


async def reddit(subreddit):
    async with aiohttp.ClientSession() as session:
        resp = await session.request(method="GET", url=f"https://api.pushshift.io/reddit/comment/search/?subreddit={subreddit}")
        return resp

async def write_to_file(file_name, resp):
    async with aiofiles.open(file_name, "w") as file:
        text: dict = await resp.json()
        json.dump(text, file)

async def main():
    reddit_it = await reddit("NoFap")
    await write_to_file("redditNoFap.json", reddit_it)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

    #не понял почемуб но оно не записывает ничего в файл
