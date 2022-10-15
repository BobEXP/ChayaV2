import asyncio
from core.utils import current_runtime

# Function > Download Updated Archive
async def download_update():
	runtime = current_runtime()
	url = f"https://github.com/BobEXP/ChayaV2/archive/refs/heads/{runtime}.zip"
	await download_file(url, "req")

	status(2, "Please replace the current archive with downloaded archive.")
	status(0, "Download Complete!")


# Function > Initialize
async def init() -> None:
	await download_update()

# Main
if __name__ == "__main__":
	asyncio.run(init())
