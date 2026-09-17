---
CLASSIFICATION: MIDSHIPMAN EYES ONLY
MISSION: 0 — REPORTING FOR DUTY
THEATRE: Starfall Defence Corps Academy
AUTHORITY: SDC Cyber Command, 2187
---

# OPERATION ORDER — MISSION 0: REPORTING FOR DUTY

> [🏠 Mission README](../README.md) · [🧭 Exercises](EXERCISES.md) · [💡 Hints](HINTS.md)

---

## 1. SITUATION

### 1a. Enemy Forces

None — yet. The Voidborn do not attack recruits at the gate. They attack cadets in the field with broken toolchains, dead Docker daemons, and ports already in use. This mission exists to make sure that never happens to you.

### 1b. Friendly Forces

The **Starfall Defence Corps (SDC)** Academy gatehouse — a single node, `sdc-gate`, standing between you and enrolment. It is expecting your arrival.

### 1c. Attachments / Support

**ARIA** (Automated Review & Intelligence Analyst) is assigned to this mission. ARIA will verify your work and report compliance status. Every mission from here on ends the same way: ARIA says green, or you are not done.

### 1d. Operational Tool

All operations will be conducted using **ANSIBLE** — *Automated Network for Secure Infrastructure, Baseline Lockdown & Enforcement*. You do not need to know it yet. Today you only need to prove it runs on your machine.

---

## 2. MISSION

Report for duty. Verify your equipment (`make doctor`), boot the gatehouse node (`make setup`), establish communications with it (one ping), and file your duty report (one command). Obtain your first green banner from ARIA.

**End state**: Your machine is proven mission-ready. Your duty report is on file. You hold the rank of Midshipman.

---

## 3. EXECUTION

### 3a. Commander's Intent

Every environment problem you will ever have — Docker not running, a busy port, a missing tool — should surface **now**, on a 15-minute mission with nothing at stake, not later inside a real operation. When this mission is green, your machine is cleared for the entire Foundation module.

### 3b. Concept of Operations

Two short phases after boot. Full procedural detail is in **[EXERCISES.md](EXERCISES.md)**.

| Phase | Task | Objective |
|-------|------|-----------|
| 1 | Comms Check | Ping the gatehouse node with ANSIBLE; confirm SUCCESS |
| 2 | Report In | File your duty report on the node with a single ad-hoc command |

### 3c. Fleet Assets

| Designation | Role | IP Address | SSH Port |
|-------------|------|------------|----------|
| `sdc-gate` | Academy Gatehouse | localhost | 2221 |

**SSH User**: `cadet`
**Authentication**: SSH key located at `workspace/.ssh/cadet_key`

The inventory file is **provided** at `workspace/inventory/hosts.yml`. You will build your own in [Mission 1.1](https://github.com/starfall-defence-corps/mission-1-1-fleet-census) — today it is issued equipment.

### 3d. Rules of Engagement

- Every command you need is written out in [EXERCISES.md](EXERCISES.md). Copy them exactly.
- If ARIA cannot verify your work, your work is not complete.
- `make doctor` is authorised — and encouraged — at any time.

---

## 4. SUPPORT

| Resource | Function | Command |
|----------|----------|---------|
| **Doctor** | Diagnoses your machine; reports what to fix | `make doctor` |
| **ARIA** | Verifies mission compliance; reports pass/fail per phase | `make test` |
| **HINTS.md** | Operational guidance if mission stalls | — |
| **Gate Reset** | Rebuilds the gatehouse container from scratch | `make reset` |

Consulting **HINTS.md** is authorised at Midshipman rank. Using available intelligence is not weakness — it is doctrine.

---

## 5. COMMAND AND SIGNAL

**Reporting**: ARIA is your automated reporting chain. Her output is your after-action record.

**Commander's Final Order**: No cadet enters the fleet with an unproven machine. Report in, get your green banner, and proceed to Mission 1.1.

Proceed to **[EXERCISES.md](EXERCISES.md)** for phase-by-phase operational instructions.

---

*SDC Cyber Command — 2187 — MIDSHIPMAN EYES ONLY*
