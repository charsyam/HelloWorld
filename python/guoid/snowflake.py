from .config import Config
from .utils import get_timestamp, til_next_millis

class SnowFlake(object):
    def __init__(self, datacenter_id, worker_id, epoch = Config.EPOCH):
        self.epoch = epoch
        self.datacenter_id = (datacenter_id & Config.DATACENTER_ID_BITS) << \
                              Config.DATACENTER_ID_SHIFT
        self.worker_id = (worker_id & Config.WORKER_ID_BITS) << \
                          Config.WORKER_ID_SHIFT

        self.last_timestamp = -1
        self.sequence = 0

    def next(self):
        timestamp = get_timestamp()
        if (timestamp < self.last_timestamp):
            raise "Clock moved backwards"

        if (timestamp == self.last_timestamp):
            self.sequence = (self.sequence + 1) & Config.SEQUENCE_MASK
            if (self.sequence == 0):
                timestamp = til_next_millis(self.last_timestamp)
            else:
                self.sequence = 0

        self.last_timestamp = timestamp
        timestamp = timestamp - (int(self.epoch*1000))
        guoidValue = (timestamp << Config.TIMESTAMP_LEFT_SHIFT) |\
                     (self.datacenter_id | (self.worker_id) | self.sequence)

        return guoidValue
