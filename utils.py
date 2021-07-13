import re
from math import fabs




def reward_engineering(state, action, reward, next_state, done):
    """
    Makes reward engineering to allow faster training in the Mountain Car environment.

    :param state: state.
    :type state: NumPy array with dimension (1, 2).
    :param action: action.
    :type action: int.
    :param reward: original reward.
    :type reward: float.
    :param next_state: next state.
    :type next_state: NumPy array with dimension (1, 2).
    :param done: if the simulation is over after this experience.
    :type done: bool.
    :return: modified reward for faster training.
    :rtype: float.
    """
    # Todo: implement reward engineering
    position = state[0]
    velocity = state[1]
    angle = state[2]
    angular_velocity = state[3]
    angular_direction = int(fabs(angle*angular_velocity) >= angle*angular_velocity)
    direction = int(fabs(position*velocity) >= position*velocity)

    reward = reward - angle**2 + angular_direction*angular_velocity**2 + direction*velocity**2
    reward = reward + 50 * int(fabs(angle) <= 1e-3 and fabs(position) <= 1e-3)


    return reward


