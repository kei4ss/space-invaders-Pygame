from enum import Enum

class Stage(Enum):
    STAGE_1 = [
            ['x', 'x', 'y', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x'],
            ['y', 'x', 'y', 'y', 'x', 'y']
        ]
    STAGE_2 = [
            ['x', 'y', 'x', 'y', 'x', 'y', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'y', 'x', 'x', 'x'],
            ['x', 'x', 'y', 'x', 'x', 'y', 'x']
        ]
    STAGE_3 = [
            ['x', 'y', 'x', 'y', 'x', 'y', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'y'],
            ['x', 'x', 'x', 'y', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'y', 'x', 'x', 'y', 'x', 'x'],
            ['x', 'y', '', 'x', 'x', '', 'y', 'x']
        ]
    TOTAL_STAGES = 3