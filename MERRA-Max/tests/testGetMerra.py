import unittest

from getMerra import GetMerra
from MmxConfig import MmxConfig

#-------------------------------------------------------------------------------
# class GetMerraTestCase
#
# python -m unittest discover tests/
#-------------------------------------------------------------------------------
class GetMerraTestCase(unittest.TestCase):

    #---------------------------------------------------------------------------
    # testInit
    #---------------------------------------------------------------------------
    def testInit(self):
       
        print 'testInit ...'
        
        # Test with an invalid config file.
        with self.assertRaises(TypeError):
            gm = GetMerra(None, True)
        
        with self.assertRaises(IOError):
            gm = GetMerra('Nonexistent file', True)
        
        # Create a config file.
        mmxConfig = MmxConfig()
        presFile  = 'tests/WLBG-geog.csv'
        startDate = '1-1-2016'
        endDate   = '1-1-2017'
        outDir    = '../'
        numProcs  = 500
        numTrials = 200
        species   = 'WLBG'
        
        mmxConfig.initializeFromValues(presFile, startDate, endDate, species,
                                       outDir, numProcs, numTrials)
                                       
        mmxConfig.write()

        # Initialize GetMerra 
        mmxConfig.setStateComplete()
        gm = GetMerra(mmxConfig.getConfigFile(), True)

    #---------------------------------------------------------------------------
    # testGetPhase
    #---------------------------------------------------------------------------
    def testGetPhase(self):
       
        print 'testGetPhase ...'
        
        mmxConfig = MmxConfig()
        presFile  = 'tests/WLBG-geog.csv'
        startDate = '1-1-2016'
        endDate   = '1-1-2017'
        outDir    = '../'
        numProcs  = 500
        numTrials = 200
        species   = 'WLBG'
        
        mmxConfig.initializeFromValues(presFile, startDate, endDate, species,
                                       outDir, numProcs, numTrials)
                                       
        mmxConfig.write()

        # Initialize GetMerra 
        mmxConfig.setStateComplete()
        gm = GetMerra(mmxConfig.getConfigFile(), True)
        self.assertEqual(gm.config.phase, 'MERRA')
