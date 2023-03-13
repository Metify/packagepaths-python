# SPDX-FileCopyrightText: 2023, Metify, Inc. <metify@metify.io>
# SPDX-License-Identifier: BSD-3-Clause

from pathlib import PosixPath
from typing import Type

from packagepaths.core.package import Package


class LinuxPlatform:
    path_class: Type[PosixPath] = PosixPath

    def append_package_path_parts(self, package: Package, path: PosixPath) -> PosixPath:
        if package.provider:
            path = path / package.provider
        if package.project:
            path = path / package.project
        path = path / package.name
        if package.version:
            path = path / package.version
        return path
