import calendar
import datetime

def dt2ts():
    """Converts a datetime object to UTC timestamp

    naive datetime will be considered UTC.

    """

    return calendar.timegm(datetime.utctimetuple())

print(dt2ts())