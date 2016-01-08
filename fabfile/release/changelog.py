"""
Changelog Maniuplation Commands
"""
from datetime import date

from fabfile.config import CHANGELOG_FILE, REPOSITORY_URL

TEMPLATE = """# Change Log
All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/) and [KeepAChangelog](http://keepachangelog.com/).

## [Unreleased]
---

### New

### Changes

### Fixes


"""


# === Update Changelog ===
def update_changelog(version):
    """
    Updates the changelog when cutting versions
    """
    today = str(date.today())
    old = get_changelog()
    minus_header = "\n".join(old.split("\n")[5:])
    with open(CHANGELOG_FILE, 'w') as changelog:
        changelog.write(TEMPLATE)
        changelog.write("## [[{0}]({2})] - ({1})\n".format(version, today, REPOSITORY_URL+'/releases/tag/v' + version))
        changelog.write(minus_header)
    return True


# === Get Changelog ===
def get_changelog():
    """
    Returns the Changelog Contents
    """
    with open(CHANGELOG_FILE, 'r') as cfile:
        changelog = cfile.read()
    return changelog
