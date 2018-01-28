from .config import Config
from .utils import get_timestamp, til_next_millis

class Instagram(object):
    def __init__(self, epoch = Config.EPOCH):
        self.epoch = epoch
        self.last_timestamp = -1
        self.sequence = 0

    def next(self, logical_shard_id):
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
        timestamp = timestamp - (int(self.epoch)*1000)
        guoidValue = (timestamp << Config.TIMESTAMP_LEFT_SHIFT) |\
                     (logical_shard_id << Config.LOGICAL_SHARD_ID_SHIFT) | self.sequence

        return guoidValue
