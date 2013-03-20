from django.utils import unittest

from mrben.main.models import Link


class LinkTestCase(unittest.TestCase):
    def setUp(self):
        self.mrben = Link.objects.create(title='mrben', url='http://mrben.co.uk/')

    def testShit(self):
        self.assertEqual(unicode(self.mrben), 'mrben - http://mrben.co.uk/')
