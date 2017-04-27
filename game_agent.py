"""This file contains all the classes you must complete for this project.

You can use the test cases in agent_test.py to help during development, and
augment the test suite with your own test cases to further test your code.

You must test your agent's strength against a set of agents with known
relative strength using tournament.py and include the results in your report.
"""
import random
import sys

class Timeout(Exception):
    """Subclass base exception for code clarity."""
    pass


# HEURISTIC .
def heuristic_score_player_moves(game, player):
    if game.is_winner(player):
        return float('inf')
    if game.is_loser(player):
        return float('-inf')

    player_moves = game.get_legal_moves(player)

    return float(len(player_moves))


# HEURISTIC improved_score.
def heuristic_score_normal_difference_moves(game, player):
    if game.is_winner(player):
        return float('inf')
    if game.is_loser(player):
        return float('-inf')

    player_moves = game.get_legal_moves(player)
    opponent_moves = game.get_legal_moves(game.get_opponent(player))

    return float(len(player_moves) - len(opponent_moves))


# HEURISTIC : difference of squared number of legal moves of player and opponent
def heuristic_score_quadratic_difference_moves(game, player):
    if game.is_winner(player):
        return float('inf')
    if game.is_loser(player):
        return float('-inf')

    player_moves = game.get_legal_moves(player)
    opponent_moves = game.get_legal_moves(game.get_opponent(player))

    return float(len(player_moves)*len(player_moves) - len(opponent_moves)*len(opponent_moves))


# HEURISTIC: min of 3 heuristics.
def heuristic_score_min_custom_score(game, player):
    if game.is_winner(player):
        return float('inf')
    if game.is_loser(player):
        return float('-inf')

    functions = [heuristic_score_player_moves(game, player), 
                heuristic_score_normal_difference_moves(game, player), 
                heuristic_score_quadratic_difference_moves(game, player)]

    return min(functions)

    # HEURISTIC: assign weights to 3 heuristics.
def heuristic_score_final_custom_score(game, player, pm_weight=0.1, ndm_weight=2, qdm_weight= 0.4):
    if game.is_winner(player):
        return float('inf')
    if game.is_loser(player):
        return float('-inf')

    functions = [heuristic_score_player_moves(game, player), 
                heuristic_score_normal_difference_moves(game, player), 
                heuristic_score_quadratic_difference_moves(game, player)]

    weights = [pm_weight, ndm_weight, qdm_weight]   

    return float(sum([i*j for i,j in zip(weights, functions)]))



heuristic = {
    'heuristic_score_player_moves': heuristic_score_player_moves,
    'heuristic_score_normal_difference_moves': heuristic_score_normal_difference_moves,
    'heuristic_score_quadratic_difference_moves': heuristic_score_quadratic_difference_moves,
    'heuristic_score_min_custom_score': heuristic_score_min_custom_score,
    'heuristic_score_final_custom_score': heuristic_score_final_custom_score
    }


def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """

    # TODO: finish this function!

    '''
    # HEURISTIC .
    def heuristic_score_player_moves(game, player):
        if game.is_winner(player):
            return float('inf')
        if game.is_loser(player):
            return float('-inf')

        player_moves = game.get_legal_moves(player)

        return float(len(player_moves))

    # HEURISTIC improved_score.
    def heuristic_score_normal_difference_moves(game, player):
        if game.is_winner(player):
            return float('inf')
        if game.is_loser(player):
            return float('-inf')

        player_moves = game.get_legal_moves(player)
        opponent_moves = game.get_legal_moves(game.get_opponent(player))

        return float(len(player_moves) - len(opponent_moves))


    # HEURISTIC : difference of squared number of legal moves of player and opponent
    def heuristic_score_quadratic_difference_moves(game, player):
        if game.is_winner(player):
            return float('inf')
        if game.is_loser(player):
            return float('-inf')

        player_moves = game.get_legal_moves(player)
        opponent_moves = game.get_legal_moves(game.get_opponent(player))

        return float(len(player_moves)*len(player_moves) - len(opponent_moves)*len(opponent_moves))


    # HEURISTIC: min of 3 heuristics.
    def heuristic_score_min_custom_score(game, player):
        if game.is_winner(player):
            return float('inf')
        if game.is_loser(player):
            return float('-inf')

        functions = [player_moves(game, player), 
                    normal_difference_moves(game, player), 
                    quadratic_difference_moves(game, player)]

        return min(functions)

    # HEURISTIC: assign weights to 3 heuristics.
    def heuristic_score_final_custom_score(game, player, pm_weight, ndm_weight, qdm_weight):
        if game.is_winner(player):
            return float('inf')
        if game.is_loser(player):
            return float('-inf')

        functions = [player_moves(game, player), 
                    normal_difference_moves(game, player), 
                    quadratic_difference_moves(game, player)]

        weights = [pm_weight, ndm_weight, qdm_weight]   

        return float(sum([i*j for i,j in zip(weights, functions)]))


    heuristic = {
    'heuristic_score_player_moves': heuristic_score_player_moves,
    'heuristic_score_normal_difference_moves': heuristic_score_normal_difference_moves,
    'heuristic_score_quadratic_difference_moves': heuristic_score_quadratic_difference_moves,
    'heuristic_score_min_custom_score': heuristic_score_min_custom_score,
    'heuristic_score_final_custom_score': heuristic_score_final_custom_score
    }

    #return min_custom_score(game, player)
    #return final_custom_score(game, player, 0, 1, 0.4)

    '''


    if game.is_winner(player):
        return float('inf')
    if game.is_loser(player):
        return float('-inf')
    
    #return heuristic[sys.argv[1]](game, player) # uncomment this to run the $ ./run_heuristics.sh
    return heuristic_score_final_custom_score(game, player)

    '''
    if game.is_winner(player):
        return float('inf')
    if game.is_loser(player):
        return float('-inf')

    player_moves = game.get_legal_moves(player)
    opponent_moves = game.get_legal_moves(game.get_opponent(player))

    return float(len(player_moves) - len(opponent_moves))
    '''
    

    #raise NotImplementedError


class CustomPlayer:
    """Game-playing agent that chooses a move using your evaluation function
    and a depth-limited minimax algorithm with alpha-beta pruning. You must
    finish and test this player to make sure it properly uses minimax and
    alpha-beta to return a good move before the search time limit expires.

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    iterative : boolean (optional)
        Flag indicating whether to perform fixed-depth search (False) or
        iterative deepening search (True).

    method : {'minimax', 'alphabeta'} (optional)
        The name of the search method to use in get_move().

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """

    def __init__(self, search_depth=3, score_fn=custom_score,
                 iterative=True, method='minimax', timeout=10.):
        self.search_depth = search_depth
        self.iterative = iterative
        self.score = score_fn
        self.method = method
        self.time_left = None
        self.TIMER_THRESHOLD = timeout

    def get_move(self, game, legal_moves, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        This function must perform iterative deepening if self.iterative=True,
        and it must use the search method (minimax or alphabeta) corresponding
        to the self.method value.

        **********************************************************************
        NOTE: If time_left < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        legal_moves : list<(int, int)>
            A list containing legal moves. Moves are encoded as tuples of pairs
            of ints defining the next (row, col) for the agent to occupy.

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """

        self.time_left = time_left

        # TODO: finish this function!

        # Perform any required initializations, including selecting an initial
        # move from the game board (i.e., an opening book), or returning
        # immediately if there are no legal moves

        possible_moves = []
        if len(legal_moves) ==0:
            return (-1, -1)

        try:
            # The search method call (alpha beta or minimax) should happen in
            # here in order to avoid timeout. The try/except block will
            # automatically catch the exception raised by the search method
            # when the timer gets close to expiring
            '''
            final_move = (-1, -1)
            score = 0

            if self.iterative:
                for depth in range(1, sys.maxsize):
                    if self.time_left <= self.TIMER_THRESHOLD:
                        return final_move

                    if self.method == 'minimax':
                        depth_score, depth_move = self.minimax(game, depth)
                    elif self.method == 'alphabeta':
                        depth_score, depth_move = self.alphabeta(game, depth)

                    if depth_move == (-1, -1):
                        return final_move

                        if depth_score >= score:
                            score = depth_score
                            final_move = depth_move

            else:
                if self.method == 'minimax':
                    score, move = self.minimax(game, self.search_depth)
                elif self.method == 'alphabeta':
                    score, move = self.alphabeta(game, self.search_depth)
                return move
            '''
            if self.iterative:
                for depth in range(1, sys.maxsize):  
                    if self.time_left() <= self.TIMER_THRESHOLD :
                        if len(possible_moves) != 0:
                            return max(possible_moves)[1]
                        else:
                            return (-1, -1)

                    if self.method == 'minimax':
                        possible_moves.append(self.minimax(game, depth))
                    elif self.method == 'alphabeta':
                        possible_moves.append(self.alphabeta(game, depth))

            else:
                if self.method == 'minimax':
                    possible_moves.append(self.minimax(game, self.search_depth))
                elif self.method == 'alphabeta':
                    possible_moves.append(self.alphabeta(game, self.search_depth))
            #pass


        except Timeout:
            # Handle any actions required at timeout, if necessary
            print("Depth {}: Timeout of iterative deepening.".format(depth))
            #pass

        # Return the best move from the last completed search iteration
        if len(possible_moves) != 0:
            final_move = max(possible_moves)[1]
            return final_move
        else:
            return (-1, -1)

        #raise NotImplementedError

    def minimax(self, game, depth, maximizing_player=True):
        """Implement the minimax search algorithm as described in the lectures.

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        maximizing_player : bool
            Flag indicating whether the current search depth corresponds to a
            maximizing layer (True) or a minimizing layer (False)

        Returns
        -------
        float
            The score for the current search branch

        tuple(int, int)
            The best move for the current branch; (-1, -1) for no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project unit tests; you cannot call any other
                evaluation function directly.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise Timeout()

        # TODO: finish this function!
        legal_moves = game.get_legal_moves()
        final_move = (-1, -1)

        if len(legal_moves)== 0 or depth == 0:
            return self.score(game, self), (-1, -1)

        

        if maximizing_player: # maximizing player (True) 
            score = float('-inf')
            for move in legal_moves:
                new_game = game.forecast_move(move)
                if depth ==1 :
                    new_score = self.score(new_game, self)
                else:
                    new_score, _ = self.minimax(new_game, depth-1, not maximizing_player)
                #score = max(score, new_score)
                if new_score > score:
                    score =  new_score
                    final_move = move
        else: # minimizing player (False)
            score = float('inf')
            for move in legal_moves:
                new_game = game.forecast_move(move)
                if depth == 1:
                    new_score = self.score(new_game, self)
                else:
                    new_score, _ = self.minimax(new_game, depth-1, not maximizing_player)
                #score = min(score, new_score)
                if new_score < score:
                    score =  new_score
                    final_move = move

        return score, final_move
        raise NotImplementedError

    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf"), maximizing_player=True):
        """Implement minimax search with alpha-beta pruning as described in the
        lectures.

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        maximizing_player : bool
            Flag indicating whether the current search depth corresponds to a
            maximizing player (True) or a minimizing player (False)

        Returns
        -------
        float
            The score for the current search branch

        tuple(int, int)
            The best move for the current branch; (-1, -1) for no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project unit tests; you cannot call any other
                evaluation function directly.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise Timeout()

        # TODO: finish this function!
        legal_moves = game.get_legal_moves()
        final_move = (-1, -1)

        if len(legal_moves)==0 or depth ==0:
            return self.score(game, self), (-1, -1)


        if maximizing_player: # maximizing player (True) 
            score = float('-inf')
            for move in legal_moves:
                new_game = game.forecast_move(move)
                if depth == 1:
                    new_score = self.score(new_game, self)
                else:
                    new_score, _ = self.alphabeta(new_game, depth-1, alpha, beta, not maximizing_player)
                #score = max(score, new_score)

                if new_score > score:
                    score =  new_score
                    final_move = move

                if score >= beta:
                    return score , final_move
                alpha = max(alpha, score)
        else: # minimizing player (False)
            score = float('inf')
            for move in legal_moves:
                new_game = game.forecast_move(move)
                if depth == 1:
                    new_score = self.score(new_game, self)
                else:
                    new_score, _ = self.alphabeta(new_game, depth-1, alpha, beta, not maximizing_player)
                #score = min(score, new_score)
                if new_score < score:
                    score =  new_score
                    final_move = move

                if score <= alpha:
                    return score, final_move
                beta = min(beta, score)


        return score, final_move

        #raise NotImplementedError
        #https://github.com/elainekmao/isolation-game/blob/master/ekm2133.py
        #http://aima.cs.berkeley.edu/python/games.html
