import os

KM_PER_MILE = 1.60934
METERS_PER_MILE = 1609.34
FEET_PER_METER = 3.28084


def is_imperial():
    """Check if the unit system is set to imperial."""
    return os.getenv("UNIT_SYSTEM", "metric").lower() == "imperial"


def meters_to_distance(meters):
    """Convert meters to km (metric) or miles (imperial)."""
    if is_imperial():
        return meters / METERS_PER_MILE
    return meters / 1000


def distance_label():
    """Return the distance unit label (km or mi)."""
    return "mi" if is_imperial() else "km"


def pace_label():
    """Return the pace unit label (/km or /mi)."""
    return "/mi" if is_imperial() else "/km"


def pace_distance_meters():
    """Return the distance in meters for one pace unit (1 km or 1 mile)."""
    return METERS_PER_MILE if is_imperial() else 1000


def elevation_convert(meters):
    """Convert elevation meters to feet (imperial) or keep as meters (metric)."""
    if is_imperial():
        return int(meters * FEET_PER_METER)
    return int(meters)


def elevation_label():
    """Return the elevation unit label (m or ft)."""
    return "ft" if is_imperial() else "m"
