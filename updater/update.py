import os, sys, zipfile
from os.path import dirname, join, abspath
from core.utils import *

sys.path.insert(0, abspath(join(dirname(__file__), '..')))

# Function > Download Updated Archive
async def download_update():
	runtime = current_runtime()
	url = f"https://github.com/BobEXP/ChayaV2/archive/refs/heads/{runtime}.zip"
	await download_file(url, "req")


# Function > Extract Archive
def extract_archive():
	runtime = current_runtime()
	with zipfile.ZipFile(f"{get_current_script_path().replace('core/utils.py', f'downloads/{runtime}.zip')}", "r") as zip_ref:
		zip_ref.extractall(f"{get_current_script_path().replace('core/utils.py', f'downloads/')}")


# Function > Cleanup & Replace
def update_setup():
	runtime = current_runtime()
	run_cmd(f"rm -rf {get_current_script_path().replace('core/utils.py', f'downloads/ChayaV2-{runtime}/updater')}")
	chaya_files = get_files_in_dir(f"{get_current_script_path().replace('core/utils.py', '')}")
	chaya_dirs = next(os.walk(f"{get_current_script_path().replace('core/utils.py', '')}"))[1]
	
	# delete folders and files except /updater, /downloads
	for cdir in chaya_dirs:
		if cdir != "updater":
			if cdir != "downloads":
				cdir = f"{get_current_script_path().replace('core/utils.py', f'{cdir}')}"
				msg_status("WARNING", f"{c_red}Deleting Directory > {c_white}{cdir}")
				run_cmd(f"rm -rf {cdir}")
	for cfile in chaya_files:
		cfile = f"{get_current_script_path().replace('core/utils.py', f'{cfile}')}"
		msg_status("WARNING", f"{c_red}Deleting File > {c_white}{cfile}")
		run_cmd(f"rm -rf {cfile}")

	# move folders and files from /downloads/chaya-runtime/
	new_chaya_files = get_files_in_dir(f"{get_current_script_path().replace('core/utils.py', f'downloads/ChayaV2-{runtime}/')}")
	new_chaya_dirs = next(os.walk(f"{get_current_script_path().replace('core/utils.py', f'downloads/ChayaV2-{runtime}/')}"))[1]

	# move new folder and files except /updater, /downloads
	for ndir in new_chaya_dirs:
		if ndir != "updater":
			if ndir != "downloads":
				ndirpath = f"downloads/ChayaV2-{runtime}/{ndir}"
				ndir = f"{get_current_script_path().replace('core/utils.py', ndirpath)}"
				msg_status("WARNING", f"{c_red}Moving Directory > {c_white}{ndir}")
				cmd = f"mv {ndir} {get_current_script_path().replace('core/utils.py', '')}"
				run_cmd(cmd)
	for nfile in new_chaya_files:
		nfilepath = f"downloads/ChayaV2-{runtime}/{nfile}"
		nfile = f"{get_current_script_path().replace('core/utils.py', nfilepath)}"
		msg_status("WARNING", f"{c_red}Moving File > {c_white}{nfile}")
		cmd = f"mv {nfile} {get_current_script_path().replace('core/utils.py', '')}"
		run_cmd(cmd)

	status("INFO", "If there are errors, you can manually move folders and files from /downloads/ or re-clone the repo using: git clone --depth=1 https://github.com/BobEXP/ChayaV2.git")
	status("INFO", "Update Complete!")


# Function > Initialize
async def init() -> None:
	await download_update()
	extract_archive()
	#update_setup()


# Main
if __name__ == "__main__":
	asyncio.run(init())
