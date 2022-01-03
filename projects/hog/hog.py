"""CS 61A Presents The Game of Hog."""

from dice import six_sided, make_test_dice, four_sided
from ucb import main

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.


######################
# Phase 1: Simulator #
######################

# 没有完全理解！！！
def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.

    num_rolls:  The number of dice rolls that will be made.
    dice:       A function that simulates a single dice roll outcome.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    mark = 0
    one = 0
    while num_rolls:
        num_rolls -= 1
        temp = dice()
        if temp == 1:
            one = temp
        else:
            mark += temp
    if one:
        return 1
    return mark
    # END PROBLEM 1


def free_bacon(score):
    """Return the points scored from rolling 0 dice (Free Bacon).

    score:  The opponent's current score.
    """
    assert score < 100, 'The game should be over.'
    # BEGIN PROBLEM 2
    if score < 10:
        return abs(score) + 2
    else:
        score1 = 2 + abs(score // 10 - score % 10)
        return score1
    # END PROBLEM 2


def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free Bacon).
    Return the points scored for the turn by the current player.

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function that simulates a single dice roll outcome.
    """
    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    # BEGIN PROBLEM 3
    if num_rolls == 0:
        return free_bacon(opponent_score)
    return roll_dice(num_rolls, dice)
    # END PROBLEM 3


# 需要assert吗？
def is_swap(score0, score1):
    """Return whether one of the scores is an integer multiple of the other."""
    # BEGIN PROBLEM 4
    if score0 > 1 and score1 > 1:
        if score0 % score1 == 0 or score1 % score0 == 0:
            return True
        else:
            return False
    else:
        return False

    # END PROBLEM 4


def other(player):
    """Return the other player, for a player PLAYER numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - player


def silence(score0, score1):
    """Announce nothing (see Phase 2)."""
    return silence


def play(strategy0, strategy1, score0=0, score1=0, dice=six_sided,
         goal=GOAL_SCORE, say=silence):
    """Simulate a game and return the final scores of both players, with Player
    0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments (the
    current player's score, and the opponent's score), and returns a number of
    dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first.
    strategy1:  The strategy function for Player 1, who plays second.
    score0:     Starting score for Player 0
    score1:     Starting score for Player 1
    dice:       A function of zero arguments that simulates a dice roll.
    goal:       The game ends and someone wins when this score is reached.
    say:        The commentary function to call at the end of the first turn.
    """
    player = 0  # Which player is about to take a turn, 0 (first) or 1 (second)
    # BEGIN PROBLEM 5
    while score0 < goal and score1 < goal:
        if player == 0:
            num_rolls = strategy0(score0, score1)
            score0 += take_turn(num_rolls, score1, dice)
        elif player == 1:
            num_rolls = strategy1(score1, score0)
            score1 += take_turn(num_rolls, score0, dice)
        if is_swap(score0, score1):
            score0, score1 = score1, score0  # cool!!!
        player = other(player)
        say = say(score0, score1)
        # I don't UNDERSTAND！！！
    # END PROBLEM 5
    return score0, score1


#######################
# Phase 2: Commentary #
#######################


def say_scores(score0, score1):
    """A commentary function that announces the score for each player."""
    print("Player 0 now has", score0, "and Player 1 now has", score1)
    return say_scores


def announce_lead_changes(previous_leader=None):
    """Return a commentary function that announces lead changes.

    >>> f0 = announce_lead_changes()
    >>> f1 = f0(5, 0)
    Player 0 takes the lead by 5
    >>> f2 = f1(5, 12)
    Player 1 takes the lead by 7
    >>> f3 = f2(8, 12)
    >>> f4 = f3(8, 13)
    >>> f5 = f4(15, 13)
    Player 0 takes the lead by 2
    """

    def say(score0, score1):
        if score0 > score1:
            leader = 0
        elif score1 > score0:
            leader = 1
        else:
            leader = None
        if leader is not None and leader != previous_leader:
            print('Player', leader, 'takes the lead by', abs(score0 - score1))
        return announce_lead_changes(leader)

    return say


def both(f, g):
    """Return a commentary function that says what f says, then what g says.

    >>> h0 = both(say_scores, announce_lead_changes())
    >>> h1 = h0(10, 0)
    Player 0 now has 10 and Player 1 now has 0
    Player 0 takes the lead by 10
    >>> h2 = h1(10, 6)
    Player 0 now has 10 and Player 1 now has 6
    >>> h3 = h2(6, 18) # Player 0 gets 8 points, then Swine Swap applies
    Player 0 now has 6 and Player 1 now has 18
    Player 1 takes the lead by 12
    """

    def say(score0, score1):
        return both(f(score0, score1), g(score0, score1))

    return say


def announce_highest(who, previous_high=0, previous_score=0):
    """Return a commentary function that announces when WHO's score
    increases by more than ever before in the game.

    >>> f0 = announce_highest(1)  #  Only announce Player 1 score gains
    >>> f1 = f0(11, 0)
    >>> f2 = f1(11, 1)
    1 point! That's the biggest gain yet for Player 1
    >>> f3 = f2(20, 1)
    >>> f4 = f3(5, 20) # Player 1 gets 4 points, then Swine Swap applies
    19 points! That's the biggest gain yet for Player 1
    >>> f5 = f4(20, 40) # Player 0 gets 35 points, then Swine Swap applies
    20 points! That's the biggest gain yet for Player 1
    >>> f6 = f5(20, 55) # Player 1 gets 15 points; not enough for a new high
    """
    assert who == 0 or who == 1, 'The who argument should indicate a player.'

    # BEGIN PROBLEM 7
    def say(score0, score1):
        if who == 0:
            current_score = score0
            gain = score0 - previous_score
        elif who == 1:
            current_score = score1
            gain = score1 - previous_score
        if gain > previous_high:
            if gain == 1:
                print("1 point! That's the biggest gain yet for Player", who)  # 中间有'的话外面用双引号省事儿！！！
            else:
                print(gain, "points! That's the biggest gain yet for Player", who)
        return announce_highest(who, max(previous_high, gain), current_score)
    return say

    # 写法2
    # def say(score0, score1):
    #     current_score = score0 if who == 0 else score1
    #     gain = current_score - previous_score
    #     if gain > previous_high:
    #         if gain == 1:
    #             print("1 point! That's the biggest gain yet for Player", who)
    #         else:
    #             print(gain, "points! That's the biggest gain yet for Player", who)
    #     return announce_highest(who, max(previous_high, gain), current_score)
    #
    # return say

# 这样写不行，因为内层函数不能在代码段中修改外层函数的变量
# （外层函数变量只能作为参数传递给内层函数的变量，而若要修改外层变量，可以通过return返回值传递）

    # def say(score0, score1):
    # 	nonlocal previous_high, previous_score  # 不然会警告⚠️是未解析的参数
    # 	if who == 0:
    # 		current_score = score0 - previous_score
    # 		previous_score = score0
    # 	elif who == 1:
    # 		current_score = score1 - previous_score
    # 		previous_score = score1
    # 	if current_score > previous_high:
    # 		if current_score == 1:
    # 			print("1 point! That's the biggest gain yet for Player", who)  # 中间有'的话外面用双引号省事儿！！！
    # 		else:
    # 			print(current_score, "points! That's the biggest gain yet for Player", who)
    # 		previous_high = current_score
    # 	return announce_highest(who, previous_high, previous_score)
    #
    # return say

    # END PROBLEM 7


#######################
# Phase 3: Strategies #
#######################


def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments (the
    current player's score, and the opponent's score), and returns a number of
    dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """

    def strategy(score, opponent_score):
        return n

    return strategy


def make_averaged(fn, num_samples=100000):
    """Return a function that returns the average value of FN when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(4, 2, 5, 1)
    >>> averaged_dice = make_averaged(dice, 1000)
    >>> averaged_dice()
    3.0
    """

    # BEGIN PROBLEM 8
    def outcome(*args):
        result = 0
        num = 0
        while num < num_samples:
            result += fn(*args)
            num += 1
        return result / num_samples

    return outcome
    # END PROBLEM 8


def max_scoring_num_rolls(dice=six_sided, num_samples=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE over NUM_SAMPLES times.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(1, 6)
    >>> max_scoring_num_rolls(dice)
    1
    """
    # BEGIN PROBLEM 9
    average_roll_dice = make_averaged(roll_dice, num_samples)
    highest_num_rolls, highest_score = 1, 1
    for num_rolls in range(1, 11):
        score = average_roll_dice(num_rolls, dice)
        if score > highest_score:
            highest_num_rolls, highest_score = num_rolls, score
    return highest_num_rolls

    # END PROBLEM 9


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(4)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


#  想不明白为什么这么算

def run_experiments():
    """Run a series of strategy experiments and report results."""
    if True:  # Change to False when done finding max_scoring_num_rolls
        six_sided_max = max_scoring_num_rolls(six_sided)
        print('Max scoring num rolls for six-sided dice:', six_sided_max)

    if True:  # Change to True to test always_roll(8)
        print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    if True:  # Change to True to test bacon_strategy
        print('bacon_strategy win rate:', average_win_rate(bacon_strategy))

    if True:  # Change to True to test swap_strategy
        print('swap_strategy win rate:', average_win_rate(swap_strategy))

    if True:  # Change to True to test final_strategy
        print('final_strategy win rate:', average_win_rate(final_strategy))

    "*** You may add additional experiments as you wish ***"


def bacon_strategy(score, opponent_score, margin=8, num_rolls=4):
    """This strategy rolls 0 dice if that gives at least MARGIN points, and
    rolls NUM_ROLLS otherwise.
    """
    # BEGIN PROBLEM 10
    standard = (abs(opponent_score // 10 - opponent_score % 10) + 2)
    if standard >= margin:
        return 0
    else:
        return num_rolls
    # END PROBLEM 10


def swap_strategy(score, opponent_score, margin=8, num_rolls=4):
    """This strategy rolls 0 dice when it triggers a beneficial swap. It also
    rolls 0 dice if it gives at least MARGIN points. Otherwise, it rolls
    NUM_ROLLS.
    """
    # BEGIN PROBLEM 11
    if is_swap(score + abs(opponent_score // 10 - opponent_score % 10) + 2, opponent_score):
        if score + abs(opponent_score // 10 - opponent_score % 10) + 2 < opponent_score:
            return 0
        else:
            return num_rolls
    return bacon_strategy(score, opponent_score, margin, num_rolls)
    #  return语句更简洁！

    # END PROBLEM 11


def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.

    *** YOUR DESCRIPTION HERE ***
    """
    # BEGIN PROBLEM 12
    return swap_strategy(score, opponent_score, margin=make_averaged(always_roll(8), 1000)(score, opponent_score),
                         num_rolls=8)

    # END PROBLEM 12


##########################
# Command Line Interface #
##########################

# NOTE: Functions in this section do not need to be changed. They use features
# of Python not yet covered in the course.


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions.

    This function uses Python syntax/techniques not yet covered in this course.
    """
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()
