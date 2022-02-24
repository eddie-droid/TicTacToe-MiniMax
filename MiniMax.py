from copy import deepcopy

from TicTacToe import TicTacToeGame


def minimax(node, player, alpha, beta):


    if (len(node.get_children()) == 0):

        mark = node.path[0].player_turn


        return node.get_util(mark), node.path

    #X is maximizing player
    elif(player == 'X'):

        frontier = node.get_children()

        while len(frontier) != 0:

            temp = deepcopy(frontier.pop(0))


            score, maxnode = minimax(temp, 'O', alpha, beta)


            if score >= beta:
                return score, None
            elif score > alpha:
                alpha = score
                node.path=(maxnode)
        return alpha, node.path
    #O is minimizing player
    else:

        frontier = node.get_children()


        while len(frontier) != 0:

            temp = deepcopy(frontier.pop(0))



            score, minnode = minimax(temp, 'X', alpha, beta)

            if score <= alpha:
                return score, None

            elif score < beta:
                beta = score
                node.path = minnode
        return beta, node.path




