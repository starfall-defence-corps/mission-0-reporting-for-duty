---
CLASSIFICATION: MIDSHIPMAN EYES ONLY
MISSION: 0 — REPORTING FOR DUTY
DOCUMENT: EXERCISES — Phase-by-Phase Operational Instructions
---

# EXERCISES — MISSION 0: REPORTING FOR DUTY

Complete each phase in sequence. Run `make test` after each phase. Every command you need is written out below — copy it exactly.

**One directory for everything**: run every command in this mission — `ansible ...` and `make ...` — from the **project root** (the folder with the `Makefile`). An `ansible.cfg` lives both there and in `workspace/`, so Ansible works from either; the steps below assume the project root throughout.

---

## PHASE 0: Arrival

> The gatehouse is expecting you. Boot it and confirm your equipment works.

### Step 0.1 — Check Your Machine

From the **project root directory**, run:

```bash
make doctor
```

Doctor checks Docker, required tools, and that port 2221 is free. If anything is red, fix it (doctor tells you how) and run it again. Do not proceed with red checks.

### Step 0.2 — Boot the Gatehouse

```bash
make setup
```

This builds one Docker container, generates SSH credentials, and starts the gatehouse node. Wait for:

```
  Gatehouse Status: sdc-gate ONLINE
```

### Step 0.3 — Activate the Python Environment

`make setup` creates a Python virtual environment with the testing tools. **Activate it** before continuing:

```bash
source venv/bin/activate
```

Your terminal prompt will show `(venv)` when active. You need to do this once per terminal session. If you open a new terminal, activate again.

### Step 0.4 — If Things Go Wrong

```bash
make reset
```

This destroys the container and rebuilds it from scratch at any time.

---

## PHASE 1: Comms Check

> A cadet who cannot raise the gatehouse on comms is still a recruit. Establish contact.

### Step 1.1 — Confirm You Are in the Project Root

```bash
ls Makefile
```

If that lists the `Makefile`, you are in the right place — every command from here on runs from this directory.

### Step 1.2 — Ping the Gatehouse

```bash
ansible all -m ping
```

**Command breakdown:**

| Part | Meaning |
|------|---------|
| `ansible` | The Ansible ad-hoc command tool |
| `all` | Target all hosts in the inventory (here: just `sdc-gate`) |
| `-m ping` | Use the `ping` module — connect over SSH, run Python, report back |

**What success looks like:**

```
sdc-gate | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
```

This is not an ICMP ping — it proves SSH connectivity, authentication, and remote execution all work. That is everything a real mission needs.

If you see `UNREACHABLE`, see [HINTS.md](HINTS.md) — the fix is almost always `make setup` or a busy port.

### Step 1.3 — Run ARIA's Verification

```bash
make test
```

Phase 1 should show green. Phase 2 will still be red — that is next.

---

## PHASE 2: Report In

> Contact established. Now make it official: file your duty report on the gatehouse node.

### Step 2.1 — File Your Duty Report

One ad-hoc command, run from the project root:

```bash
ansible all -m shell -a "echo 'Cadet reporting for duty' > /home/cadet/duty-report.txt"
```

**Command breakdown:**

| Part | Meaning |
|------|---------|
| `-m shell` | Use the `shell` module — run a shell command on the remote node |
| `-a "..."` | The command to run |
| `echo ... > ...` | Write your report into a file **on the gatehouse node**, not your machine |

**What success looks like:**

```
sdc-gate | CHANGED | rc=0 >>
```

`CHANGED` means the command ran on the remote node. You just used Ansible to change the state of a machine you have never SSH'd into by hand. That is the whole job, in miniature.

### Step 2.2 — Optional: See It With Your Own Eyes

```bash
ansible all -m shell -a "cat /home/cadet/duty-report.txt"
```

Or SSH in like a tourist: `make ssh-gate`, then `cat duty-report.txt` and `exit`. Password: `academy`.

### Step 2.3 — Final ARIA Verification

```bash
make test
```

All phases green — that is your first green banner. Screenshot-worthy.

---

## SUBMIT

From the project root:

```bash
make submit
```

This branches, commits, pushes, and opens your review pull request in one command. If you added an `ANTHROPIC_API_KEY` secret (see README), ARIA posts a review on the PR. Adding the key later? Re-run the workflow from the Actions tab — secrets alone don't trigger a re-run.

---

## MISSION COMPLETE — DEBRIEF CHECKLIST

- [ ] `make doctor` — all checks green
- [ ] `sdc-gate` responds to `ansible all -m ping` with `SUCCESS`
- [ ] Duty report filed at `/home/cadet/duty-report.txt` on the gatehouse node
- [ ] `make test` — all ARIA checks pass
- [ ] `make submit` — pull request opened

Your machine is cleared for the Foundation module. Proceed to [Mission 1.1 — Fleet Census](https://github.com/starfall-defence-corps/mission-1-1-fleet-census).

---

*SDC Cyber Command — 2187 — MIDSHIPMAN EYES ONLY*
