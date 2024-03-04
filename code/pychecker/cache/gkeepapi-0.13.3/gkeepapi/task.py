# -*- coding: utf-8 -*-
"""
.. automodule:: gkeepapi
   :members:
   :inherited-members:

.. moduleauthor:: Kai <z@kwi.li>
"""

import datetime
import logging
import time
import random
import enum

logger = logging.getLogger(__name__)

class Task(object):
    pass

    def load(self, raw):
        pass

def from_json(raw):
    """Helper to construct a task from a dict.

    Args:
        raw (dict): Raw task representation.

    Returns:
        Task: A Task object or None.
    """
    task = Task()
    task.load(raw)

    return task
