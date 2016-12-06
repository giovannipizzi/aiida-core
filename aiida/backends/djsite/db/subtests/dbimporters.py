# -*- coding: utf-8 -*-
"""
Tests for subclasses of DbImporter, DbSearchResults and DbEntry
"""
from django.utils import unittest

from aiida.backends.tests.dbimporters import TestCodDbImporter
from aiida.backends.tests.dbimporters import TestTcodDbImporter
from aiida.backends.tests.dbimporters import TestPcodDbImporter
from aiida.backends.tests.dbimporters import TestMpodDbImporter
from aiida.backends.tests.dbimporters import TestNnincDbImporter
from aiida.backends.djsite.db.testbase import AiidaTestCase

__copyright__ = u"Copyright (c), This file is part of the AiiDA platform. For further information please visit http://www.aiida.net/. All rights reserved."
__license__ = "MIT license, see LICENSE.txt file."
__version__ = "0.7.0"
__authors__ = "The AiiDA team."


class TestCodDbImporterDjango(TestCodDbImporter, AiidaTestCase):
    """
    """
    pass


class TestTcodDbImporterDjango(TestTcodDbImporter, AiidaTestCase):
    """
    """
    pass


class TestPcodDbImporterDjango(TestPcodDbImporter, AiidaTestCase):
    """
    """
    pass


class TestMpodDbImporterDjango(TestMpodDbImporter, AiidaTestCase):
    """
    """
    pass


class TestNnincDbImporterDjango(TestNnincDbImporter, AiidaTestCase):
    """
    """
    pass
