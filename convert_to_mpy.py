import os
import subprocess
from glob import glob

# Path to the mpy cross compiler program
mpy_cross_path = "mpy-cross-windows-8.2.9.static.exe"

# Path to the main folder to convert
src_folder = "src\\sprig_essentials"

# Get a list of all .py files in the src/sprig_essentials folder
py_file_paths = [y for x in os.walk(src_folder) for y in glob(os.path.join(x[0], '*.py'))]

# Create an output folder if it doesn't exist
dst_folder = "output"
os.makedirs(dst_folder, exist_ok=True)

print("Compiling .py files into .mpy files...")

# Iterate over each .py file and run mpy-cross with the file name as the argument
for py_file_path in py_file_paths:
    subprocess.run([mpy_cross_path, py_file_path])

    # Move the created .mpy file to the output folder
    mpy_file_path = py_file_path.replace(".py", ".mpy").replace("/", "\\")
    output_file_path = os.path.join(dst_folder, mpy_file_path.split(src_folder)[-1][1:])
    os.renames(mpy_file_path, output_file_path)

print("Completed!")
