"""
https://github.com/lazyprogrammer/machine_learning_examples/tree/master/rl2
"""

# =============================================
# RANDOM SEARCH
# =============================================

import gym
import numpy as np
import matplotlib.pyplot as plt


def get_action(s, w):
    return 1 if s.dot(w) > 0 else 0 # .dot does multiplication between two arrays


def play_one_episode(env, params):
    observation = env.reset()
    done = False
    t = 0
    while not done and t < 10000:  # cap the limit of a single episode to 10000 frames
        t += 1
        action = get_action(observation, params)
        observation, reward, done, info = env.step(action)
        if done:
            break
    return t  # returns the number of frames that the env has lasted


def play_multiple_episodes(env, T, params):
    episode_lengths = np.empty(T)
    for i in range(T):  # 100 episodes for parameter set (random so far)
        episode_lengths[i] = play_one_episode(env, params)
    avg_length = episode_lengths.mean()  # computes the mean duration of the episodes with a certain set of parameters
    print("avg length: ", avg_length)
    return avg_length


def random_search(env):
    episode_lengths = []
    best = 0
    params = None
    for t in range(100):  # testing 100 random parameters, each test has 100 episodes
        new_params = np.random.random(4) * 2 - 1
        avg_length = play_multiple_episodes(env, 100, new_params)
        episode_lengths.append(avg_length)
        if avg_length > best:
            params = new_params
            best = avg_length
    return episode_lengths, params


env = gym.make('CartPole-v0')
env.reset()  # loads the start state
episode_lengths, params = random_search(env)
plt.plot(episode_lengths)
plt.show()
# features:
# cart position , cart velocity, pole position, pole velocity at tip
# print(env.action_space) # number of possible actions

"""
#run episodes
done=False
while not done:
    # play an episode: send actions
    observation, reward, done, info = env.step(action) # info is only for debugging
"""
