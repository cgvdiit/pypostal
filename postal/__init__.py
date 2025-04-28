import os
LIBPOSTAL_DLL_PATH = os.getenv("LIBPOSTAL_DLL_PATH")
if LIBPOSTAL_DLL_PATH:
    os.add_dll_directory(LIBPOSTAL_DLL_PATH)
