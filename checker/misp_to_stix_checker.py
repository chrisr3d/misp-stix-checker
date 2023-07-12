#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from .checker import Checker, _FILES_TYPING
from pathlib import Path


class MISPtoSTIXChecker(Checker):
    def __init__(self, debug: bool = False, version: int = 2):
        super().__init__(debug, version)

    def check_misp_to_stix_conversion(
            self, misp_file: _FILES_TYPING, stix_file: _FILES_TYPING):
        stix_content = self._load_stix_content(stix_file)
        return


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Check the STIX -> MISP conversion results'
    )
    parser.add_argument(
        '-d', '--debug', action='store_true',
        help='Verbose debugging event for successfull conversion.'
    )
    parser.add_argument(
        '-m', '--misp', type=Path, help='MISP file(s) to check.'
    )
    parser.add_argument(
        '-s', '--stix', type=Path, help='STIX file to check.'
    )
    parser.add_argument(
        '-v', '--version', default=2, choices=[1,2], type=int,
        help='STIX version'
    )
    check_args = parser.parse_args()
    checker = MISPtoSTIXChecker(
        debug=check_args.debug, version=check_args.version
    )
    checker.check_misp_to_stix_conversion(check_args.misp, check_args.stix)
    checker.print_conversion_results()