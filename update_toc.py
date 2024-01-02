import os
from pathlib import Path

def is_valid_file(file_path, valid_extensions=['.md', '.py']):
    """Checks if a file is valid based on its extension."""
    return file_path.suffix in valid_extensions

def update_toc(directory, readme_name):
    """Updates the table of contents (TOC) in the specified README file for the given directory."""
    toc = ["# Table of Contents"]

    # Get the existing TOC lines from the README file, if it exists
    readme_path = Path(directory) / readme_name
    existing_toc = []

    if readme_path.exists():
        with open(readme_path, 'r') as f:
            existing_toc = f.read().splitlines()

    # Find files directly in the directory and add them to the TOC if they are valid
    for file_name in os.listdir(directory):
        file_path = Path(directory) / file_name
        if file_path.is_file() and is_valid_file(file_path):
            relative_path = file_path.relative_to(Path(directory)).as_posix().replace(' ', '%20')
            toc.append(f"- [{file_path.stem}]({relative_path})")

    # Update the TOC lines in the README file, preserving any existing content
    with open(readme_path, 'w') as f:
        for line in toc:
            f.write(line + '\n')
        f.write('\n'.join(existing_toc[len(existing_toc) - 1:]))

# Update TOC in ReadmeC.md for Challenges
update_toc('/home/rcode/Ops/Ops-401/Challenges', 'ReadmeC.md')

print("TOC in ReadmeC.md updated successfully.")
