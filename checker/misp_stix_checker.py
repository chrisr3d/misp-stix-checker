#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .misp_to_stix_checker import MISPtoSTIXChecker
from .stix_to_misp_checker import STIXtoMISPChecker
from pathlib import Path
from pymisp import MISPEvent
from stix.core import STIXPackage
from stix2.parsing import parse as stix2_parser
from typing import Tuple, Union


def check_misp_to_stix(misp_file: Path, stix_file: Path,
                       debug: bool = False, version: int = 2):
    checker = MISPtoSTIXChecker(debug=debug, version=version)
    checker.check_misp_to_stix_conversion(misp_file, stix_file)
    checker.print_conversion_results()


def check_stix_to_misp(stix_file: Path, *misp_files: Tuple[Path],
                       debug: bool = False, version: int = 2):
    checker = STIXtoMISPChecker(debug=debug, version=version)
    checker.check_stix_to_misp_conversion(stix_file, *misp_files)
    checker.print_conversion_results()