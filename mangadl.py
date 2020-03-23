"""
A script to download manga images from MangaReader.

The purpose of this script is to periodically check mangareader.net for new
episodes of manga that I read, and to download the images for those manga,
organizing them in a sensible manner on my laptop.

Written using Python 3.7
"""

import requests
import bs4
import os
import csv
import re
