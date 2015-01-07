from ..dynamic_replicator_block import DynamicReplicator
from nio.util.support.block_test_case import NIOBlockTestCase
from nio.common.signal.base import Signal


class DummySignal(Signal):

    def __init__(self, val, list=[None]):
        super().__init__()
        self.val = val
        self.list = list


class TestDynamicReplicator(NIOBlockTestCase):

    def setUp(self):
        super().setUp()
        self.last_notified = []

    def signals_notified(self, signals, output_id='default'):
        self.last_notified = signals

    def test_block(self):
        signals = [DummySignal("a banana!", [1, 2])]
        attrs = signals[0].__dict__
        blk = DynamicReplicator()
        self.configure_block(blk, {'title': 'new_value',
                                   'list': '{{$list}}'})
        blk.start()
        blk.process_signals(signals)
        self.assertEqual(len(self.last_notified), 2)
        self.assertTrue(self.last_notified[0].new_value in [1, 2])
        self.assertTrue(self.last_notified[1].new_value in [1, 2])
