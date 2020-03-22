import unittest
from gsing.channel import Channel, Observer, Wave


class Test_observer(Observer):
    def on_notify(self, event):
        return True


class Test_wave_flat(Wave):
    def get_sample(self):
        return 1


class channel_resgistration_test(unittest.TestCase):
    def setUp(self):
        self.channel = Channel()
        self.observer = Test_observer()
        self.wave = Test_wave_flat()

    def test_observer_registration(self):
        self.channel.notify_at(self.observer, 0)
        assert self.channel._observers[0] == [self.observer]

    def test_wave_registration(self):
        self.channel.register_wave(self.wave)
        assert self.channel._waves == [self.wave]
