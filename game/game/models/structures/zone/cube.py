from dataclasses import dataclass, field

from common.ctype import ctype
from game.models.structures.zone.farm import ZoneFarm


@dataclass(kw_only=True)
class ZoneCube(ZoneFarm):
    x1: ctype.int32
    x2: ctype.int32
    y1: ctype.int32
    y2: ctype.int32
    z1: ctype.int32
    z2: ctype.int32
