from datetime import datetime
from typing import List

class Base_charge:
    user_id: int
    base_pricing: int


class Deer:
    deer_name: str
    deer_area_id: int


class UserDTO:
    user_id : int
    use_deer: Deer
    use_end_lat: float
    use_end_lng: float

    use_start_at: datetime
    use_end_at: datetime


