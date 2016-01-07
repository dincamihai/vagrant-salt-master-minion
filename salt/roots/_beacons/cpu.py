# -*- coding: utf-8 -*-
"""Test beacon."""

__virtualname__ = 'cpu'

import logging

# Import Salt libs
import salt.utils

# Import Third Party Libs
try:
    import psutil
    HAS_PSUTIL = True
except ImportError:
    HAS_PSUTIL = False


log = logging.getLogger(__name__)


def __virtual__():
    if HAS_PSUTIL is False:
        return False
    else:
        return __virtualname__


def validate(config):
    '''
    Validate the beacon configuration
    '''
    return True


def beacon(config):
    '''
    Watch the configured files

    Example Config

    .. code-block:: yaml

        beacons:
          test: {}
    '''
    ret = [{"cpu%": psutil.cpu_percent()}]
    # Return event data
    return ret
