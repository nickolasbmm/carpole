from math import fabs

LIMIT_ANGLE = 0.418/4
LIMIT_POSITION = 4.8/4



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
    next_position = next_state[0]
    next_angle = next_state[1]

    reward = reward - angle**2 - angular_velocity**2 - position**2 - velocity**2
    reward = reward + 1 + int(fabs(next_angle) <= LIMIT_ANGLE and fabs(next_position) <= LIMIT_POSITION)


    return reward


