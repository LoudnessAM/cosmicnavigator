import swisseph as swe
from datetime import datetime, timezone

# 360 degrees : 12 Zodiac_Signs = 30 degree segment
LUNAR_SIGNS = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio",
    "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]

# Calculating current moon phase, moon sign and moon illumination
def get_lunar_data():
    # utc so the calculation stays the same
    now = datetime.now(timezone.utc)

    # swisseph needs Julian Day, give [Year, Month, Day, Hour]
    julian_day = swe.julday(
        now.year, now.month, now.day, now.hour + now.minute / 60.0
    )
    # Calculating the Moon position (longitude in degrees 0-360)
    lunar_position = swe.calc_ut(julian_day, swe.MOON)[0][0]

    # Calculating the Sun position (needed for moon-phase!)
    sun_position = swe.calc_ut(julian_day, swe.SUN)[0][0]

    # Calculating Moon Phase (angle between the Sun and Moon)
    lunar_phase_angle = (lunar_position - sun_position) % 360

    # Determining the Moon phase based on the angle
    lunar_phase_name = get_lunar_phase_name(lunar_phase_angle)

    # Calculating illumination percentage (0% = New Moon, 100% = Full Moon)
    lunar_illumination = round((1 - abs(180 - lunar_phase_angle) / 180) * 100, 1)

    # Determining the Zodiac sign based on the Moon's position (
    lunar_sign_index = int(lunar_position // 30)
    lunar_sign = LUNAR_SIGNS[lunar_sign_index]

    # Determining the exact degree within the zodiac sign
    lunar_degree = round(lunar_position % 30, 2)

    return {
        "lunar_sign": lunar_sign,
        "lunar_degree": lunar_degree,
        "lunar_phase_name": lunar_phase_name,
        "lunar_phase_angle": lunar_phase_angle,
        "lunar_illumination": lunar_illumination
    }

def get_lunar_phase_name(angle):
    if angle < 45:
        return "New Moon"
    elif angle < 90:
        return "Waxing Crescent"
    elif angle < 135:
        return "First Quarter"
    elif angle < 180:
        return "Waxing Gibbous"
    elif angle < 225:
        return "Full Moon"
    elif angle < 270:
        return "Waning Gibbous"
    elif angle < 315:
        return "Last Quarter"
    else:
        return "Waning Crescent"
   