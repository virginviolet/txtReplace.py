#! /usr/bin/python
# -*- coding: utf-8 -*-

# This script will replace the string "SponsorBlock" with "SponorBlock" in all localization files found in all folders.

import os
import re
import sys


def replace(sourcearg, findarg, replacearg):
    print(findarg, replacearg)

    count = 0

    textfiles = []
    for root, dirnames, filenames in os.walk(sourcearg):
        for filename in [s for s in filenames if s.endswith(".json")]:
            print("Processing: {}".format(filename))
            textfiles.append(os.path.join(root, filename))

    #findarg, replacearg = list(map(re.escape, [findarg, replacearg]))
    for textfile in textfiles:
        with open(textfile, 'r') as f:
            try:
                content, count = re.subn(findarg, replacearg, f.read())
                count += 1
            except UnicodeDecodeError:
                print("ERROR: UnicodeDecodeError")

        with open(textfile, 'w') as f:
            f.write(content)
            count -= 1
    
    print(findarg, replacearg)

    print("Replaced {} occurences of {} in {}".format(
        str(count), findarg, sourcearg))

try:
   args = sys.argv
   sourcearg = args[1]
except:
    print( """Invalid arguments passed. Usage:\n scriptname.py full-source-path""")
    sys.exit()

# input from user
confirm = input("Will replace strings in files located in {} and all subfolders. Is this what you want to do? (Y/N)\n".format(sourcearg))
if confirm.lower() != "y" and confirm.lower() != "yes":
    print("Exiting.")
    sys.exit()

replace(sourcearg, "SponsorBlock ", "SponorBlock ")
replace(sourcearg, " SponsorBlock", " SponorBlock")

replace(sourcearg, "sponsor ", "sponor ")
replace(sourcearg, " sponsor", " sponor")

replace(sourcearg, "Sponsor ", "Sponor ")
replace(sourcearg, " Sponsor", " Sponor")

replace(sourcearg, "sponsors ", "sponors ")
replace(sourcearg, " sponsors", " sponors")

replace(sourcearg, "Sponsors ", "Sponors ")
replace(sourcearg, " Sponsors", " Sponors")

replace(sourcearg, "sponsorship ", "sponorship ")
replace(sourcearg, " sponsorship", " sponsorship")

replace(sourcearg, "Sponsorship ", "Sponorship ")
replace(sourcearg, " Sponsorship", " Sponsorship")

replace(sourcearg, "sponsorships ", "sponorships ")
replace(sourcearg, " sponsorships", " sponsorships")

replace(sourcearg, "Sponsorships ", "Sponorships ")
replace(sourcearg, " Sponsorships", " Sponsorships")

replace(sourcearg, " sponsor.", "  sponor.")

replace(sourcearg, " sponsors.", "  sponors.")