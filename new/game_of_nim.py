from gamestest import * 

class GameOfNim(Game):
    def __init__(self, board):
        # Similar to TicTacToe, we can define the parameters of our problem.
        moves = []
        for i in range(len(board)):
            for j in range(1, board[i] + 1):  # ex.) changed from [0,5) to [1,6)
                moves.append((i, j))
        self.initial = GameState(to_move="MAX", utility=1, board=board, moves=moves)

    def result(self, state, move):
        if move not in state.moves:
            return state
        board = state.board.copy()  # creates copy of the board
        (index, amount_to_remove) = move  # unpacks the index and the amount to remove
        board[index] -= amount_to_remove  # removes amount from element at position
        moves = []  # create a new move list with new bounds
        for i in range(len(board)):
            for j in range(1, board[i] + 1):
                moves.append((i, j))
        return GameState(
            to_move=("MAX" if state.to_move == "MIN" else "MIN"),
            utility=(-1 if state.to_move == "MIN" else 1),
            board=board,
            moves=moves,
        )

    def actions(self, state):
        # return moves list
        return state.moves

    def terminal_test(self, state):
        # returns true if no more moves left or if the board is all zeroes
        return True if len(state.moves) == 0 or sum(state.board) == 0 else False

    def utility(self, state, player):
        # if "MAX" wins return 1, else return -1
        return state.utility if player == "MAX" else -state.utility

    def to_move(self, state):
        # Return the player whose move it is in this state
        return state.to_move


if __name__ == "__main__":
    nim = GameOfNim(board=[7, 5, 3, 1])  # Creating the game instance
    # nim = GameOfNim(board=[7, 5, 3, 1]) # a much larger tree to search
    print(nim.initial.board)  # must be [0, 5, 3, 1]
    print(
        nim.initial.moves
    )  # must be [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2,1), (2, 2), (2, 3), (3, 1)]
    print(nim.result(nim.initial, (1, 2)))
    utility = nim.play_game(alpha_beta_player, query_player)  # computer moves first
    if utility < 0:
        print("MIN won the game")
    else:
         print("MAX won the game")