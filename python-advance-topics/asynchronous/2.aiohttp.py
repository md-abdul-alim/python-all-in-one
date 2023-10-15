import asyncio
import aiohttp


async def fetch(url):
    async with aiohttp.ClientSession() as session:  # This creates an asynchronous context manager, initiating a session for HTTP requests.
        async with session.get(url) as response:  # This asynchronously sends a GET request to the provided URL and waits for the response.
            return await response.text()  # It waits for and returns the response text (HTML content, in most cases).


async def main():
    try:
        html = await fetch('https://machine.dekkoisho.com') # Calls the fetch() function and waits for it to complete, storing the returned text
        print(html)
    except Exception as e:
        print('Error: ', e)

asyncio.run(main())
