from datetime import datetime, date, timedelta, timezone

# The timezone class is a subclass of tzinfo, each instance of which represents a timezone defined by a fixed offset from UTC.

import time

if __name__ == '__main__':

    # https://docs.python.org/3.8/library/datetime.html?#module-datetime

    test_dt = datetime(2020, 3, 13, hour = 23, minute = 30)
    print(test_dt)
    print('=====')

    test_date = date(2009, 3, 6)
    print(test_date)
    print('weekday', test_date.weekday())
    print(test_date.ctime())
    print('=====')

    the_start_date = datetime.fromisoformat('2011-11-04T00:05:23')
    print('the_start_date', the_start_date)
    print('the_start_date in isoformat', the_start_date.isoformat())

    date_from_ts = date.fromtimestamp(228282)
    print('===', date_from_ts)

    now = datetime.now()
    print('now YYYY MM DD', now, now.year, now.month, now.day)
    print(now.strftime('Using strftime: %A, %Y-%m-%d'))

    one_year = timedelta(days=365)
    day_next_year = now + one_year
    print('same day next year', day_next_year)

    # try:
    #     two_days_ago = timedelta(days=a)
    # except NameError:
    #     print('days should be a valid value')

    two_days_ago = timedelta(days=-2)
    two_days_later = timedelta(days=2)

    one_day_in_seconds = timedelta(days=1).total_seconds()
    print('one_day_in_seconds', one_day_in_seconds)

    one_hour_in_seconds = timedelta(hours=1).total_seconds()
    print('one_hour_in_seconds', one_hour_in_seconds)

    year = timedelta(days=365)
    ten_years = 10 * year
    print('ten_years', ten_years)

    today_from_date = date.today()
    print('today_from_date', today_from_date)
    now = time.time()
    print('now', now)
    today_from_time = date.fromtimestamp(now)
    print('today_from_time', today_from_time)
    print(today_from_date == today_from_time)

    # get an aware datetime object
    aware_dt_from_timestamp = datetime.fromtimestamp(now, timezone.utc)
    print('aware_dt_from_timestamp', aware_dt_from_timestamp)

    target_date = date(2022, 12, 25)
    delta_to_target = abs(target_date - today_from_date)
    print('days to target date', delta_to_target)

    # these two are equivalent
    print(datetime.today())
    print(datetime.fromtimestamp(time.time()))

    # https://docs.python.org/3.8/library/datetime.html?#strftime-strptime-behavior
    # strptime is a method of datetime
    # strftime is a method of date, datetime and time

    # Parse a string representing a datetime according to a format.
    dt_string = "Sep 27, 2022, 11:45 +0400"
    dt_from_string = datetime.strptime(dt_string, "%b %d, %Y, %H:%M %z")
    print("dt_string to datetime", dt_string, dt_from_string, dt_from_string.day, dt_from_string.tzinfo)

    some_dt = datetime(2022, 10, 30, 11, 45, 0)
    print(some_dt)

    # Because naive datetime objects are treated by many datetime methods as local times, it is preferred to use aware datetimes to represent times in UTC. As such, the recommended way to create an object representing the current time in UTC is by calling datetime.now(timezone.utc).
    aware_current_dt_in_utc = datetime.now(timezone.utc)
    print(aware_current_dt_in_utc)




