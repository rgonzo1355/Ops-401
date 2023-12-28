import os

def generate_toc(directory):
    toc = ["# Table of Contents\n"]
    for root, dirs, files in os.walk(directory):
        level = root.replace(directory, '').count(os.sep)
        indent = ' ' * 4 * level
        if os.path.basename(root) != '':
            toc.append(f'{indent}- {os.path.basename(root)}')
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            if f.endswith('.md') and f != 'README.md':
                filepath = os.path.relpath(os.path.join(root, f), directory)
                toc.append(f'{subindent}- [{f}]({filepath})')
    return '\n'.join(toc)

def update_readme(directory, toc):
    readme_path = os.path.join(directory, 'README.md')
    with open(readme_path, 'w') as f:
        f.write(toc)

# Paths to your subdirectories
directories = ['Readings', 'Challenges']

for directory in directories:
    toc = generate_toc(directory)
    update_readme(directory, toc)

