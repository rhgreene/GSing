import abc
import math
from collections import defaultdict


class Channel():
    """Encapsulates a channel for wave creation.
    One or many waves are registered with the channel

    Keeps track of it's own time starting at zero.
    """

    def __init__(self):
        self._waves = []
        self._observers = defaultdict(list)
        self._elapsed_time = 0.0
        self._countdown = 0.0

    def register_wave(self, wave):
        """Connect a wave mapper.
        """
        self._waves.append(wave)

    def notify_at(self, observer, time):
        """Register an observer to be notified at the specified time.
        Observer will be derigistered upon notification.
        """
        self._observers[time].append(observer)

    def _step_forward(self):
        next_time = sorted(self._observers.keys())[0]
        delta_t = next_time - self._elapsed_time
        for wave in self._waves:
            wave.increment(delta_t)
        for observer in self._observers.pop(next_time):
            observer.notify()


class Observer(abc.ABC):

    @abc.abstractmethod
    def on_notify(self, event):
        """Method called by channel on notification of timestep"""
        pass


class Wave(abc.ABC):
    def __init__(self, acceleration=0.0, velocity=0.0, displacement=0.0):
        self.acceleration = acceleration
        self.velocity = velocity
        self.displacement = displacement

    def increment(self, time_step):
        self.velocity += self.acceleration * time_step
        self.displacement += self.velocity * time_step
        self.trim_angle()

    def trim_angle(self):
        if self.displacement > 2.0 * math.pi:
            rotations = self.displacement / (2.0 * math.pi)
            self.displacement -= math.floor(rotations) * 2.0 * math.pi

    @abc.abstractmethod
    def get_sample(self):
        pass
