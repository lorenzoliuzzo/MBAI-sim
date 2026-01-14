from typing import List, Optional
from dataclasses import dataclass
from datetime import datetime

from .timing import TimeWindow, ClockWindow
from .stints import LineUpStint, PlayerStint


@dataclass()
class Action: 
    time: datetime
    game_clock: float 
    period_clock: float 


@dataclass(kw_only=True)
class Possession(TimeWindow, ClockWindow):
    is_home: bool
    actions: List[Action]