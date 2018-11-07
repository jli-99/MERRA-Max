
from datetime import datetime
import json
import os
import unittest

from MmxConfig import MmxConfig

#-------------------------------------------------------------------------------
# class MmxConfigTestCase
#
# python -m unittest discover tests/
#-------------------------------------------------------------------------------
class MmxConfigTestCase(unittest.TestCase):

    #---------------------------------------------------------------------------
    # testInit
    #---------------------------------------------------------------------------
    def testInit(self):
       
        print 'testInit ...'
        
        mmxConfig = MmxConfig()
        self.assertEqual(mmxConfig.phase,        'Unknown')
        self.assertEqual(mmxConfig.state,        'Pending')
        self.assertEqual(mmxConfig.configFile,   None)
        self.assertEqual(mmxConfig.numProcesses, 10)
        self.assertEqual(mmxConfig.numTrials,    10)
        self.assertEqual(mmxConfig.startDate,    None)
        self.assertEqual(mmxConfig.endDate,      None)
        self.assertEqual(mmxConfig.outDir,       '.')
        self.assertEqual(mmxConfig.presFile,     None)
        self.assertEqual(mmxConfig.species,      'species')
        # self.assertEqual(mmxConfig.trialTuples,  [])
        self.assertEqual(mmxConfig.topTen,       None)

    #---------------------------------------------------------------------------
    # testFromDict
    #---------------------------------------------------------------------------
    def testFromDict(self):
       
        print 'testFromDict ...'

        mmxConfig = MmxConfig()
        mmxDict = mmxConfig.toDict()
        mmxConfig2 = MmxConfig()
        mmxConfig2.fromDict(mmxDict)
        self.assertEqual(mmxDict, mmxConfig2.toDict())
        
    #---------------------------------------------------------------------------
    # testGetConfigFile
    #---------------------------------------------------------------------------
    def testGetConfigFile(self):
       
        print 'testGetConfigFile ...'

        mmxConfig = MmxConfig()
        self.assertEqual(mmxConfig.configFile, None)
        mmxConfig.write()
        self.assertEqual(mmxConfig.configFile, './config.mmx')
        os.remove(mmxConfig.configFile)
        
    #---------------------------------------------------------------------------
    # testInitializeFromFile
    #---------------------------------------------------------------------------
    def testInitializeFromFile(self):
       
        print 'testInitializeFromFile ...'
        
        mmxConfig = MmxConfig()
        mmxConfig.write()
        mmxConfig2 = MmxConfig()
        mmxConfig2.initializeFromFile(mmxConfig.getConfigFile())
        self.assertEqual(mmxConfig.toDict(), mmxConfig2.toDict())
        
    #---------------------------------------------------------------------------
    # testInitializeFromValues
    #---------------------------------------------------------------------------
    def testInitializeFromValues(self):
       
        print 'testInitializeFromValues ...'
        
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
                                       
        self.assertEqual(mmxConfig.phase,        'Unknown')
        self.assertEqual(mmxConfig.state,        'Pending')
        self.assertEqual(mmxConfig.configFile,   None)
        self.assertEqual(mmxConfig.numProcesses, numProcs)
        self.assertEqual(mmxConfig.numTrials,    numTrials)
        
        d = datetime.strptime(startDate, '%m-%d-%Y').date()
        self.assertEqual(mmxConfig.startDate, d)
        
        d = datetime.strptime(endDate, '%m-%d-%Y').date()
        self.assertEqual(mmxConfig.endDate, d)
        
        self.assertEqual(mmxConfig.outDir,       outDir)
        self.assertEqual(mmxConfig.presFile,     presFile)
        self.assertEqual(mmxConfig.species,      species)
        # self.assertEqual(mmxConfig.trialTuples,  [])
        self.assertEqual(mmxConfig.topTen,       None)

    #---------------------------------------------------------------------------
    # testSetEndDate
    #---------------------------------------------------------------------------
    def testSetEndDate(self):
       
        print 'testSetEndDate ...'
        
        mmxConfig = MmxConfig()
        
        with self.assertRaises(ValueError):
            mmxConfig.setEndDate('111-22-3333')
        
        with self.assertRaises(ValueError):
            mmxConfig.setEndDate('02-31-2017')
        
        with self.assertRaises(ValueError):
            mmxConfig.setEndDate('01/01/2017')
        
        dStr = '01-01-2017'
        mmxConfig.setEndDate(dStr)
        d = datetime.strptime(dStr, '%m-%d-%Y').date()
        self.assertEqual(mmxConfig.endDate, d)
        
        dStr = '2-2-2017'
        mmxConfig.setEndDate(dStr)
        d = datetime.strptime(dStr, '%m-%d-%Y').date()
        self.assertEqual(mmxConfig.endDate, d)
        
    #---------------------------------------------------------------------------
    # testSetEPSG
    #---------------------------------------------------------------------------
    def testSetEPSG(self):
        
        print 'testSetEPSG ...'
        
        mmxConfig = MmxConfig()
        self.assertEqual(None, mmxConfig.epsg)

        mmxConfig.setEPSG(None)

        with self.assertRaises(IndexError):
            mmxConfig.setEPSG('EPSG26912')
            
        mmxConfig.setEPSG('EPSG:26912')
        self.assertEqual(26912, mmxConfig.epsg)
        mmxConfig.setEPSG('4326')
        self.assertEqual(4326, mmxConfig.epsg)

    #---------------------------------------------------------------------------
    # testSetLrx
    #---------------------------------------------------------------------------
    def testSetLrx(self):
       
        print 'testSetLrx ...'
        
        mmxConfig = MmxConfig()
        mmxConfig.setLrx(None)

        with self.assertRaises(ValueError):
            mmxConfig.setLrx('d')
        
        mmxConfig.setLrx(30)

        with self.assertRaises(RuntimeError):

            mmxConfig.ulx = 20
            mmxConfig.setLrx(10)
            
    #---------------------------------------------------------------------------
    # testSetLry
    #---------------------------------------------------------------------------
    def testSetLry(self):
       
        print 'testSetLry ...'
        
        mmxConfig = MmxConfig()
        mmxConfig.setLry(None)

        with self.assertRaises(ValueError):
            mmxConfig.setLry('d')
        
        mmxConfig.setLry(30)

        with self.assertRaises(RuntimeError):

            mmxConfig.uly = 10
            mmxConfig.setLry(20)
            
    #---------------------------------------------------------------------------
    # testSetNumProcs
    #---------------------------------------------------------------------------
    def testSetNumProcs(self):
       
        print 'testSetNumProcs ...'
        
        mmxConfig = MmxConfig()
        self.assertEqual(mmxConfig.numProcesses, 10)
        mmxConfig.setNumProcs(-2112)
        self.assertEqual(mmxConfig.numProcesses, 10)
        mmxConfig.setNumProcs(2112)
        self.assertEqual(mmxConfig.numProcesses, 10)
        mmxConfig.setNumProcs(500)
        self.assertEqual(mmxConfig.numProcesses, 500)
        
    #---------------------------------------------------------------------------
    # testSetNumTrials
    #---------------------------------------------------------------------------
    def testSetNumTrials(self):
       
        print 'testSetNumTrials ...'
        
        mmxConfig = MmxConfig()
        self.assertEqual(mmxConfig.numTrials, 10)
        mmxConfig.setNumTrials(-2112)
        self.assertEqual(mmxConfig.numTrials, 10)
        mmxConfig.setNumTrials(2112)
        self.assertEqual(mmxConfig.numTrials, 2112)
        mmxConfig.setNumTrials(500)
        self.assertEqual(mmxConfig.numTrials, 500)
                                     
    #---------------------------------------------------------------------------
    # testSetOutDir
    #---------------------------------------------------------------------------
    def testSetOutDir(self):
       
        print 'testSetOutDir ...'

        mmxConfig = MmxConfig()
        self.assertEqual(mmxConfig.outDir, '.')

        with self.assertRaises(RuntimeError):
            mmxConfig.setOutDir(None)
        
        with self.assertRaises(RuntimeError):
            mmxConfig.setOutDir('/bogus/path')

        with self.assertRaises(RuntimeError):
            mmxConfig.setOutDir('tests/WLBG-geog.csv')
            
        mmxConfig.setOutDir(os.getcwd())
        self.assertEqual(mmxConfig.outDir, os.getcwd())
        
    #---------------------------------------------------------------------------
    # testSetPresFile
    #---------------------------------------------------------------------------
    def testSetPresFile(self):
       
        print 'testSetPresFile ...'
        
        mmxConfig = MmxConfig()
        self.assertEqual(mmxConfig.presFile, None)
        
        mmxConfig.setPresFile(None)
            
        with self.assertRaises(RuntimeError):
            mmxConfig.setPresFile('does/not/exist/config.mmx')
            
        with self.assertRaises(RuntimeError):
            mmxConfig.setPresFile('tests')

        with self.assertRaises(RuntimeError):
            mmxConfig.setPresFile('MmxConfig.py')
            
        validFile = 'tests/WLBG-geog.csv'
        mmxConfig.setPresFile(validFile)
        self.assertEqual(mmxConfig.presFile, validFile)

    #---------------------------------------------------------------------------
    # testSetSpecies
    #---------------------------------------------------------------------------
    def testSetSpecies(self):
       
        print 'testSetSpecies ...'
        
        mmxConfig = MmxConfig()
        
        with self.assertRaises(RuntimeError):
            mmxConfig.setSpecies('')
            
        mmxConfig.setSpecies('WLBG')
        self.assertEqual(mmxConfig.species, 'WLBG')
        
    #---------------------------------------------------------------------------
    # testSetStartDate
    #---------------------------------------------------------------------------
    def testSetStartDate(self):
       
        print 'testSetStartDate ...'
        
        mmxConfig = MmxConfig()
        
        with self.assertRaises(ValueError):
            mmxConfig.setStartDate('111-22-3333')

        with self.assertRaises(ValueError):
            mmxConfig.setStartDate('02-31-2017')

        with self.assertRaises(ValueError):
            mmxConfig.setStartDate('01/01/2017')
            
        dStr = '01-01-2017'
        mmxConfig.setStartDate(dStr)
        d = datetime.strptime(dStr, '%m-%d-%Y').date()
        self.assertEqual(mmxConfig.startDate, d)
        
        dStr = '2-2-2017'
        mmxConfig.setStartDate(dStr)
        d = datetime.strptime(dStr, '%m-%d-%Y').date()
        self.assertEqual(mmxConfig.startDate, d)
            
        with self.assertRaises(RuntimeError):
            mmxConfig.setEndDate('1-1-2017')
            mmxConfig.setStartDate('1-2-2017')
        
    #---------------------------------------------------------------------------
    # testSetStateComplete
    #---------------------------------------------------------------------------
    def testSetStateComplete(self):
       
        print 'testSetStateComplete ...'
        
        mmxConfig = MmxConfig()
        mmxConfig.setStateComplete()
        self.assertEqual(mmxConfig.state, MmxConfig.STATES['COMPLETE'])

    #---------------------------------------------------------------------------
    # testSetStateFailed
    #---------------------------------------------------------------------------
    def testSetStateFailed(self):
       
        print 'testSetStateFailed ...'
        
        mmxConfig = MmxConfig()
        self.assertEqual(mmxConfig.state, MmxConfig.STATES['PENDING'])
        mmxConfig.setStateFailed()
        self.assertEqual(mmxConfig.state, MmxConfig.STATES['FAILED'])

    #---------------------------------------------------------------------------
    # testSetStatePending
    #---------------------------------------------------------------------------
    def testSetStatePending(self):
       
        print 'testSetStatePending ...'
        
        mmxConfig = MmxConfig()
        mmxConfig.setStateFailed()
        mmxConfig.setStatePending()
        self.assertEqual(mmxConfig.state, MmxConfig.STATES['PENDING'])

    #---------------------------------------------------------------------------
    # testSetStateRunning
    #---------------------------------------------------------------------------
    def testSetStateRunning(self):
       
        print 'testSetStateRunning ...'
        
        mmxConfig = MmxConfig()
        mmxConfig.setStateFailed()
        mmxConfig.setStateRunning()
        self.assertEqual(mmxConfig.state, MmxConfig.STATES['RUNNING'])

    #---------------------------------------------------------------------------
    # testSetUlx
    #---------------------------------------------------------------------------
    def testSetUlx(self):
       
        print 'testSetUlx ...'
        
        mmxConfig = MmxConfig()
        mmxConfig.setUlx(None)

        with self.assertRaises(ValueError):
            mmxConfig.setUlx('d')
        
        mmxConfig.setUlx(30)

        with self.assertRaises(RuntimeError):

            mmxConfig.lrx = 10
            mmxConfig.setUlx(20)
            
    #---------------------------------------------------------------------------
    # testSetUly
    #---------------------------------------------------------------------------
    def testSetUly(self):
       
        print 'testSetUly ...'
        
        mmxConfig = MmxConfig()
        mmxConfig.setUly(None)

        with self.assertRaises(ValueError):
            mmxConfig.setUly('d')
        
        mmxConfig.setUly(30)

        with self.assertRaises(RuntimeError):

            mmxConfig.lry = 20
            mmxConfig.setUly(10)
            
    #---------------------------------------------------------------------------
    # testToDict
    #---------------------------------------------------------------------------
    def testToDict(self):
       
        print 'testToDict ...'

        mmxConfig = MmxConfig()
        result = mmxConfig.toDict()
                    
        expected = {MmxConfig.CONFIG_FILE_KEY  : None,
                    MmxConfig.END_DATE_KEY     : None,
                    MmxConfig.EPSG_KEY         : None,
                    MmxConfig.LRX_KEY          : None,
                    MmxConfig.LRY_KEY          : None,
                    MmxConfig.NUM_PROCS_KEY    : 10,
                    MmxConfig.NUM_TRIALS_KEY   : 10,
                    MmxConfig.OUT_DIR_KEY      : '.',
                    MmxConfig.PHASE_KEY        : 'Unknown',
                    MmxConfig.PRES_FILE_KEY    : None,
                    MmxConfig.SPECIES_KEY      : 'species',
                    MmxConfig.START_DATE_KEY   : None,
                    MmxConfig.STATE_KEY        : 'Pending',
                    MmxConfig.TOP_TEN_KEY      : None,
                    # MmxConfig.TRIAL_TUPLES_KEY : [],
                    MmxConfig.ULX_KEY          : None,
                    MmxConfig.ULY_KEY          : None}

        self.assertEqual(result, expected)
        
        startDate = '01-01-2016'
        endDate = '01-01-2017'
        mmxConfig.setStartDate(startDate)
        mmxConfig.setEndDate(endDate)
        
        result = mmxConfig.toDict()
        
        expected = {MmxConfig.CONFIG_FILE_KEY  : None,
                    MmxConfig.END_DATE_KEY     : endDate,
                    MmxConfig.EPSG_KEY         : None,
                    MmxConfig.LRX_KEY          : None,
                    MmxConfig.LRY_KEY          : None,
                    MmxConfig.NUM_PROCS_KEY    : 10,
                    MmxConfig.NUM_TRIALS_KEY   : 10,
                    MmxConfig.OUT_DIR_KEY      : '.',
                    MmxConfig.PHASE_KEY        : 'Unknown',
                    MmxConfig.PRES_FILE_KEY    : None,
                    MmxConfig.SPECIES_KEY      : 'species',
                    MmxConfig.START_DATE_KEY   : startDate,
                    MmxConfig.STATE_KEY        : 'Pending',
                    MmxConfig.TOP_TEN_KEY      : None,
                    MmxConfig.ULX_KEY          : None,
                    MmxConfig.ULY_KEY          : None}

        self.assertEqual(result, expected)
        
    #---------------------------------------------------------------------------
    # testWrite
    #---------------------------------------------------------------------------
    def testWrite(self):
       
        print 'testWrite ...'
        
        mmxConfig = MmxConfig()
        mmxConfig.write()
        expected = json.dumps(mmxConfig.toDict(), indent = 0)

        result = None
        
        with open(mmxConfig.configFile, 'r') as f:
            result = f.read()

        self.assertEqual(result, expected)
        os.remove(mmxConfig.configFile)

#-------------------------------------------------------------------------------
# main
#-------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()

