import time
import platform
from pypresence import Presence

CLIENT_ID = "1574113209462296596"
rpc = Presence(CLIENT_ID)
rpc.connect()

kernel = platform.release()
start_time = int(time.time())

while True:
    rpc.update(
        details="Using Arch Linux",
        state=f"Kernel: {kernel}",
        start=start_time,
        large_image="_",
        large_text="Arch Linux"
    )
    time.sleep(15)
