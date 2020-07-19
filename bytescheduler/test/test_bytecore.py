#!/usr/bin/python

from __future__ import absolute_import
import time
import sys
import logging
from bytescheduler.common.bytecore import core
from bytescheduler.common.bytetask import ByteTask

class TestTask(ByteTask):

    def _additional_init(self):
        self.start_time = self.kwargs["start_time"]
        return

    def _prepare(self):
        self.notify_ready()
        return

    def _do(self):
        return

    def _wait_until_finish(self):
        need_time = self.tensor_size() / 1000.0
        time.sleep(max(0, self.start_time + need_time - time.time()))
        return

    def _tensor_size(self):
        return self._tensor

    def _partition_tensor(self, size):
        partitions = []
        number = self.tensor_size() / size
        for i in range(number):
            partitions.append(self.tensor_size() * 1.0 / number)
        return partitions

    def _notify_upper_layer_finish(self):
        print("Finished task {} in {} seconds!".format(self.name, time.time() - self.start_time))
        return




def test_core():
    core.start(rank=0, arch="ps")
    start = time.time()
    for i in reversed(range(3)):
        print("Post task {}".format(i))
        t = TestTask(i, 1000*(i+1), "allreduce", start_time=time.time(), add_notify_finish_trigger=True)
        t.priority = i
        core.post(t)
    core.shutdown(wait_for_all=True)
    print("Finished all tasks in {} seconds!".format(time.time() - start))


if __name__ == '__main__':
    if len(sys.argv) < 1:
        print("Usage: test_bytecore.py [debug_flag]")
        exit(1)

    if len(sys.argv) >= 2:
        logger = logging.getLogger("ByteScheduler")
        logger.setLevel(logging.DEBUG)

    test_core()
