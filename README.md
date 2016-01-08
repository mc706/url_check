# webmon
---
![version](https://img.shields.io/badge/version-0.0.3-blue.svg)
[![Stories in Ready](https://badge.waffle.io/mc706/webmon.png?label=ready&title=Ready)](https://waffle.io/mc706/webmon)
[![PyPi version](https://pypip.in/v/webmon/badge.png)](https://crate.io/packages/webmon/)
[![PyPi downloads](https://pypip.in/d/webmon/badge.png)](https://crate.io/packages/webmon/)

A tool that allows you to point to a number of different URLS and have it take screenshots and listen for differences 
over time.

This is intended to run as a CLI, that takes a searches parent directories until it finds a configuraiton file.


## Setup
`cd` into the directory where you want the repo to go.

Run:
```
git clone https://github.com/mc706/url_check
```

To setup the repo, make sure you have `python` and `pip` installed. If you dont have pip install 
[here](https://pip.pypa.io/en/stable/installing/).


Once you have `pip`, run:

```
pip install -r requirements.txt
```

Edit the `URLS` list in `check.py` to be the list of URLS you need to check.

Run:

```
python check.py
```


## How it works
The `check.py` command has 3 steps.

The project uses [selenium]() using [splinter]() to control the Firefox. It visits the websites in `URLS`
and takes screenshots and saves them to `screenshots/`.

The second step takes the root square mean difference of the historgrams of each pair of screenshots already in 
the screenshots directory. It then calculates the average and the standard deviation of the rms. It then compares the 
last screenshot in the directory to the current screenshot and marks it changed if it falls outside of the standard devation.
Note: due to the size of the calculation of every pair of screenshots, the length of this step tends to go up exponentially,
per website. To shorten this, I have it taking the last `10` samples only. This can be adjusted for accuracy in the `SAMPLES`
variable.

The last step reports which of the urls have deviated too much and by how much.

