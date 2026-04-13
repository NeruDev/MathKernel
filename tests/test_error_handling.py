from scripts.core.error_handling import ErrorCollector, ProcessingError


def test_error_collector_registers_errors():
    collector = ErrorCollector()
    collector.add("step-a", ProcessingError("fallo"), critical=True)

    assert collector.has_errors is True
    assert collector.has_critical_errors is True
    assert any("step-a" in line for line in collector.format_summary())


def test_error_collector_registers_messages():
    collector = ErrorCollector()
    collector.add_message("step-b", "mensaje", critical=False)

    assert collector.has_errors is True
    assert collector.has_critical_errors is False
    assert any("mensaje" in line for line in collector.format_summary())
