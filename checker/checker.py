#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import ABCMeta
from collections import defaultdict
from pathlib import Path
from pymisp import MISPEvent
from stix.core import STIXPackage
from stix2.bundle import Bundle
from stix2.parsing import parse as stix2_parser
from typing import Union

_FILES_TYPING = Union[Path, str]


class Checker(metaclass=ABCMeta):
    def __init__(self, debug: bool, version: int):
        self.__debug = debug
        self.__errors = defaultdict(set)
        self.__success = defaultdict(set)
        self.__version = self._check_stix_version(version)

    @property
    def debug(self) -> bool:
        return self.__debug
    
    @property
    def errors(self) -> dict:
        return self.__errors
    
    @property
    def success(self) -> dict:
        return self.__success

    @property
    def version(self) -> int:
        return self.__version

    @version.setter
    def update_version(self, version: int):
        self.__version = version

    def print_conversion_results(self):
        return
    
    def _check_stix_version(self, version: Union[int, str]) -> Union[int, None]:
        try:
            version = int(version)
        except Exception:
            return self._version_error(version)
        else:
            if version not in (1, 2):
                return self._version_error(version)
            return version
        
    def _load_misp_content(self, filename: _FILES_TYPING):
        if not isinstance(filename, Path):
            filename = Path(filename).resolve()
        if not filename.exists() or not filename.is_file():
            self._misp_loading_error(filename, f'Wrong MISP file name')
        misp_event = MISPEvent()
        try:
            misp_event.load_file(filename)
        except Exception as exception:
            self._misp_loading_error(filename, exception)
        else:
            return misp_event
        
    def _load_stix_content(self, filename: _FILES_TYPING):
        if not isinstance(filename, Path):
            filename = Path(filename).resolve()
        if not filename.exists() or not filename.is_file():
            self._stix_loading_error(filename, f'Wrong STIX file name')
        if self.version is None:
            for version in (1, 2):
                try:
                    content = getattr(self, f'_load_stix{version}_content')(
                        filename
                    )
                except Exception:
                    continue
                else:
                    self.update_version(version)
                    return content
            self._stix_loading_error(filename, 'Fails for both version 1 and 2')
        else:
            try:
                content = getattr(self, f'_load_stix{self.version}_content')(
                    filename
                )
            except Exception as exception:
                self._stix_loading_error(filename, exception)
            else:
                return content
    
    @staticmethod
    def _load_stix1_content(filename: Path) -> STIXPackage:
        return STIXPackage.from_xml(filename)
    
    @staticmethod
    def _load_stix2_content(filename: Path) -> Bundle:
        with open(filename, 'rt', encoding='utf-8') as f:
            return stix2_parser(f.read(), allow_custom=True)
    
    def _misp_loading_error(self, filename: Path, exception: str):
        self.errors[filename].add(f'Unable to load MISP content:\n{exception}')
            
    def _stix_loading_error(self, filename: Path, exception: str):
        self.errors[filename].add(f'Unable to load STIX content:\n{exception}')
        
    def _version_error(self, version: Union[int, str]):
        self.errors['init'].add(
            f'Wrong STIX major version: {version}. Must be 1 or 2.'
        )