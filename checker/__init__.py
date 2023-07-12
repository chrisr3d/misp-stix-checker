import argparse
from .misp_stix_checker import check_misp_to_stix, check_stix_to_misp
from .misp_to_stix_checker import MISPtoSTIXChecker
from .stix_to_misp_checker import STIXtoMISPChecker
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        description='Check the STIX <-> MISP conversion results'
    )
    parser.add_argument(
        '-d', '--debug', action='store_true', help='Show errors and warnings'
    )
    parser.add_argument(
        '-v', '--version', default=2, choices=[1,2], type=int,
        help='STIX version'
    )

    # SUBPARSERS TO SEPARATE THE 2 MAIN FEATURES
    subparsers = parser.add_subparsers(
        title='Main feature', dest='feature', required=True
    )

    # MISP TO STIX CONVERSION CHECK FEATURE
    misp_to_stix_parser = subparsers.add_parser(
        'misp_to_stix', help='Check the MISP -> STIX conversion results'
    )
    misp_to_stix_parser.add_argument(
        '-m', '--misp', type=Path, help='MISP file to check.'
    )
    misp_to_stix_parser.add_argument(
        '-s', '--stix', nargs='+', type=Path, help='STIX file(s) to check.'
    )
    misp_to_stix_parser.set_defaults(func=check_misp_to_stix)

    # STIX TO MISP CONVERSION CHECK FEATURE
    stix_to_misp_parser = subparsers.add_parser(
        'stix_to_misp', help='Check the STIX -> MISP conversion results'
    )
    stix_to_misp_parser.add_argument(
        '-s', '--stix', type=Path, help='STIX file to check.'
    )
    stix_to_misp_parser.add_argument(
        '-m', '--misp', nargs='+', type=Path, help='MISP file(s) to check.'
    )
    stix_to_misp_parser.set_defaults(func=check_stix_to_misp)

    args = parser.parse_args()
    args.func(args)