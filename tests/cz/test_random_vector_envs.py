"""run random vector envs"""
import gymnasium as gym
import pytest
import time

def random_action_on_vec_env(env_name, num_envs=3):
    envs = gym.make_vec(env_name, num_envs=num_envs, render_mode="human")
    #
    observation, info = envs.reset()
    for _ in range(50):
        actions = envs.action_space.sample()  # agent policy that uses the observation and info
        observations, rewards, terminateds, truncateds, infos = envs.step(actions)
        #time.sleep(0.5)
        time.sleep(0.05)
    #
    envs.close()


def test_bug_on_mujoco_lib():
    """Use this case to locate root cause of a special bug relating to mujoco lib"""
    random_action_on_vec_env("CartPole-v1")


