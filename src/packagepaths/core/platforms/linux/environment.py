# SPDX-FileCopyrightText: 2023, Metify, Inc. <metify@metify.io>
# SPDX-License-Identifier: BSD-3-Clause

from __future__ import annotations

from typing import Optional

from packagepaths.core.conventions.environment import EnvironmentConvention
from packagepaths.core.package import Package
from packagepaths.core.platforms.linux.base import LinuxPlatform


class LinuxPlatformEnvironmentConvention(LinuxPlatform, EnvironmentConvention):
    def __init__(self, package: Package, /, prefix: Optional[str] = None) -> None:
        LinuxPlatform.__init__(self)
        EnvironmentConvention.__init__(self, package)
        self.package = package
        self.prefix = prefix

    @classmethod
    def detect(cls, package: Package, /, strict: bool = False) -> LinuxPlatformEnvironmentConvention:
        raise NotImplementedError
