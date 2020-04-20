import os
import os.path
import glob


output_dirs = []
# print(os.getcwd())
# if glob.glob("*.py"):
#     output_dirs.append(os.getcwd())
# print(output_dirs)

def extension_in_list(input_list):
    for file in input_list:
        if file.endswith(".py"):
            return True

for current_dir, dirs, files in os.walk('main'):
    if extension_in_list(files):
        output_dirs.append(current_dir)
        output_dirs.sort()


print(output_dirs)



with open('output_dirs.txt', 'w') as out:
    output_line = "\n".join(output_dirs)
    out.write(output_line)