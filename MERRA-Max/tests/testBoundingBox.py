
import unittest

from BoundingBox import BoundingBox
from PresencePoints import PresencePoints

#-------------------------------------------------------------------------------
# class BoundingBoxTestCase
#
# python -m unittest discover tests/
#-------------------------------------------------------------------------------
class BoundingBoxTestCase(unittest.TestCase):

    #---------------------------------------------------------------------------
    # testInit
    #---------------------------------------------------------------------------
    def testInit(self):
       
        print 'testInit ...'
        
        validFile = 'tests/WLBG-geog.csv'
        presPts   = PresencePoints(validFile, 'WLBG')
        bbox      = BoundingBox(presPts.points, presPts.epsg)

    #---------------------------------------------------------------------------
    # testGetBoundingBox
    #---------------------------------------------------------------------------
    def testGetBoundingBox(self):
        
        validFile = 'tests/WLBG-geog.csv'
        presPts   = PresencePoints(validFile, 'WLBG')
        bbox      = BoundingBox(presPts.points, presPts.epsg)

        expected = (-76.8933333297525, -76.8579444453814, 39.3381111142888, 39.4326111107889)
        self.assertEqual(expected, bbox.getBoundingBox())
        
    #---------------------------------------------------------------------------
    # testGetEpsg
    #---------------------------------------------------------------------------
    def testGetEpsg(self):
        
        validFile = 'tests/WLBG-geog.csv'
        presPts   = PresencePoints(validFile, 'WLBG')
        bbox      = BoundingBox(presPts.points, presPts.epsg)
        self.assertEqual('4326', bbox.getEpsg())

    #---------------------------------------------------------------------------
    # testLrx
    #---------------------------------------------------------------------------
    def testLrx(self):
        
        validFile = 'tests/WLBG-geog.csv'
        presPts   = PresencePoints(validFile, 'WLBG')
        bbox      = BoundingBox(presPts.points, presPts.epsg)
        self.assertEqual(-76.8579444453814, bbox.getLrx())

    #---------------------------------------------------------------------------
    # testLry
    #---------------------------------------------------------------------------
    def testLry(self):
        
        validFile = 'tests/WLBG-geog.csv'
        presPts   = PresencePoints(validFile, 'WLBG')
        bbox      = BoundingBox(presPts.points, presPts.epsg)
        self.assertEqual(39.3381111142888, bbox.getLry())

    #---------------------------------------------------------------------------
    # testUlx
    #---------------------------------------------------------------------------
    def testUlx(self):
        
        validFile = 'tests/WLBG-geog.csv'
        presPts   = PresencePoints(validFile, 'WLBG')
        bbox      = BoundingBox(presPts.points, presPts.epsg)
        self.assertEqual(-76.8933333297525, bbox.getUlx())

    #---------------------------------------------------------------------------
    # testUly
    #---------------------------------------------------------------------------
    def testUly(self):
        
        validFile = 'tests/WLBG-geog.csv'
        presPts   = PresencePoints(validFile, 'WLBG')
        bbox      = BoundingBox(presPts.points, presPts.epsg)
        self.assertEqual(39.4326111107889, bbox.getUly())


