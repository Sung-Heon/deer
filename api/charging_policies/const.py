from datetime import timedelta


base_policy_const = {1: {
    "NAME"                : "건국",
    "basic_rate"               : 790,
    "per_minute_rate": 150}
}

PARKING_ZONE_DISCOUNT_RATE = 0.3

OUTSIDE_CHARGE = 1000

FORBIDDEN_DISTRICT_CHARGE = 6000

REUSE_TIMEDELTA = timedelta(minutes=30)

EXCEPTION_TIMEDELTA = timedelta(minutes=1)



