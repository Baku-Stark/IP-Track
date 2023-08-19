import asyncio, sys

def check_version():
    import lib.cli
    # major=3, minor=11, micro=2
    python_version = sys.version_info
    return exit("[+] Go install the most recent version of python -> https://www.python.org/downloads/") if python_version < (3, 10) else asyncio.run(lib.cli.parser())