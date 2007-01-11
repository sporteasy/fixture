
import os
from nose.tools import eq_
from nose.exc import SkipTest
from fixture import Fixture
from fixture.test import env_supports
from fixture.test.test_loader import (  
    LoaderTest, HavingCategoryData, HavingOfferProductData)
from fixture.loader import SQLObjectLoader
from fixture.dataset import MergedSuperSet, DataSet
from fixture.style import NamedDataStyle, PaddedNameStyle, CamelAndUndersStyle
from fixture.examples.db.sqlobject_examples import *
from fixture.test import conf

def setup():
    if not env_supports.sqlobject: raise SkipTest

class SQLObjectLoaderTest(LoaderTest):
    fixture = Fixture(  loader=SQLObjectLoader(
                            style=( NamedDataStyle() + CamelAndUndersStyle()),
                            dsn=conf.MEM_DSN, env=globals()),
                        dataclass=MergedSuperSet )
        
    def setUp(self, dsn=conf.MEM_DSN):
        """should load the dataset"""
        from sqlobject import connectionForURI
        self.conn = connectionForURI(dsn)
        setup_db(self.conn)
        
        from sqlobject import sqlhub
        sqlhub.processConnection = self.conn
        
        self.fixture.loader.connection = self.conn
    
    def tearDown(self):
        """should unload the dataset."""
        teardown_db(self.conn)
        from sqlobject import sqlhub
        sqlhub.processConnection = None

class TestSQLObjectLoader(HavingCategoryData, SQLObjectLoaderTest):
    
    def assert_data_loaded(self, dataset):
        """assert that the dataset was loaded."""
        eq_(Category.get( dataset.gray_stuff.id).name, 
                            dataset.gray_stuff.name)
        eq_(Category.get( dataset.yellow_stuff.id).name, 
                            dataset.yellow_stuff.name)
    
    def assert_data_torndown(self):
        """assert that the dataset was torn down."""
        eq_(Category.select().count(), 0)

class TestSQLObjectLoaderForeignKeys(
                        HavingOfferProductData, SQLObjectLoaderTest):
    # def setUp(self):
    #     if not conf.POSTGRES_DSN:
    #         raise SkipTest
    #         
    #     SQLObjectLoaderTest.setUp(self, dsn=conf.POSTGRES_DSN)
    
    def assert_data_loaded(self, dataset):
        """assert that the dataset was loaded."""
        eq_(Offer.get(dataset.free_truck.id).name, dataset.free_truck.name)
        
        eq_(Product.get(
                dataset.truck.id).name,
                dataset.truck.name)
                
        eq_(Category.get(
                dataset.cars.id).name,
                dataset.cars.name)
        eq_(Category.get(
                dataset.free_stuff.id).name,
                dataset.free_stuff.name)
        
        eq_(dataset.just_some_widget.type, 'foobar')
    
    def assert_data_torndown(self):
        """assert that the dataset was torn down."""
        eq_(Category.select().count(), 0)
        eq_(Offer.select().count(), 0)
        eq_(Product.select().count(), 0)
            