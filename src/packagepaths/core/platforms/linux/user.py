# SPDX-FileCopyrightText: 2023, Metify, Inc. <metify@metify.io>
# SPDX-License-Identifier: BSD-3-Clause

from __future__ import annotations

from packagepaths.core.conventions.user import UserConvention
from packagepaths.core.package import Package
from packagepaths.core.platforms.linux.base import LinuxPlatform


class LinuxPlatformUserConvention(LinuxPlatform, UserConvention):
    def __init__(self, package: Package, /, local: bool = False) -> None:
        LinuxPlatform.__init__(self)
        UserConvention.__init__(self, package)
        self.package = package
        self.local = local

    @classmethod
    def detect(cls, package: Package, /, strict: bool = False) -> LinuxPlatformUserConvention:
        raise NotImplementedError
