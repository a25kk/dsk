# -*- coding: utf-8 -*-
"""Init and utils."""

from zope.i18nmessageid import MessageFactory

MessageFactory = MessageFactory('dsk.greeting')


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
