# SPDX-FileCopyrightText: 2023, Metify, Inc. <metify@metify.io>
# SPDX-License-Identifier: BSD-3-Clause

from typing import Optional


class Package:
    def __init__(
        self,
        name: str,
        /,
        provider: Optional[str] = None,
        project: Optional[str] = None,
        version: Optional[str] = None,
    ):
        self.name = name
        self.provider = provider
        self.project = project
        self.version = version
