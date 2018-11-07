import unittest

from trials import Trials
from MmxConfig import MmxConfig

#-------------------------------------------------------------------------------
# class TrialsTestCase
#
# python -m unittest discover tests/
#-------------------------------------------------------------------------------
class TrialsTestCase(unittest.TestCase):

    #---------------------------------------------------------------------------
    # testInit
    #---------------------------------------------------------------------------
    def testInit(self):
       
        print 'testInit ...'
        
        # Test with an invalid config file.
        with self.assertRaises(TypeError):
            trials = Trials(None, True)
        
        with self.assertRaises(IOError):
            trials = Trials('Nonexistent file', True)
        
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
        trials = Trials(mmxConfig.getConfigFile(), True)

    #---------------------------------------------------------------------------
    # testGenerateFileIndexes
    #---------------------------------------------------------------------------
    def testGenerateFileIndexes(self):
       
        print 'testGenerateFileIndexes ...'
        
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

        trials = Trials(mmxConfig.getConfigFile(), True)
        trials.generateFileIndexes(50)

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
        trials = Trials(mmxConfig.getConfigFile(), True)
        self.assertEqual(trials.config.phase, 'TRIALS')
