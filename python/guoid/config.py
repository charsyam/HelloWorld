# -*- coding:utf-8 -*-
import time

class Config:
    WORKER_ID_BITS = 5
    DATACENTER_ID_BITS = 5
    SEQUENCE_BITS = 12

    WORKER_ID_SHIFT = SEQUENCE_BITS
    DATACENTER_ID_SHIFT = SEQUENCE_BITS + WORKER_ID_BITS
    TIMESTAMP_LEFT_SHIFT = SEQUENCE_BITS + WORKER_ID_BITS + DATACENTER_ID_BITS

    WORKER_ID_MASK = (1 << WORKER_ID_BITS) - 1
    SEQUENCE_MASK = (1 << SEQUENCE_BITS) - 1

    LOGICAL_SHARD_ID_BITS = 10
    LOGICAL_SHARD_ID_MASK = (1 << LOGICAL_SHARD_ID_BITS) - 1
    LOGICAL_SHARD_ID_SHIFT = SEQUENCE_BITS
    EPOCH = time.mktime((2014, 4, 30, 0, 0, 0, 0, 0, 0))
