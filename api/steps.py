
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

TURN_LEFT_S = [0,0,-90,0,0,0,0]
TURN_LEFT_T = [3,3,3,3,3,3,3]
TURN_LEFT = [TURN_LEFT_S, TURN_LEFT_T]

FOLD_BACK_S = [[0, 90 ,0],[0 ,90, 2, 2],0,[90, 0],[0 ,-26.9, -30],[0, 30.4 ,27.2],0]
FOLD_BACK_T = [[3, 3 ,4],[3 ,3, 2 ,2],10,[3 ,7],[6 ,2 ,2],[6, 2 ,2],10]
FOLD_BACK = [FOLD_BACK_S, FOLD_BACK_T]

DANCE_STEP3_T = [[0 ,-10.6 ,-79.4],[0, -184, 46 ,44],[0 ,-83.9, 83.9],[0, -3.1, 46.1, -133],[0, 60.8, -4 ,0],[110, 6.4, -84, -90],0]
DANCE_STEP3_S = [[8, 3, 3],[4, 4 ,3 ,3],[8, 3, 3],[4, 4, 3, 3],[4, 4 ,3, 3],[4, 4, 3 ,3],14]
DANCE_STEP3 = [DANCE_STEP3_S, DANCE_STEP3_T]

DANCE_STEP4_S = [0,0,90,0,0,0,0]
DANCE_STEP4_T= [2,2,2,2,2,2,2]
DANCE_STEP4 = [DANCE_STEP4_S, DANCE_STEP4_T]

SPIN_S = [-359,0,0,-180,0,-90,0]
SPIN_T = [7,7,7,7,7,7,7]
SPIN = [SPIN_S, SPIN_T]


TWIST_S = [0,0,[30, -60, 30],0,0,0,0]
TWIST_T = [6,6,[1.5, 3, 1.5],6,6,6,6]
TWIST = [TWIST_S, TWIST_T]

BOB_S = [0,[30, -30],0,[-35, 35],0,[40 ,-40],0]
BOB_T = [4,[0.75 ,3.25],4,[1, 3],4,[1.25, 2.75],4]
BOB = [BOB_S, BOB_T]

NOD_S = [0,0,0,[30 ,-30],0,0,0]
NOD_T = [3,3,3,[1.5 ,1.5],3,3,3]
NOD = [NOD_S, NOD_T]

SEARCH_R_S = [[0, -90, 0, -90],[0, 90, -19, -48],[0, 2, 0],[0, 35 ,32 ,8],[180, -68, 7],[117, -20, -4],0]
SEARCH_R_T = [[.75, 4, 3, 3.25],[0.75, 4, 3 ,3.25], [4.5, 3 ,3.5], [0.5, 4 ,3 ,3.5],[4, 3, 4], [4, 3, 4], 11]
SEARCH_R = [SEARCH_R_S, SEARCH_R_T]
 
SEARCH_L_S =[[0, 85, 0, -82],[0, 38, -7 ,-20],[0, 6, -8.5, 0],[0, 48, 14, -.2],[-3.5, 92.5, 22],[72, 36, -9],0]
SEARCH_L_T = [[0.75, 4, 3, 3.25],[0.75, 4 ,3 ,3.25],[0.5, 4, 3, 3.5],[0.5, 4, 3 ,3.5],[4, 3, 4],[4, 3, 4],11]
SEARCH_L = [SEARCH_L_S, SEARCH_L_T]

SEARCH_R2_S = [[0, 57, -14, 0],[0, 57, 0, -26, 0],0,[0, -5, 0, 5],[-21, 7, 0],[-1, -7, -80, 80, -80, 80],0]
SEARCH_R2_T = [[0.75, 3, 2, 3.25],[0.75, 3, 2 ,2, 1.25],9,[3.5, 2, 2, 1.5],[3, 2, 4],[3, 2, 1, 1, 1 ,1],9]
SEARCH_R2 = [SEARCH_R2_S, SEARCH_R2_T]

PRETURN_S = [0,30,0,-30,0,0,0]
PRETURN_T = [2,2,2,2,2,2,2]
PRETURN = [PRETURN_S, PRETURN_T]

RIGHT_TURN_S = [-45,[-10 ,10],0,[15 ,-15],0,[-20 ,20],0]
RIGHT_TURN_T = [2,[1 ,1],2,[1, 1],2,[1 ,1],2]
RIGHT_TURN = [RIGHT_TURN_S, RIGHT_TURN_T]

LEFT_TURN_S = [45,[-10 ,10],0,[15,-15], 0, [-20 ,20], 0]
LEFT_TURN_T = [2,[1 ,1],2,[1, 1],2,[1, 1],2]
LEFT_TURN = [LEFT_TURN_S, LEFT_TURN_T]

SWAY_LEFT_S = [[-30, -10, -5, 0],[-40, -20, 20, 40], 0,[20, 5, -5, -20],0,[10, 5, -5, -10],0]
SWAY_LEFT_T =[[1, 1, 1, 1],[1, 1, 1, 1],4,[1, 1, 1, 1],4,[1, 1, 1, 1],4]
SWAY_LEFT = [SWAY_LEFT_S, SWAY_LEFT_T]

SWAY_RIGHT_S = [0,[40, 20, -20, -40], 0,[-20, -5, 5 ,20],0,[-10, -5, 5 ,10],0]
SWAY_RIGHT_T = [4,[1, 1, 1, 1],4,[1, 1, 1, 1],4,[1, 1, 1, 1],4]
SWAY_RIGHT = [SWAY_RIGHT_S, SWAY_RIGHT_T]

WORM_S = [[10, -20, 10],[-15, 30, -15],0,[20, -40, 20], [10, 0, -10],[-5, 10, -5],0]
WORM_T = [[1, 1, 1], [1, 1, 1],3,[1, 1, 1],[1, 1, 1],[1, 1, 1],3]
WORM = [WORM_S, WORM_T]

fill_db_steps = [ISO_LEFT, ISO_RIGHT, KNOCK, WAVE_BACK, WAVE_RIGHT, WAVE_LEFT, LEAN_BACK, DIP, HEAD_DOWN, HEAD_UP,
                      HEAD_TURN_RIGHT, HEAD_TURN_LEFT, TURN_BIG_RIGHT, TURN_BIG_LEFT, TURN_SMALL_RIGHT,
                      TURN_SMALL_LEFT, WAVE_DIAGONAL_RIGHT, WAVE_DIAGONAL_LEFT, SEMI_CIRCLE, LEAN, CIRCLE, BLOOM,
                      TURN_LEFT, FOLD_BACK, DANCE_STEP3, DANCE_STEP4,SPIN, TWIST, BOB, NOD,SEARCH_R, SEARCH_L,
                      SEARCH_R2, PRETURN, RIGHT_TURN, LEFT_TURN, SWAY_LEFT, SWAY_RIGHT, WORM]

LOOK_AROUND = ['HEAD_UP, HEAD_DOWN, HEAD_TURN_LEFT, HEAD_TURN_RIGHT, HEAD_UP, HEAD_DOWN, HEAD_TURN_LEFT, HEAD_TURN_RIGHT']


SMOOTH_GROOVE = ['SWAY_LEFT, SWAY_RIGHT, WAVE_LEFT, WAVE_RIGHT, LEAN_BACK, NOD']

THE_EXPLORER = ['SEARCH_R, SEARCH_L, SEARCH_R2, SEARCH_L, SEARCH_R, SEARCH_L, SEARCH_R2, SEARCH_L']

SIMPLE_GROOVE = ['NOD, NOD, NOD, NOD, NOD, NOD, NOD_S, NOD, NOD, NOD']

fill_db_dances = [LOOK_AROUND, SMOOTH_GROOVE, THE_EXPLORER, SIMPLE_GROOVE]