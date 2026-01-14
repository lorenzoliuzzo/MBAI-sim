from typing import List, Optional
from dataclasses import dataclass
from datetime import datetime, timedelta

from .timing import TimeWindow, ClockWindow
from .stints import LineUpStint, PlayerStint
from .actions import Action, Possession


@dataclass(kw_only=True)
class Score(TimeWindow, ClockWindow): 
    game_home: int = 0 
    game_away: int = 0

    period_home: int = 0 
    period_away: int = 0

    @property
    def game_margin(self) -> int: 
        return self.game_home - self.game_away

    @property
    def period_margin(self) -> int: 
        return self.period_home - self.period_away



@dataclass(kw_only=True)
class CourtContext(TimeWindow, ClockWindow):
    lineup_home: LineUpStint
    lineup_away: LineUpStint

    possessions: List[Possession]
    scores: List[Optional[Score]]


@dataclass(kw_only=True)
class Period(TimeWindow):
    n: int
    contexts: List[CourtContext]


class Game(TimeWindow): 
    home_id: int
    away_id: int
    periods: List[Period]

    def __init__(self, home_id, away_id, periods):
        assert len(periods) >= 4
        super().__init__(
            time_start=periods[0].time_start,
            time_end=periods[-1].time_end
        )
        self.home_id = home_id
        self.away_id = away_id
        self.periods = periods