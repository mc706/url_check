"""
Processes the badges in README.md
"""
from fabfile.config import README_FILE, PROJECT_NAME


# === update readme badge ===
def update_readme_badge(version):
    minus_header = "\n".join(get_readme_file().split('\n')[2:])
    with open(README_FILE, 'w') as readme:
        readme.write("# {0}\n".format(PROJECT_NAME))
        readme.write("![version](https://img.shields.io/badge/version-{0}-blue.svg)\n".format(version))
        readme.write(minus_header)
    return True


# === get readme file ===
def get_readme_file():
    with open(README_FILE, 'r') as readme:
        return readme.read()
