"""
ARIA Custom Test Reporter
Provides color-coded, phase-grouped output for mission verification.

Writes all output to stderr so check-work.sh can discard pytest's
default stdout while preserving our formatted display.
"""
import os
import pytest
import sys

# -- Phase and test name mappings -------------------------------------------

PHASES = {
    "TestCommsCheck":  ("1", "Comms Check"),
    "TestDutyReport":  ("2", "Report In"),
}

FRIENDLY = {
    "test_inventory_present":    "Issued inventory in place",
    "test_gate_node_responds":   "Gatehouse responds to ping",
    "test_duty_report_filed":    "Duty report filed on sdc-gate",
    "test_duty_report_signed":   "Duty report reports for duty",
}

# -- Reporter ---------------------------------------------------------------

# The phase-oriented summary is rendered by the shared `aria-reporter`
# pytest plugin (installed via requirements.txt); this file only declares
# the mission's phases + friendly objective names.
from aria_reporter import configure  # noqa: E402

configure(phases=PHASES, friendly=FRIENDLY, mission_id="0")
