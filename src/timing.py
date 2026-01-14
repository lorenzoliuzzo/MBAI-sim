from typing import Optional
from dataclasses import dataclass
from datetime import datetime, timedelta


@dataclass(kw_only=True)
class TimeWindow:
    time_start: datetime
    time_end: Optional[datetime] = None

    @property 
    def time_duration(self) -> Optional[timedelta]:
        if self.time_end:
            return self.time_end - self.time_start


@dataclass(kw_only=True)
class ClockWindow:
    game_clock_start: float
    game_clock_end: Optional[float] = None

    period_clock_start: float
    period_clock_end: Optional[float] = None

    @property 
    def clock_duration(self) -> Optional[float]:
        if self.period_clock_end: 
            return self.period_clock_start - self.period_clock_end