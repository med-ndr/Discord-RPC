import time
import platform
from pypresence import Presence

#open your Discord Developer Portal and create an application to get your client ID
CLIENT_ID = "YOU-ID"
rpc = Presence(CLIENT_ID)
rpc.connect()

kernel = platform.release()
start_time = int(time.time())

while True:
    rpc.update(
        details="Using Arch Linux",
        state=f"Kernel: {kernel}",
        start=start_time,
        #you can change the large_image and large_text to whatever you want, but make sure to upload the image to your Discord Developer Portal first
        large_image="linux-1",
        large_text="Arch Linux"
    )
    time.sleep(15)
