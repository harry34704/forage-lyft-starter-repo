import unittest
from datetime import datetime, timedelta
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class TestCapuletEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        capulet_engine = CapuletEngine(50000, 20000)
        capulet_engine.last_service_mileage = 30000
        self.assertTrue(capulet_engine.engine_should_be_serviced())

class TestSternmanEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        sternman_engine = SternmanEngine(datetime(2020, 1, 1), True)
        self.assertTrue(sternman_engine.engine_should_be_serviced())

class TestWilloughbyEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        willoughby_engine = WilloughbyEngine(70000, 30000)
        willoughby_engine.last_service_mileage = 50000
        self.assertTrue(willoughby_engine.engine_should_be_serviced())

    def test_engine_should_not_be_serviced(self):
        willoughby_engine = WilloughbyEngine(70000, 30000)
        willoughby_engine.last_service_mileage = 80000
        self.assertFalse(willoughby_engine.engine_should_be_serviced())

if __name__ == '__main__':
    unittest.main()
