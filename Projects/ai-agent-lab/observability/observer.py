"""Abstract observer interface."""

from abc import ABC, abstractmethod
from observability.span import Span
from observability.metrics import Metric


class Observer(ABC):
    """Abstract base class for telemetry observers."""

    @abstractmethod
    def on_span_end(self, span: Span) -> None:
        """Called when a span completes."""
        pass

    @abstractmethod
    def on_metric_record(self, metric: Metric) -> None:
        """Called when a metric is recorded."""
        pass
