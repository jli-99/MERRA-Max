import unittest

from pydap.client import open_url
from pydap.client import open_dods
from pydap.cas.urs import setup_session
import os
import netrc
import gdal
import xarray



class OpenDapTestCase(unittest.TestCase):

    #---------------------------------------------------------------------------
    # test access to M2 data
    #---------------------------------------------------------------------------

    def testOpenDap(self):

        print 'testOpenDap NASA EARTHDATA'

        # Get authentication from the .netrc file
        netrc_file = '/home/jli/.netrc'

        if os.path.isfile(netrc_file):
            logins = netrc.netrc()
            accounts = logins.hosts
            for host, info in accounts.iteritems():
                self.login, self.account, self.password = info



        #dataset_url = 'https://goldsmr5.gesdisc.eosdis.nasa.gov:443/opendap/MERRA2/M2I3NPASM.5.12.4/1986/12/MERRA2_100.inst3_3d_asm_Np.19861201.nc4'
        dataset_url = 'https://goldsmr4.gesdisc.eosdis.nasa.gov/dods/M2T1NXSLV.dods?t2m[1:2][1:5][7:14]'
        dataset_url = 'https://goldsmr4.gesdisc.eosdis.nasa.gov/dods/M2T1NXSLV.dods?t2m'
        session = setup_session(self.login,self.password,check_url=dataset_url)
        #dataset = open_url(dataset_url,session=session)
        #dataset_url = 'https://goldsmr4.gesdisc.eosdis.nasa.gov/dods/M2T1NXSLV.dods?t2m[1:2][1:5][7:14]'
        dataset = open_dods(dataset_url,session=session)
        #store = xarray.backends.PydapDataStore(dataset)
        #ds = xarray.open_dataset(store)

        #print ds.keys()
        print type(dataset)
        print dataset.keys()

    def testGdalTrans(self):
        self.merraDir = "/home/jli/workspace/mmx/MERRA-Max/RAW_MERRA/"
        ncFiles = glob.glob(os.path.join(self.merraDir, "*.nc"))
        if len(ncFiles) >= 1:
            for f in ncFiles:
                ds = gdal.Translate(self.merraDir + ".tiff", self.merraDir + '/' + f, format="GTiff",
                                    srcSRS="EPSG:4326")
                ds = None
        else:
            raise RuntimeError('There is no raw data file available.')

    def testURLs(self):
        base = 'https://goldsmr5.gesdisc.eosdis.nasa.gov:443/opendap/MERRA2/M2I3NPASM.5.12.4/1986/12/MERRA2_100.inst3_3d_asm_Np.19861201.nc4'
        files = [base % d for d in range(0,24,6)]
        print files

if __name__ == '__main__':
    unittest.main()