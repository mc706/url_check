"""
Gets and Sets configuration for Webmon
"""
import os
import click
import ConfigParser
from ConfigParser import NoSectionError, NoOptionError
APP_NAME = 'My Application'


def get_config():
    config = ConfigParser.RawConfigParser()
    config.read([
        os.path.expanduser('~/.webmonrc'),
        os.path.join(click.get_app_dir(APP_NAME), 'config.ini'),
        'config.ini'
    ])
    return config


def get_urls():
    config = get_config()
    sections = config.sections()
    urls = [section for section in sections if section != 'webmon']
    return urls


def get_default_samples():
    config = get_config()
    try:
        return config.get('webmon', 'samples')
    except (NoSectionError, NoOptionError):
        return 10


def get_samples(section):
    config = get_config()
    try:
        return config.get(section, 'samples')
    except (NoSectionError, NoOptionError):
        return get_default_samples()


def get_photos_directory():
    config = get_config()
    try:
        return config.get('webmon', 'photos_directory')
    except (NoSectionError, NoOptionError):
        return 'screenshots'
