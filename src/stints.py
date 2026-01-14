from typing import List
from dataclasses import dataclass

from .timing import TimeWindow, ClockWindow


@dataclass(kw_only=True)
class PlayerStint(TimeWindow, ClockWindow): 
    player_id: int


@dataclass(kw_only=True)
class LineUpStint(TimeWindow, ClockWindow): 
    lineup_id: int
    players: List[PlayerStint]