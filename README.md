# Canvas Calendar Sync

Automatically sync Canvas assignments into your local calendar on Ubuntu.

## Why I Built This

This project started as a way for me to get comfortable using **Ubuntu Linux as my daily development environment**. I wanted to:

- Set up my full developer workflow on Linux (Python, virtual environments, Visual Studio Code, cron, system tools)
- Build something practical instead of a throwaway demo
- Reduce friction in my daily student workflow

I use Canvas for school, but I found myself constantly logging in just to check upcoming assignments. I wanted all my deadlines to live in **my own calendar**, alongside everything else in my life.

So I built a tool that:
- Pulls assignments from Canvas
- Cleans and formats the data
- Syncs everything into my system calendar automatically

Once it’s set up, I never have to open Canvas just to check due dates.

---

## What This Project Does

- Fetches upcoming assignments from the Canvas API
- Converts HTML assignment descriptions into clean, readable text
- Generates a single `calendar.ics` file (iCalendar feed)
- Adds reminders (24 hours before due dates)
- Automatically updates the calendar daily using `cron`
- Works with GNOME Calendar and any ICS-compatible calendar app
- Avoids duplicate events using stable Canvas assignment IDs

After initial setup, the calendar stays in sync without any manual effort.

---

## How It Works (High Level)
Canvas API --> Python Script --> Cleaned Assignment Data --> calendar.ics (single feed) --> System Calendar (subscribed once) --> Daily Updates via Cron 

The calendar file is regenerated every day and acts as the single source of truth. Calendar apps automatically refresh when the file changes.

---

## Tech Stack

- **Python 3**
- **Canvas REST API**
- **SQLite** (local state tracking)
- **iCalendar (ICS)**
- **cron** (Linux task scheduler)
- **GNOME Calendar** (local calendar integration)

---

## Setup Overview

1. Clone the repository
2. Create and activate a Python virtual environment
3. Install dependencies
4. Add your Canvas API token via `.env`
5. Run the script once to generate `calendar.ics`
6. Subscribe your calendar app to the file
7. Set up cron for daily sync

After that, everything runs automatically.

---

## Automation

This project is designed to run unattended.

Once cron is configured, assignments:
- Appear automatically in the calendar
- Update if due dates change
- Trigger reminders without manual input

No repeated imports. No duplicate events. No daily maintenance.

---

## Notes

- API tokens and local state are excluded from version control
- The project follows standard security practices (`.env`, `.gitignore`)
- The design mirrors how real calendar subscription feeds work

---

## Motivation Summary

This project helped me:
- Get comfortable developing on Ubuntu Linux
- Learn practical system automation (cron, environment variables)
- Work with real APIs and file formats
- Build a tool I actually use every day

It’s both a learning project and a productivity tool.
