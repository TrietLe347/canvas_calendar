from datetime import datetime, timedelta
from uuid import uuid4


def events_to_ics(events):
    """
    Convert a list of Event objects into ONE ICS calendar feed
    """

    lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//Minh Triet Le//Canvas Calendar Sync//EN"
    ]

    for event in events:
        due = event.get_due_date()
        if not due:
            continue

        dt_start = datetime.fromisoformat(due.replace("Z", "+00:00"))
        dt_end = dt_start + timedelta(minutes=15)

        dt_start_str = dt_start.strftime("%Y%m%dT%H%M%SZ")
        dt_end_str = dt_end.strftime("%Y%m%dT%H%M%SZ")

        description = f"""{event.get_course()}

{event.get_desc()}

Link: {event.get_url()}
"""
        description = description.replace("\n", "\\n")

        lines.extend([
            "BEGIN:VEVENT",
            f"UID:{event.uid}@csusm.instructure.com",
            f"DTSTAMP:{dt_start_str}",
            f"DTSTART:{dt_start_str}",
            f"DTEND:{dt_end_str}",
            f"SUMMARY:{event.get_title()} ({event.get_course()})",
            f"DESCRIPTION:{description}",
            "BEGIN:VALARM",
            "TRIGGER:-PT24H",
            "ACTION:DISPLAY",
            "DESCRIPTION:Assignment due tomorrow",
            "END:VALARM",
            "END:VEVENT",
        ])

    lines.append("END:VCALENDAR")
    return "\n".join(lines)