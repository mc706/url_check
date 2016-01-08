"""
Version Manipulation
"""

from fabfile.config import VERSION_FILE


# === get version ===
def get_current_version():
    """
    Gets the current api version
    """
    with open(VERSION_FILE, 'r') as vfile:
        original = vfile.read()
    return original.split('=')[1].strip('\" \n\'')


# === write version ===
def write_version(new_version):
    """
    Writes the version to the new file
    """
    with open(VERSION_FILE, 'w') as version_file:
        version_file.write('__version__ = "{0}"'.format(new_version))
    return True


# === bump ===
def bump(type='patch'):
    """
    Returns the bumped version number
    """
    version = get_current_version()
    major, minor, patch = version.split('.')
    if type == "patch":
        patch = int(patch) + 1
    elif type == "minor":
        patch = 0
        minor = int(minor) + 1
    elif type == 'major':
        patch = 0
        minor = 0
        major = int(major) + 1
    return "{0}.{1}.{2}".format(major, minor, patch)
