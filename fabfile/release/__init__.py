"""
Fabric Release Commands
"""
from fabric.api import task, local

from changelog import update_changelog
from fabfile.config import VERSION_FILE, CHANGELOG_FILE, README_FILE
from readme import update_readme_badge
from version import get_current_version, bump, write_version


# === release ===
@task(default=True)
def release(type='patch'):
    """
    Kicks off and completes a git flow release. Takes `type` argument
    """
    version = bump(type)
    local('git flow release start {0}'.format(version))
    update_changelog(version)
    write_version(version)
    update_readme_badge(version)
    local('git add {0} {1} {2}'.format(VERSION_FILE, CHANGELOG_FILE, README_FILE))
    local('git commit -m "updated version and changelog to {0}"'.format(version))
    local('git flow release finish {0}'.format(version))
    local('git push --all')
    local('git push --tags')


# === release patch ===
@task()
def patch():
    """
    Shorthand for release:type=patch
    """
    release(type='patch')


# === release minor ===
@task()
def minor():
    """
    shorthand for release:type=minor
    """
    release(type='minor')


# === release major ===
@task()
def major():
    """
    Shorthand for release:type=major
    """
    release(type='major')
