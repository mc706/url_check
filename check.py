import os, shutil
from datetime import datetime
from splinter import Browser

import cv2

URLS = [
    'http://www.mc706.com',
    'http://www.google.com',
]

PHOTOS_DIR = 'screenshots'


def _clean_filename(name):
    return name.strip('http://').strip('/')


def _compare(image1, image2):
    img1 = cv2.imread(image1)
    img2 = cv2.imread(image2)
    row1, cols1, channel1 = img1.shape
    row2, cols2, channel2 = img2.shape
    print 'image 1 rows:', row1
    print 'image 2 rows:', row2
    print 'image 1 cols:', cols1
    print 'image 2 cols:', cols2
    print 'image 1 channel:', channel1
    print 'image 2 channel2:', channel2
    if (row1 != row2) or (cols1 != cols2) or (channel1 != channel2):
        print "two images are different"
        match = False
        return match
    else:
        mismatch = 0
        for i in range(1, row1):
            for j in range(1, cols1):
                px1 = img1[i, j]
                px2 = img2[i, j]
                if (px1.sum() != px2.sum()):
                    mismatch = mismatch + 1
        print 'total mismatch is:', mismatch
        if (mismatch == 0):
            match = True
        else:
            match = False
        return match


def check_urls():
    created = []
    today = str(datetime.now())
    with Browser() as browser:
        for url in URLS:
            browser.visit(url)
            screenshot = browser.screenshot('screenshot.png')
            if screenshot:
                dest = os.path.join(os.getcwd(), PHOTOS_DIR, _clean_filename(url))
                if not os.path.exists(dest):
                    os.makedirs(dest)
                name = os.path.join(dest, 'screenshot-{0}.png'.format(today))
                created.append(name)
                shutil.move(screenshot, name)


if __name__ == "__main__":
    check_urls()
