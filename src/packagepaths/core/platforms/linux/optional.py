# SPDX-FileCopyrightText: 2023, Metify, Inc. <metify@metify.io>
# SPDX-License-Identifier: BSD-3-Clause

from __future__ import annotations

from typing import Optional

from packagepaths.core.conventions.optional import OptionalConvention
from packagepaths.core.defaults import (
    DEFAULT_LINUX_PLATFORM_OPTIONAL_CONVENTION_BASE,
    DEFAULT_LINUX_PLATFORM_OPTIONAL_CONVENTION_HYBRID_ETC_BASE,
)
from packagepaths.core.package import Package
from packagepaths.core.platforms.linux.base import LinuxPlatform


class LinuxPlatformOptionalConvention(LinuxPlatform, OptionalConvention):
    def __init__(
        self,
        package: Package,
        /,
        base: Optional[str] = DEFAULT_LINUX_PLATFORM_OPTIONAL_CONVENTION_BASE,
        hybrid: bool = False,
        hybrid_etc_base: str = DEFAULT_LINUX_PLATFORM_OPTIONAL_CONVENTION_HYBRID_ETC_BASE,
    ) -> None:
        LinuxPlatform.__init__(self)
        OptionalConvention.__init__(self, package)
        self.package = package
        self.base = base
        self.hybrid = hybrid
        self.hybrid_etc_base = hybrid_etc_base

    @classmethod
    def detect(cls, package: Package, /, strict: bool = False) -> LinuxPlatformOptionalConvention:
        raise NotImplementedError
