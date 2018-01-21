import logging
import threading
try:
    import Queue
except ImportError:
    import queue as Queue

logger = logging.getLogger(__name__)


class DelayedPost(object):
    def __init__(self, timer):
        self.__timer = timer

    def cancel(self):
        self.__timer.cancel()


class Zyklus(object):
    def __init__(self):
        self.eventQueue = Queue.Queue()
        self.terminated = False

    def loop(self):
        if self.terminated:
            raise ValueError("Already terminated")

        logger.debug("Starting event loop")
        while not self.terminated:
            self.exec_callable(self.eventQueue.get())

        logger.debug("Event loop terminated")

    def terminate(self):
        logger.debug("Going to terminate loop")
        if not self.terminated:
            self.post(self.__do_terminate)

    def __do_terminate(self):
        logger.debug("Terminating loops")
        self.terminated = True

    def post(self, clbl):
        if self.__class__.ensure_postable(clbl):
            if not self.terminated:
                self.eventQueue.put(clbl)
            else:
                logger.warning("Loop already terminated, won't post")
        else:
            pass

    @staticmethod
    def is_callable(clbl):
        return hasattr(clbl, '__call__') or callable(clbl)

    @classmethod
    def ensure_postable(cls, clbl):
        assert cls.is_callable(clbl), "Can't post non-callables"
        return True

    def post_delayed(self, clbl, t):
        assert type(t) in (int, float)
        self.__class__.ensure_postable(clbl)
        t = threading.Timer(t, self.post, args=(clbl,))
        t.start()
        return DelayedPost(t)

    def exec_callable(self, clbl):
        clbl()