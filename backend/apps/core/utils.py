from typing import List
from typing import Dict

import arrow
import datetime
import logging
import sys
import functools

from django.utils import timezone
from django.utils.timezone import localtime

LOGGER = logging.getLogger("default")
LOGGER.name = __name__


def get_now() -> datetime:
    return localtime(timezone.now())