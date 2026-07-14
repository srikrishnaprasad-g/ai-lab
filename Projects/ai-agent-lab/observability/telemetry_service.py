"""Telemetry service implementation."""

import time
from typing import Any

from observability.span import Span
from observability.metrics import Metric
from observability.observer import Observer


class TelemetryService:
    """Centralized service for managing spans and metrics."""

    def __init__(self) -> None:
        self._observers: list[Observer] = []

    def add_observer(self, observer: Observer) -> None:
        """Registers a telemetry observer."""
        self._observers.append(observer)

    def start_span(self, name: str, component: str, trace_id: str) -> Span:
        """Starts a new execution span."""
        return Span(name=name, component=component, trace_id=trace_id, start_time=time.perf_counter())

    def end_span(self, span: Span) -> None:
        """Ends a span and notifies observers."""
        span.end_time = time.perf_counter()
        for observer in self._observers:
            observer.on_span_end(span)

    def record_metric(self, category: str, name: str, value: Any, metadata: dict[str, Any]) -> None:
        """Records a metric and notifies observers."""
        metric = Metric(category=category, name=name, value=value, metadata=metadata)
        for observer in self._observers:
            observer.on_metric_record(metric)
