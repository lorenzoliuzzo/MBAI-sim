from typing import List, Optional
from dataclasses import dataclass
from datetime import datetime, timedelta

from .timing import TimeWindow, ClockWindow
from .stints import PlayerStint, LineUpStint, CourtContext
from .actions import Action, Possession


@dataclass 
class Score():
    home: int
    away: int

    @property
    def margin(self) -> int: 
        return self.home - self.away


@dataclass(kw_only=True)
class GameState(TimeWindow, ClockWindow):
    court: CourtContext
    game_score: Score
    period_score: Score
    possessions: List[Possession]


@dataclass(kw_only=True)
class Period(TimeWindow):
    n: int
    history: List[GameState]

    @property
    def game_clock_offset(self) -> int:         
        return 300 if self.n > 4 else 720
        

@dataclass(kw_only=True)
class Game(TimeWindow): 
    home_id: int
    away_id: int
    periods: List[Period]