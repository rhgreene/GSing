import unittest
from gsing.channel import Channel, Observer, Wave


class TestObserver(Observer):
    def on_notify(self, event):
        return True

class TestWaveFlat(Wave):
    def get_sample(self):
        return 1


class ChannelResgistrationTest(unittest.TestCase):
    def setUp(self):
        self.channel = Channel()
        self.observer = TestObserver()
        self.wave = TestWaveFlat()

    def test_observer_registration(self):
        self.channel.notify_at(self.observer, 0)
        assert self.channel._observers[0] == [self.observer]

    def test_wave_registration(self):
        self.channel.register_wave(self.wave)
        assert self.channel._waves == [self.wave]

# class ChannelBiddingTest(unittest.TestCase):
#     def setUp(self):
#         self.channel = Channel()
#         self.observers = {
#             a: Test_observer(),
#             b: Test_observer(),
#             c: Test_observer(),
#             d: Test_observer(),
#             e: Test_observer(),
#             f: Test_observer(),
#             g: Test_observer(),
#         }
#         self.wave = Test_wave_flat()