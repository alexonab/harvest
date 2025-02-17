# Builtin Imports
import re
import sys
import time
import random
import logging
import datetime as dt
from datetime import timezone as tz
from enum import IntEnum, auto
from zoneinfo import ZoneInfo

# External Imports
import pytz
import tzlocal
import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s : %(name)s : %(levelname)s : %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
    handlers=[logging.FileHandler("harvest.log"), logging.StreamHandler(sys.stdout)],
)
debugger = logging.getLogger("harvest")


class Interval(IntEnum):
    SEC_15 = auto()
    MIN_1 = auto()
    MIN_5 = auto()
    MIN_15 = auto()
    MIN_30 = auto()
    HR_1 = auto()
    DAY_1 = auto()


def interval_string_to_enum(str_interval: str):
    if str_interval == "15SEC":
        return Interval.SEC_15
    elif str_interval == "1MIN":
        return Interval.MIN_1
    elif str_interval == "5MIN":
        return Interval.MIN_5
    elif str_interval == "15MIN":
        return Interval.MIN_15
    elif str_interval == "30MIN":
        return Interval.MIN_30
    elif str_interval == "1HR":
        return Interval.HR_1
    elif str_interval == "1DAY":
        return Interval.DAY_1
    else:
        raise ValueError(f"Invalid interval string {str_interval}")


def interval_enum_to_string(enum):
    try:
        name = enum.name
        unit, val = name.split("_")
        return val + unit
    except:
        return str(enum)


def is_freq(time, interval):
    """Helper function to determine if algorithm should be invoked for the
    current timestamp. For example, if interval is 30MIN,
    algorithm should be called when minutes are 0 and 30.
    """
    time = time.astimezone(pytz.timezone("UTC"))

    if interval == Interval.MIN_1:
        return True

    minutes = time.minute
    hours = time.hour
    if interval == Interval.DAY_1:
        # TODO: Use API to get real-time market hours
        return minutes == 50 and hours == 19
    elif interval == Interval.HR_1:
        return minutes == 0
    val, _ = expand_interval(interval)

    return minutes % val == 0


def expand_interval(interval: Interval):
    string = interval.name
    unit, value = string.split("_")
    return int(value), unit


def expand_string_interval(interval: str):
    """
    Given a string interval, returns the unit of time and the number of units.
    For example, "3DAY" should return (3, "DAY")
    """
    num = [c for c in interval if c.isdigit()]
    value = int("".join(num))
    unit = interval[len(num) :]
    return value, unit


def interval_to_timedelta(interval: Interval) -> dt.timedelta:
    expanded_units = {"DAY": "days", "HR": "hours", "MIN": "minutes"}
    value, unit = expand_interval(interval)
    params = {expanded_units[unit]: value}
    return dt.timedelta(**params)


def is_crypto(symbol: str) -> bool:
    return symbol[0] == "@"


def normalize_pandas_dt_index(df: pd.DataFrame) -> pd.Index:
    return df.index.floor("min")


def aggregate_df(df, interval: Interval) -> pd.DataFrame:
    sym = df.columns[0][0]
    df = df[sym]
    op_dict = {
        "open": "first",
        "high": "max",
        "low": "min",
        "close": "last",
        "volume": "sum",
    }
    val, unit = expand_interval(interval)
    val = str(val)
    if unit == "1HR":
        val = "H"
    elif unit == "MIN":
        val += "T"
    else:
        val = "D"
    df = df.resample(val).agg(op_dict)
    df.columns = pd.MultiIndex.from_product([[sym], df.columns])

    return df.dropna()


def now() -> dt.datetime:
    """
    Returns the current time precise to the minute in the UTC timezone
    """
    return dt.datetime.now(tz.utc).replace(microsecond=0, second=0)


def epoch_zero() -> dt.datetime:
    """
    Returns a datetime object corresponding to midnight 1/1/1970 UTC
    """
    return dt.datetime(1970, 1, 1, tzinfo=tz.utc)


def date_to_str(day) -> str:
    return day.strftime("%Y-%m-%d")


def str_to_date(day) -> str:
    return dt.datetime.strptime(day, "%Y-%m-%d")


def str_to_datetime(date: str) -> dt.datetime:
    """
    :date: A string in the format YYYY-MM-DD hh:mm
    """
    if len(date) <= 10:
        return dt.datetime.strptime(date, "%Y-%m-%d")
    return dt.datetime.strptime(date, "%Y-%m-%d %H:%M")


def mark_up(x):
    return round(x * 1.05, 2)


def mark_down(x):
    return round(x * 0.95, 2)


def has_timezone(date: dt.datetime) -> bool:
    return date.tzinfo is not None and date.tzinfo.utcoffset(date) is not None


# def set_system_timezone(date: dt.datetime) -> dt.datetime:
#     """
#     :date: A python datetime object that does not have tzinfo set.
#     If tzinfo is set, an error will occur. Converts first to the
#     timezone of the user's system and then to UTC.
#     """
#     timezone = pytz.timezone(str(tzlocal.get_localzone()))
#     return timezone.localize(date).astimezone(pytz.utc)


class Timestamp:
    def __init__(self, *args) -> None:
        if len(args) == 1:
            timestamp = args[1]
            if isinstance(timestamp, str):
                self.timestamp = str_to_datetime(timestamp)
            elif isinstance(timestamp, dt.datetime):
                self.timestamp = timestamp
            else:
                raise ValueError(f"Invalid timestamp type {type(timestamp)}")
        elif len(args) > 1:
            self.timestamp = dt.datetime(*args)

    def __sub__(self, other):
        return Timerange(self.timestamp - other.timestamp)


class Timerange:
    def __init__(self, *args) -> None:
        if len(args) == 1:
            timerange = args[1]
            if isinstance(timerange, dt.timedelta):
                self.timerange = timerange
            else:
                raise ValueError(f"Invalid timestamp type {type(timerange)}")
        elif len(args) > 1:
            range_list = ["days", "hours", "minutes"]
            dict = {range_list[i]: arg for i, arg in enumerate(args)}
            self.timerange = dt.timedelta(**dict)


def convert_input_to_datetime(datetime, timezone: ZoneInfo):

    if datetime is None:
        return None
    elif isinstance(datetime, Timestamp):
        datetime = tz.localize(datetime.timestamp)
    elif isinstance(datetime, str):
        datetime = str_to_datetime(datetime)
    elif isinstance(datetime, dt.datetime):
        datetime = datetime.replace(tzinfo=timezone)
    else:
        raise ValueError(f"Cannot convert {datetime} to datetime.")

    datetime = datetime.replace(tzinfo=timezone)
    datetime = datetime.astimezone(tz.utc)


def convert_input_to_timedelta(period):
    """Converts period into a timedelta object.
    Period can be a string, timedelta object, or a Timerange object."""
    if period is None:
        return None
    elif isinstance(period, Timerange):
        return period.timerange
    elif isinstance(period, str):
        expanded_units = {"DAY": "days", "HR": "hours", "MIN": "minutes"}
        val, unit = expand_string_interval(period)
        return dt.timedelta(**{expanded_units[unit]: val})
    elif isinstance(period, dt.timedelta):
        return period
    else:
        raise ValueError(f"Cannot convert {period} to timedelta.")


def pandas_timestamp_to_local(df: pd.DataFrame, timezone: ZoneInfo) -> pd.DataFrame:
    """
    Converts the timestamp of a dataframe to local time, represented as a
    timezone naive datetime object.
    """
    df.index = df.index.map(lambda x: datetime_utc_to_local(x, timezone))
    return df


def datetime_utc_to_local(datetime: dt.datetime, timezone: ZoneInfo) -> dt.datetime:
    """
    Converts a datetime object in UTC to local time, represented as a
    timezone naive datetime object.
    """
    return datetime.astimezone(timezone).replace(tzinfo=None)


############ Functions used for testing #################


def gen_data(symbol: str, points: int = 50) -> pd.DataFrame:
    n = now()
    index = [n - dt.timedelta(minutes=1) * i for i in range(points)][::-1]
    df = pd.DataFrame(index=index, columns=["low", "high", "close", "open", "volume"])
    df.index.rename("timestamp", inplace=True)
    df["low"] = [random.random() for _ in range(points)]
    df["high"] = [random.random() for _ in range(points)]
    df["close"] = [random.random() for _ in range(points)]
    df["open"] = [random.random() for _ in range(points)]
    df["volume"] = [random.random() for _ in range(points)]
    # df.index = normalize_pandas_dt_index(df)
    df.columns = pd.MultiIndex.from_product([[symbol], df.columns])

    return df


def not_gh_action(func):
    def wrapper(*args, **kwargs):
        if "GITHUB_ACTIONS" in os.environ:
            return
        func(*args, **kwargs)
        return wrapper
