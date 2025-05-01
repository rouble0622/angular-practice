from datetime import datetime, timedelta
import pytz

def get_current_time(timezone='UTC'):
    """Get current time in specified timezone."""
    tz = pytz.timezone(timezone)
    return datetime.now(tz)

def format_datetime(dt, format='%Y-%m-%d %H:%M:%S'):
    """Format datetime object to string."""
    if isinstance(dt, str):
        dt = datetime.fromisoformat(dt)
    return dt.strftime(format)

def parse_datetime(dt_str, format='%Y-%m-%d %H:%M:%S'):
    """Parse datetime string to datetime object."""
    return datetime.strptime(dt_str, format)

def add_time_delta(dt, days=0, hours=0, minutes=0, seconds=0):
    """Add time delta to datetime object."""
    if isinstance(dt, str):
        dt = datetime.fromisoformat(dt)
    return dt + timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds) 