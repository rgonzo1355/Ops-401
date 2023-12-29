import os
from pathlib import Path

def is_valid_file(file_path, readme_name, valid_extensions=['.md', '.py']):
    """Checks if a file is valid based on its extension and name."""
    return file_path.suffix in valid_extensions and file_path.name != readme_name

def generate_toc(directory, readme_name):
    """Generates a table of contents for the given directory."""
    toc = ["# Table of Contents\n"]
    root_path = Path(directory)

    # List files directly in the directory
    for file_name in os.listdir(root_path):
        file_path = root_path / file_name
        if file_path.is_file() and is_valid_file(file_path, readme_name):
            relative_path = file_path.relative_to(root_path).as_posix().replace(' ', '%20')
            toc.append(f"- [{file_path.stem}]({relative_path})")  # Using file stem for clean names

    # Update the specified README file
    readme_path = root_path / readme_name
    with open(readme_path, 'w') as f:
        f.write('\n'.join(toc))

# Updating TOC in ReadmeC.md for Challenges
generate_toc('/home/rcode/Ops/Ops-401/Challenges', 'ReadmeC.md')

print("TOC update completed successfully.")
