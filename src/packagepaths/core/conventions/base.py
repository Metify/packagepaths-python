# SPDX-FileCopyrightText: 2023, Metify, Inc. <metify@metify.io>
# SPDX-License-Identifier: BSD-3-Clause

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Type

from packagepaths.core.package import Package


class Standard(ABC):
    def __init__(self, package: Package, /):
        self.package = package

    @property
    @abstractmethod
    def path_class(self) -> Type[Path]:
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def detect(cls, package: Package, /, strict: bool = False) -> Standard:
        return cls(package)

    @property
    @abstractmethod
    def cache_path(self) -> Path:
        raise NotImplementedError

    @property
    @abstractmethod
    def config_path(self) -> Path:
        raise NotImplementedError

    @property
    @abstractmethod
    def data_path(self) -> Path:
        raise NotImplementedError

    @property
    @abstractmethod
    def log_path(self) -> Path:
        raise NotImplementedError

    @property
    @abstractmethod
    def runtime_path(self) -> Path:
        raise NotImplementedError

    @property
    @abstractmethod
    def tmp_path(self) -> Path:
        raise NotImplementedError
