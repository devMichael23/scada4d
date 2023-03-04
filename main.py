import asyncio
from api.Server import *
from api.Vars import *

manager = mng()


async def main():
    room = await serverInitStart(manager)

    await manager.server.start()

    tmp = await hiTemp(manager, room)
    t = tmp.getValue()

    while True:
        await asyncio.sleep(1)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.set_debug(True)
    loop.run_until_complete(main())
    manager.server.stop()