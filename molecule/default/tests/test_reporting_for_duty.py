"""
=== STARFALL DEFENCE CORPS ACADEMY ===
ARIA Automated Verification - Mission 0: Reporting for Duty
========================================================
"""
import os
import subprocess
import pytest


def _root_dir():
    """Return the mission root directory."""
    tests_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.abspath(os.path.join(tests_dir, "..", "..", ".."))


def _workspace_dir():
    return os.path.join(_root_dir(), "workspace")


def _inventory():
    return os.path.join(_workspace_dir(), "inventory", "hosts.yml")


def _ansible(args, timeout=30):
    return subprocess.run(
        ["ansible"] + args + ["-i", _inventory()],
        capture_output=True, text=True, timeout=timeout,
        cwd=_workspace_dir(),
    )


# -------------------------------------------------------------------
# Phase 1: Comms check — the gatehouse responds
# -------------------------------------------------------------------

class TestCommsCheck:
    """ARIA verifies: Can the recruit raise the gatehouse on comms?"""

    def test_inventory_present(self):
        """The issued inventory file must still be in place"""
        assert os.path.isfile(_inventory()), (
            "ARIA: The issued inventory at workspace/inventory/hosts.yml is "
            "missing. It ships with this repo — restore it with "
            "'git checkout workspace/inventory/hosts.yml'."
        )

    def test_gate_node_responds(self):
        """sdc-gate must respond to ansible ping"""
        if not os.path.isfile(_inventory()):
            pytest.skip("Inventory file is missing")
        result = _ansible(["all", "-m", "ping"])
        assert result.returncode == 0 and "SUCCESS" in result.stdout, (
            f"ARIA: The gatehouse is not responding.\n"
            f"Output: {result.stdout}\n"
            f"Errors: {result.stderr}\n"
            f"Is the node up? Run 'make setup' from the project root, then "
            f"'ansible all -m ping' from workspace/."
        )


# -------------------------------------------------------------------
# Phase 2: Report in — duty report filed on the node
# -------------------------------------------------------------------

class TestDutyReport:
    """ARIA verifies: Has the recruit filed a duty report?"""

    def test_duty_report_filed(self):
        """Duty report file must exist on sdc-gate"""
        if not os.path.isfile(_inventory()):
            pytest.skip("Inventory file is missing")
        result = _ansible(
            ["all", "-m", "command", "-a", "cat /home/cadet/duty-report.txt"]
        )
        assert result.returncode == 0, (
            "ARIA: No duty report found at /home/cadet/duty-report.txt on the "
            "gatehouse node. File it from the repo root (or workspace/) "
            "with: ansible all -m shell -a "
            "\"echo 'Cadet reporting for duty' > /home/cadet/duty-report.txt\""
        )

    def test_duty_report_signed(self):
        """Duty report must actually report for duty"""
        if not os.path.isfile(_inventory()):
            pytest.skip("Inventory file is missing")
        result = _ansible(
            ["all", "-m", "command", "-a", "cat /home/cadet/duty-report.txt"]
        )
        if result.returncode != 0:
            pytest.skip("Duty report not filed yet")
        assert "reporting for duty" in result.stdout.lower(), (
            "ARIA: The duty report exists but does not report for duty. "
            "It must contain the phrase 'reporting for duty'. Re-file it with: "
            "ansible all -m shell -a \"echo 'Cadet reporting for duty' > "
            "/home/cadet/duty-report.txt\""
        )
