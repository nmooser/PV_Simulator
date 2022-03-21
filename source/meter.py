import math
from datetime import datetime

class meter():
    now = datetime.now()
    today = now.replace(hour=0, minute=0, second=0, microsecond=0)
    phase1min = today.replace(hour=6)
    phase1max = phase2min = today.replace(hour=8)
    phase2max = phase3min = today.replace(hour=14)
    phase3max = phase4min = today.replace(hour=20)
    phase4max = today.replace(hour=21)
    slope1 = slope4 = x1 = x2 = x3 = y1 = y2 = y3 = 0.0

    def __init__(self):
        self.x1 = self.getSecs(self.phase2min)
        self.y1 = 0.35
        self.x2 = self.getSecs(self.phase2max)
        self.y2 = 3.25
        self.x3 = self.getSecs(self.phase3max)
        self.y3 = 0.15
        self.slope1 = 0.35 / ((8 - 6) * 60 * 60)
        self.slope4 = -0.15 / ((21 - 20) * 60 * 60)

    def getSecs(self, dateinfo):
        return dateinfo.hour * 60 * 60 + dateinfo.minute * 60 + dateinfo.second

    def getPowerValue(self, dateInfo):
        dateinfoSecs = self.getSecs(dateInfo)
        if (dateInfo >= self.phase1min and dateInfo <= self.phase1max):
            return self.slope1 * (dateinfoSecs - self.getSecs(self.phase1min))
        if (dateInfo >= self.phase2min and dateInfo <= self.phase2max):
            return self.fitSinCurve(self.x1, self.y1, self.x2, self.y2, dateinfoSecs)
        if (dateInfo >= self.phase3min and dateInfo <= self.phase3max):
            return self.fitSinCurve(self.x2, self.y2, self.x3, self.y3, dateinfoSecs)
        if (dateInfo >= self.phase4min and dateInfo <= self.phase4max):
            return self.slope4 * (dateinfoSecs - self.getSecs(self.phase4min)) + 0.15
        return 0.0

    def fitSinCurve(self, x1, y1, x2, y2, x):
        a = (y1 - y2) / 2
        b = math.pi / (x2 - x1)
        c = math.pi * x2 / (x1 - x2) - math.pi / 2
        d = (y1 + y2) / 2
        return a * math.sin(b * x + c) + d
