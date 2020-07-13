#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#   (C) Copyright 2020 Hewlett Packard Enterprise Development LP
#
#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.

"""Module with abstract device class."""


import logging
from abc import ABC, abstractmethod

from hpestorapi.exceptions import WrongParameter


if __name__ == "__main__":
    pass

logging.getLogger('hpestorapi.base').addHandler(logging.NullHandler())
LOG = logging.getLogger('hpestorapi.base')


class BaseDevice(ABC):
    """Base device abstract class."""

    def __init__(self):
        """Initialize base device object."""
        # Default timeouts:
        # ConnectionTimeout = 1 second, ReadTimeout = infinity
        self._timeout = (1, None)

    @property
    def timeout(self):
        """
        Rest API client timeout.

        Number of seconds that Rest API client waits for a response from
        Rest API server before generating a timeout exception.
        Different timeouts for connection setup and for getting first piece
        of data can be used. In this case, use tuple(float, float) with the
        first value being a connection delay and with the second value being
        a read delay. Alternatively, you can use one float value for both
        types of timeouts. 'None' value can be used instead not to limit the
        device response time. Default value: (1, None).
        """
        return self._timeout

    @timeout.setter
    def timeout(self, delay):
        if isinstance(delay, (float, int)):
            self._timeout = (delay, delay)
        elif isinstance(delay, tuple):
            self._timeout = delay
        elif delay is None:
            self._timeout = (None, None)
        else:
            raise WrongParameter('Wrong timeout value.')

    @property
    @abstractmethod
    def _base_url(self) -> str:
        """
        Generate static part of URL.

        :rtype: str
        :return: Static part of URL
        """
        raise NotImplementedError
