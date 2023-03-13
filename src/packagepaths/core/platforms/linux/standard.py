# SPDX-FileCopyrightText: 2023, Metify, Inc. <metify@metify.io>
# SPDX-License-Identifier: BSD-3-Clause

from __future__ import annotations

from packagepaths.core.conventions.standard import StandardConvention
from packagepaths.core.package import Package
from packagepaths.core.platforms.linux.base import LinuxPlatform


class LinuxPlatformStandardConvention(LinuxPlatform, StandardConvention):
    def __init__(self, package: Package, /, local: bool = False) -> None:
        LinuxPlatform.__init__(self)
        StandardConvention.__init__(self, package)
        self.package = package
        self.local = local

    @classmethod
    def detect(cls, package: Package, /, strict: bool = False) -> LinuxPlatformStandardConvention:
        raise NotImplementedError
