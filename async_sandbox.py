

async def inner() -> None:
    print("inner")
    await asyncio.sleep(3)
    print("sleep over")


async def main() -> None:
    await inner()
    print("main")


if __name__ == "__main__":
    import asyncio
    with asyncio.Runner(loop_factory=asyncio.new_event_loop) as runner:
        asyncio.run(main())
