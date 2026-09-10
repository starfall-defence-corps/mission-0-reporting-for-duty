# Starfall Defence Corps Academy

> 🧭 🏁 Start here · **You are here: 0 Reporting for Duty** · [1.1 Fleet Census →](https://github.com/starfall-defence-corps/mission-1-1-fleet-census) · [🏠 Academy Hub](https://github.com/starfall-defence-corps/sdc-academy) · [📚 Field Manuals](https://github.com/starfall-defence-corps/sdc-academy/tree/main/field-manuals)

> ☁️ **No Docker on your machine?** Create your own copy first (Use this template), then on **your** repo: **Code → Codespaces → Create codespace** — everything is preinstalled. First boot takes ~5 min (one-time); after that it starts fast.

## Mission 0: Reporting for Duty

> *"Before you can defend the fleet, the fleet needs to know you exist."*

Welcome to the Academy, Cadet. This is not a real mission — it is your **arrival at the gate**. In about 15 minutes you will boot a one-node lab, make radio contact with it using Ansible, file your duty report, and get your first green banner from ARIA. If anything on your machine is going to cause trouble later, we find out **here** — not halfway through a real mission.

No Ansible knowledge needed. Every command is given to you. Type, run, done.

## Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (with Docker Compose v2)
- [GNU Make](https://www.gnu.org/software/make/)
- [Ansible](https://docs.ansible.com/ansible/latest/installation_guide/) (`ansible-core`)
- Python 3.10+ (for test environment)
  - On Debian/Ubuntu: `sudo apt install python3-venv`
- Git
- [GitHub CLI](https://cli.github.com/) (`gh`) — needed for `make submit`; run `gh auth login` once after installing

> **Windows users**: This mission requires a Linux environment. Install [WSL2](https://learn.microsoft.com/en-us/windows/wsl/install) and run all commands from within your WSL terminal. Docker Desktop should be configured to use the WSL2 backend.

## Quick Start

```bash
# 1. Use this template on GitHub (green button, top right)
#    This creates YOUR OWN copy of the repo.
#    Set it to Public, then clone it:
git clone https://github.com/YOUR-USERNAME/mission-0-reporting-for-duty.git
cd mission-0-reporting-for-duty

# 2. Check your machine is mission-ready
make doctor

# 3. Boot the gatehouse node
make setup

# 4. Activate the Python environment
source venv/bin/activate
```

5. **Read your orders**: [Mission Briefing](docs/BRIEFING.md)
6. **Complete the exercises**: [Exercises](docs/EXERCISES.md)
7. **Stuck?** [Hints & Troubleshooting](docs/HINTS.md)
8. **Track progress**: [Checklist](CHECKLIST.md)

## Lab Architecture

```
 Your Machine
+------------------------------------------+
|  workspace/                              |
|    ansible.cfg                           |
|    inventory/hosts.yml  (provided)       |
|    .ssh/cadet_key       (auto-generated) |
|                                          |
|  Docker Network: 172.30.0.0/24           |
|  +--------------+                        |
|  | sdc-gate     |                        |
|  | :2221        |                        |
|  | Ubuntu 22.04 |                        |
|  | systemd      |                        |
|  +--------------+                        |
+------------------------------------------+
```

## Available Commands

```
make help       Show available commands
make doctor     Check your machine is mission-ready (Docker, ports, tools)
make setup      Boot the gatehouse node
make test       Ask ARIA to verify your work
make submit     Submit your work for ARIA review (branch, commit, push, PR)
make reset      Destroy and rebuild the gatehouse node
make destroy    Tear down everything (containers, keys, venv)
make ssh-gate   SSH into sdc-gate (the gatehouse node)
```

## Mission Files

| File | Purpose |
|------|---------|
| [BRIEFING.md](docs/BRIEFING.md) | Mission briefing — **read this first** |
| [EXERCISES.md](docs/EXERCISES.md) | Step-by-step exercises (2 phases) |
| [HINTS.md](docs/HINTS.md) | Troubleshooting and hints |
| [CHECKLIST.md](CHECKLIST.md) | Progress tracker |

## ARIA Review (Pull Request Workflow)

**ARIA** (Automated Review & Intelligence Analyst) reviews your work in two ways:

**Locally** — run `make test` for instant pass/fail verification. No API key needed.

**On Pull Request** — push your work to a branch, open a PR to `main`, and ARIA reads your files and posts a qualitative review as a PR comment (structure, security, recommendations).

To enable PR reviews, add an API key to your repo:
1. Get a key from [platform.claude.com](https://platform.claude.com/)
2. In your repo: **Settings** > **Secrets and variables** > **Actions** > **New repository secret**
3. Name: `ANTHROPIC_API_KEY`, Value: your key

If no key is configured, ARIA skips the PR review — `make test` still works locally.

## Troubleshooting

**Anything failing?** Run `make doctor` first — it diagnoses the usual suspects (Docker not running, busy ports, missing tools) and tells you exactly what to fix.

**Container won't start**: Ensure Docker Desktop is running. Check for a port conflict on 2221.

**SSH connection refused**: Run `make setup` to ensure the container is running and SSH is ready.

**`make test` fails with "No module named pytest"**: Run `make setup` first — it creates the Python virtual environment automatically.

**Need a clean slate**: Run `make reset` to destroy and rebuild everything.

**Docker network conflict**: If you see "Pool overlaps with other one on this address space", another Docker network is using the 172.30.0.0/24 subnet. Stop conflicting containers or edit `.docker/docker-compose.yml` to use a different subnet.
