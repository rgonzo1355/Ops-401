import os
from pathlib import Path

def is_valid_file(file_path, valid_extensions=['.md', '.py', '.txt']):
    """Checks if a file is valid based on its extension and name."""
    return file_path.suffix in valid_extensions and file_path.name != 'README.md'

def generate_toc(directory):
    """Generates a table of contents for the given directory."""
    toc = ["# Table of Contents\n"]
    root_path = Path(directory)

    # List files directly in the directory (not in subdirectories)
    for file_name in os.listdir(root_path):
        file_path = root_path / file_name
        if file_path.is_file() and is_valid_file(file_path):
            relative_path = file_path.relative_to(root_path).as_posix().replace(' ', '%20')
            toc.append(f"- [{file_path.name}]({relative_path})")

    return '\n'.join(toc)

def update_readme(directory, toc):
    """Updates the README.md file in the given directory with the generated TOC."""
    readme_path = Path(directory) / 'README.md'
    with open(readme_path, 'w') as f:
        f.write(toc)

# Paths to your directories
directories = ['/home/rcode/Ops/Ops-401/Readings', '/home/rcode/Ops/Ops-401/Challenges']

for directory in directories:
    toc = generate_toc(directory)
    update_readme(directory, toc)
    print(f"Updated TOC in {Path(directory).name}")

print("TOC update completed successfully.")
