from search import *


eight_puzzle = EightPuzzle((1,2,3,5,7,4,8,6,0)) # <- change this

# if __name__ == '__main__':    
    #print(eight_puzzle.actions((0, 1, 2, 3, 4, 5, 6, 7, 8)))
    #print(eight_puzzle.result((0, 1, 2, 3, 4, 5, 6, 7, 8), 'DOWN'))
print(astar_search(eight_puzzle, h=None, display=True).solution())
# print(dfs(eight_puzzle, h=None, display=True).solution())

    # exit()
