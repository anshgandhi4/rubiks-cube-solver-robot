CORNER_COLOR_TO_POSITION = 'A_B___D_CM_N___P_OI_J___L_KU_V___X_WE_F___H_GQ_R___T_S'
CORNER_PIECE_STRING = ['AER', 'BNQ', 'CJM', 'DFI', 'GLU', 'HSX', 'KPV', 'OTW']
EDGE_COLOR_TO_POSITION = '_A_D_B_C__M_P_N_O__I_L_J_K__U_X_V_W__E_H_F_G__Q_T_R_S_'
EDGE_PIECE_STRING = ['AQ', 'BM', 'CI', 'DE', 'FL', 'GX', 'HR', 'JP', 'KU', 'NT', 'OV', 'SW']

def op_corners(inp, out):
    corner_colors = [''.join([inp[CORNER_COLOR_TO_POSITION.index(char)] for char in string]) for string in CORNER_PIECE_STRING]
    sorted_corner_colors = [''.join(sorted(string)) for string in corner_colors]
    solved_corner_colors = [''.join([out[CORNER_COLOR_TO_POSITION.index(char)] for char in string]) for string in CORNER_PIECE_STRING]
    sorted_solved_corner_colors = [''.join(sorted(string)) for string in solved_corner_colors]

    visited_corners = [True] + [False] * 7
    output = ''
    current_position = 'E'

    while visited_corners != [True] * 8:
        index = 0
        position_index = 0
        for i in range(len(CORNER_PIECE_STRING)):
            if current_position in CORNER_PIECE_STRING[i]:
                index = i
                position_index = CORNER_PIECE_STRING[i].index(current_position)
                break

        index1 = sorted_solved_corner_colors.index(sorted_corner_colors[index])
        position_index1 = solved_corner_colors[index1].index(corner_colors[index][position_index])

        new_position = CORNER_PIECE_STRING[index1][position_index1]
        if not visited_corners[index1]:
            visited_corners[index1] = True
        else:
            for i in range(8):
                if not visited_corners[i]:
                    if corner_colors[i] == solved_corner_colors[i]:
                        visited_corners[i] = True
                        new_position = ''
                    else:
                        new_position = CORNER_PIECE_STRING[i][0]
                        break

        output += new_position
        current_position = new_position

    return output

def op_edges(inp, out):
    edge_colors = [''.join([inp[EDGE_COLOR_TO_POSITION.index(char)] for char in string]) for string in EDGE_PIECE_STRING]
    sorted_edge_colors = [''.join(sorted(string)) for string in edge_colors]
    solved_edge_colors = [''.join([out[EDGE_COLOR_TO_POSITION.index(char)] for char in string]) for string in EDGE_PIECE_STRING]
    sorted_solved_edge_colors = [''.join(sorted(string)) for string in solved_edge_colors]

    visited_edges = [False] + [True] + [False] * 10
    output = ''
    current_position = 'B'

    while visited_edges != [True] * 12:
        index = 0
        position_index = 0
        for i in range(len(EDGE_PIECE_STRING)):
            if current_position in EDGE_PIECE_STRING[i]:
                index = i
                position_index = EDGE_PIECE_STRING[i].index(current_position)
                break

        index1 = sorted_solved_edge_colors.index(sorted_edge_colors[index])
        position_index1 = solved_edge_colors[index1].index(edge_colors[index][position_index])

        new_position = EDGE_PIECE_STRING[index1][position_index1]
        if not visited_edges[index1]:
            visited_edges[index1] = True
        else:
            for i in range(12):
                if not visited_edges[i]:
                    if edge_colors[i] == solved_edge_colors[i]:
                        visited_edges[i] = True
                        new_position = ''
                    else:
                        new_position = EDGE_PIECE_STRING[i][0]
                        break

        output += new_position
        current_position = new_position

    return output
