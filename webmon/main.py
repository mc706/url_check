import os, shutil
from datetime import datetime
from splinter import Browser

from webmon.utils import _clean_filename, _rmsdiff, _directory_stdev
from webmon.configuration import get_urls, get_photos_directory


def run():
    urls = get_urls()
    pdir = get_photos_directory()
    created = []
    changed = []
    today = str(datetime.now())
    if os.path.isabs(pdir):
        photos_dir = pdir
    else:
        photos_dir = os.path.join(os.getcwd(), pdir)
    print "Taking Screenshots"
    with Browser() as browser:
        for url in urls:
            browser.visit(url)
            screenshot = browser.screenshot('screenshot.png')
            if screenshot:
                dest = os.path.join(photos_dir, _clean_filename(url))
                if not os.path.exists(dest):
                    os.makedirs(dest)
                name = os.path.join(dest, 'screenshot-{0}.png'.format(today))
                created.append(name)
                shutil.move(screenshot, name)
    print "Calculating Differences"
    for directory in os.listdir(photos_dir):
        if os.path.isdir(os.path.join(photos_dir, directory)):
            for image in created:
                if directory in image:
                    active = image
            if active:
                files = os.listdir(os.path.join(photos_dir, directory))
                mean, std = _directory_stdev(os.path.join(photos_dir, directory))
                current = _rmsdiff(os.path.join(photos_dir, directory, files[-1]), active)
                if current < mean - std or current > mean + std:
                    changed.append((directory, current, mean, std))
    if changed:
        for change in changed:
            print "{0} has changed by more than the average, {1} !~ {2}+/-{3}".format(*change)
    else:
        print "None of the websites have changed"
