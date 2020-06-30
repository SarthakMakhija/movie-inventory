from typing import Set

from aws_xray_sdk.core import patch as xray_patch


def patch(libraries: Set[str]):
    xray_patch(libraries)
