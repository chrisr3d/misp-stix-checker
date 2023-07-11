# MISP-STIX-Checker - Check the MISP <-> STIX conversion results to indicate the mapping gaps 

[![Python version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![License](https://img.shields.io/github/license/MISP/misp-stix.svg)](#License)

MISP-STIX-Checker is a Python (>= 3.8 tool) to check the conversions results between MISP & STIX.
This conversion is handled with [misp-stix](https://github.com/misp/misp-stix)

## Features

- Command-line tool to check how efficiently MISP and STIX formats are converted between each others
  - We focus on showing the mapping gaps
  - Choose between showing a summary OR details of the well mapped items
- Available for both MISP -> STIX & STIX -> MISP directions
- Simply pass the input & output files to have a quick check of the conversion efficiency
- /!\ This appliance does not support the conversion itself, please look at [misp-stix](https://github.com/misp/misp-stix) for this /!\

