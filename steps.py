
ISO_LEFT_S = [[0],[0], [20],[ 0], [45], [0], [0]]
ISO_LEFT_T = [[2],[2],[2],[2],[2],[2],[2]]
ISO_LEFT = [ISO_LEFT_S, ISO_LEFT_T]


ISO_RIGHT_S = [[0], [0], [-20], [0], [-45], [0], [0]]
ISO_RIGHT_T = [[2],[2],[2],[2],[2],[2],[2]]
ISO_RIGHT = [ISO_RIGHT_S, ISO_RIGHT_T]



KNOCK_S = [[90, 0, -90],[0, 70, 0, -100, 20],[0],[0, 60, 0, -45, 105, -60],[0],[0, 120, -70, 70, -70],[0]]
KNOCK_T = [[4, 24, 4],[4, 8, 8, 6, 6],[32],[4, 4, 8, 4, 6, 6],[32], [12, 4, 4, 6, 6],[32]]
KNOCK = [KNOCK_S, KNOCK_T]

WAVE_BACK_S = [[0],[0, 0, 0, -30, 0],[0],[30, 0, 0, 40, -40, 0],[0],[30, 0, 60, -60, 0],[0]]
WAVE_BACK_T = [[4],[2, 0.5, 0.5, 0.9, 0.1],[4],[2, 0.5, 0.25, 0.5, 0.5, 0.25],[4],[2, 0.5, 0.5, 0.5, 0.5],[4]]
WAVE_BACK = [WAVE_BACK_S, WAVE_BACK_T]

WAVE_RIGHT_S = [[-90, 0],[0, 0, 0, -30, 0],[0],[30, 0, 0, 40, -40, 0],[0],[30, 0, 60, -60, 0],[0]]
WAVE_RIGHT_T = [[2, 2],[2, 0.5, 0.5, 0.9, 0.1],[4],[2, 0.5, 0.25, 0.5, 0.5, 0.25],[4],[2, 0.5, 0.5, 0.5, 0.5],[4]]
WAVE_RIGHT = [WAVE_RIGHT_S, WAVE_RIGHT_T]

WAVE_LEFT_S = [[90, 0],[0, 0, 0, -30, 0],[0],[30, 0, 0, 40, -40, 0],[0],[30, 0, 60, -60, 0],[0]]
WAVE_LEFT_T = [[2, 2],[2, 0.5, 0.5, 0.9, 0.1],[4],[2, 0.5, 0.25, 0.5, 0.5, 0.25],[4],[2, 0.5, 0.5, 0.5, 0.5],[4]]
WAVE_LEFT = [WAVE_LEFT_S, WAVE_LEFT_T]

LEAN_BACK_S = [[0],[0, 45],[0],[30, 0],[0],[30, 0],[0]]
LEAN_BACK_T = [[6],[2, 4],[6],[2, 4],[6],[2, 4],[6]]
LEAN_BACK = [LEAN_BACK_S, LEAN_BACK_T]

DIP_S = [[90, -180],[0],[0, 15, -30],[0, -40, 40],[0],[0],[0]]
DIP_T = [[2, 6],[8],[2, 3, 3],[2, 3, 3],[8],[8],[8]]
DIP = [DIP_S, DIP_T]

HEAD_DOWN_S = [[0],[0],[0],[0],[0],[-45],[0]]
HEAD_DOWN_T = [[2],[2],[2],[2],[2],[2],[2]]
HEAD_DOWN = [HEAD_DOWN_S, HEAD_DOWN_T]

HEAD_UP_S = [[0],[0],[0],[0],[0],[45],[0]]
HEAD_UP_T = [[2],[2],[2],[2],[2],[2],[2]]
HEAD_UP = [HEAD_UP_S, HEAD_UP_T]

HEAD_TURN_RIGHT_S = [[0],[0],[0],[0],[90],[0],[0]]
HEAD_TURN_RIGHT_T = [[2],[2],[2],[2],[2],[2],[2]]
HEAD_TURN_RIGHT = [HEAD_TURN_RIGHT_S, HEAD_TURN_RIGHT_T]

HEAD_TURN_LEFT_S = [[0],[0],[0],[0],[-90],[0],[0]]
HEAD_TURN_LEFT_T = [[2],[2],[2],[2],[2],[2],[2]]
HEAD_TURN_LEFT = [HEAD_TURN_LEFT_S, HEAD_TURN_LEFT_T]

TURN_BIG_RIGHT_S = [[90],[0],[0],[0],[0],[0],[0]]
TURN_BIG_RIGHT_T = [[4],[4],[4],[4],[4],[4],[4]]
TURN_BIG_RIGHT = [TURN_BIG_RIGHT_S, TURN_BIG_RIGHT_T]


TURN_BIG_LEFT_S = [[-90],[0],[0],[0],[0],[0],[0]]
TURN_BIG_LEFT_T = [[4],[4],[4],[4],[4],[4],[4]]
TURN_BIG_LEFT = [TURN_BIG_LEFT_S, TURN_BIG_LEFT_T]


TURN_SMALL_RIGHT_S = [[0],[0],[90],[0],[0],[0],[0]]
TURN_SMALL_RIGHT_T = [[4],[4],[4],[4],[4],[4],[4]]
TURN_SMALL_RIGHT = [TURN_SMALL_RIGHT_S, TURN_SMALL_RIGHT_T]


TURN_SMALL_LEFT_S = [[0],[0],[-90],[0],[0],[0],[0]]
TURN_SMALL_LEFT_T = [[4],[4],[4],[4],[4],[4],[4]]
TURN_SMALL_LEFT = [TURN_SMALL_LEFT_S, TURN_SMALL_LEFT_T]


WAVE_DIAGONAL_LEFT_S = [[-45, 0],[0, 0, 0, -30, 0],[0],[30, 0, 0, 40, -40, 0],[0],[30, 0, 60, -60, 0],[0]]
WAVE_DIAGONAL_LEFT_T = [[2, 2],[2, 0.5, 0.5, 0.9, 0.1],[4],[2, 0.5, 0.25, 0.5, 0.5, 0.25],[4],[2, 0.5, 0.5, 0.5, 0.5],[4]]
WAVE_DIAGONAL_LEFT = [WAVE_DIAGONAL_LEFT_S, WAVE_DIAGONAL_LEFT_T]

WAVE_DIAGONAL_RIGHT_S = [[45, 0],[0, 0, 0, -30, 0],[0],[30, 0, 0, 40, -40, 0],[0],[30, 0, 60, -60, 0],[0]]
WAVE_DIAGONAL_RIGHT_T = [[2, 2],[2, 0.5, 0.5, 0.9, 0.1],[4],[2, 0.5, 0.25, 0.5, 0.5, 0.25],[4],[2, 0.5, 0.5, 0.5, 0.5],[4]]
WAVE_DIAGONAL_RIGHT = [WAVE_DIAGONAL_RIGHT_S, WAVE_DIAGONAL_RIGHT_T]

SEMI_CIRCLE_S = [[90, -180],[0],[0, 15, -30],[0, 40, -40],[0],[0],[0]]
SEMI_CIRCLE_T = [[2, 6],[8],[2, 3, 3],[2, 3, 3],[8],[8],[8]]
SEMI_CIRCLE = [SEMI_CIRCLE_S, SEMI_CIRCLE_T]

LEAN_S = [[90, -180],[0, -45],[0],[0, 30],[0],[0, 75],[0]]
LEAN_T = [[2, 6],[2, 6],[8],[2, 6],[8],[2, 6],[8]]
LEAN = [LEAN_S, LEAN_T]

CIRCLE_S = [[90, -180, 180],[0],[0, 15, -30, -15, 30],[0, 40, -40, -40, 40],[0],[0],[0]]
CIRCLE_T = [[2, 6, 6],[14],[2, 3, 3, 3, 3],[2, 3, 3, 3, 3],[14],[14],[14]]
CIRCLE = [CIRCLE_S, CIRCLE_T]

BLOOM_S = [[0],[0, -40],[0],[0, 30],[0],[-25, 8],[0]]
BLOOM_T = [[11],[1, 10],[11],[1, 10],[11],[5.5, 5.5],[11]]
BLOOM = [BLOOM_S, BLOOM_T]

dance_step_database = [ISO_LEFT, ISO_RIGHT, KNOCK, WAVE_BACK, WAVE_RIGHT, WAVE_LEFT, LEAN_BACK, DIP, HEAD_DOWN, HEAD_UP,
                      HEAD_TURN_RIGHT, HEAD_TURN_LEFT, TURN_BIG_RIGHT, TURN_BIG_LEFT, TURN_SMALL_RIGHT,
                      TURN_SMALL_LEFT, WAVE_DIAGONAL_RIGHT, WAVE_DIAGONAL_LEFT, SEMI_CIRCLE, LEAN, CIRCLE, BLOOM]
