def get_next(state):
    """ given a (partial) state, return a set of possible candidates for the next position."""
    pass


def is_goal(state):
    """ Given a state, check whether this state is a valid solution."""
    pass


ans = []  # answers


def backtracking(state):
    if is_goal(state):
        # if this state is a solution, record it into answer
        # since state is list (mutable), need to do a deep copy
        ans.append(state[:])
        return  # 找到答案就停止
    else:
        for candidate in get_next(state):
            # add the next possible candidate to current (partial) solution
            state.append(candidate)
            # recursively solving
            backtracking(state)
            # after trying all following states by the recursive call, remove previous candidate
            state.pop()  # 回溯操作
