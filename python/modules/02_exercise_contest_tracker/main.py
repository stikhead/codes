from contest_tracker import fetch_upcoming, format_times

contests = fetch_upcoming()
format_times(contests)