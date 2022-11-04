from search import *

class WolfGoatCabbage(Problem):
    def __init__(self, initial=frozenset({'F', 'G', 'W', 'C'}), goal=frozenset()):
        """The constructor specifies the initial state, and possibly a goal
        state, if there is a unique goal. Your subclass's constructor can add
        other arguments."""
        self.initial = initial
        self.goal = goal

    def actions(self, state):
        """Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once."""
        possible_actions = [{'F'}, {'G', 'F'}, {'W', 'F'}, {'C', 'F'}]
        length = len(state)

        # if {F, G, W, C}
        if length == 4:
            return [possible_actions[1]]

        # if state == G
        if length == 1:
            if 'G' in state:
                return [possible_actions[0]]
            if 'W' in state:
                return [possible_actions[1]]
            if 'C' in state:
                return [possible_actions[1]]

        # if F is in the state, F will never cross alone
        if 'F' in state:
            possible_actions.remove({'F'})

        # if F and object aren't on the same side of the bank, they can't move together
        objs = ['W', 'G', 'C']
        for obj in objs:
            if ('F' not in state) ^ (obj not in state):
                possible_actions.remove({obj, 'F'})

        return possible_actions

    def result(self, state, action):
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""
        new_state = list(state)

        for elem in action:
            if elem in new_state:
                new_state.remove(elem)
            else:
                new_state.append(elem)
                
        return frozenset(tuple(new_state))

    def goal_test(self, state):
        """ Given a state, return True if state is a goal state or False, otherwise """

        return state == self.goal
 
if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)