import asyncio


async def main():
    print("Hello")
    await asyncio.sleep(1)  # This 1 second other tasks will perform, await will not prevent any blockage in code execution for this 1 second.
    print("World")

asyncio.run(main())
