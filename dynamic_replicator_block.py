from nio.common.block.base import Block
from nio.common.signal.base import Signal
from nio.common.discovery import Discoverable, DiscoverableType
from nio.metadata.properties.string import StringProperty
from nio.metadata.properties.expression import ExpressionProperty


@Discoverable(DiscoverableType.block)
class DynamicReplicator(Block):
    """Each incoming signal is replicated x times, where x
    is the length of list. Each output signal with have a
    new attribute, title, with the value of the list.

    """
    title = StringProperty(title='Attribute Title')
    list = ExpressionProperty(title='List')

    def process_signals(self, signals):
        return_signals = []
        for signal in signals:
            try:
                values = self.list(signal)
            except Exception as e:
                values = [None]
            values = [None] if not values else values
            for value in values:
                sig = Signal(signal.to_dict())
                setattr(sig, self.title, value)
                return_signals.append(sig)
        if return_signals:
            self.notify_signals(return_signals)
