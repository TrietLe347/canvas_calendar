from datetime import datetime

from canvas_api import get_future_assign
from utils import html_to_text
from event import Event
from ics_feed_writer import events_to_ics
from pathlib import Path
from db import init_db, has_assignment, save_assignment

EVENTS = []

def init():
    init_db()
    assignments = get_future_assign()

    EVENTS.clear()

    for a in assignments:
        assignment_id = a.get("id")

        title = a.get("title")
        course = a.get("context_name")
        due = a.get("assignment", {}).get("due_at")
        desc = html_to_text(a.get("assignment", {}).get("description", ""))
        url = a.get("html_url") or "URL not provided"

        if not desc:
            desc = "Description not provided"

        event = Event(assignment_id,title, course, due, desc, url)

        # ALWAYS add to calendar feed
        EVENTS.append(event)

        # Update DB (new or existing)
        save_assignment(assignment_id, due)



def main():
    
    init()

    calendar_path = Path("/home/minhtriet/Dev/canvas_calendar/calendar.ics")

    events = EVENTS

    ics_content = events_to_ics(events)
    calendar_path.write_text(ics_content, encoding="utf-8")

    print(f"Updated calendar feed: {calendar_path}")

    

if __name__ == "__main__":
    main()