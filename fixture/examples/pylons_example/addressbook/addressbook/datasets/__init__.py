
from builtins import object
from fixture import DataSet

class AddressData(DataSet):
    class joe_in_montego(object):
        address = "111 St. James St, Montego Bay, Jamaica"
    class joe_in_ny(object):
        address = "111 S. 2nd Ave, New York, NY"

class PersonData(DataSet):
    class joe_gibbs(object):
        name = "Joe Gibbs"
        email = "joe@joegibbs.com"
        my_addresses = [
            AddressData.joe_in_montego, 
            AddressData.joe_in_ny]