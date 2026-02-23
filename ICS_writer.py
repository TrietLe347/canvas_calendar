from datetime import datetime, timedelta
from uuid import uuid4
from pathlib import Path
from event import Event

def event_to_ics(event):

    uid = str(uuid4())

    due = event.get_due_date()
    if not due:
        return None

    dt_start = datetime.fromisoformat(due.replace("Z", "+00:00"))
    dt_end = dt_start + timedelta(minutes=15)

    dt_start_str = dt_start.strftime("%Y%m%dT%H%M%SZ")
    dt_end_str = dt_end.strftime("%Y%m%dT%H%M%SZ")

    
    summary = f"{event.get_title()} ({event.get_course()})"

    description = f"""{event.get_course()}

{event.get_desc()}

Link: {event.get_url()}
"""
    
    description = description.replace("\n","\\n")

    ics = f"""BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Canvas Sync//EN
BEGIN:VEVENT
UID:{uid}
DTSTAMP:{dt_start_str}
DTSTART:{dt_start_str}
DTEND:{dt_end_str}
SUMMARY:{summary}
DESCRIPTION:{description}
BEGIN:VALARM
TRIGGER:-PT24H
ACTION:DISPLAY
DESCRIPTION:Assignment due tomorrow
END:VALARM
END:VEVENT
END:VCALENDAR
    """
    return ics

def write_ics(event,output_dir):

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True,exist_ok=True)

    filename = f"{event.get_course()}_{event.get_title()}".replace(" ", "_")
    filename = filename.replace("/", "_")

    path = output_dir / f"{filename}.ics"

    ics_content = event_to_ics(event)
    if not ics_content:
        return None

    path.write_text(ics_content,encoding="utf-8")
    return path