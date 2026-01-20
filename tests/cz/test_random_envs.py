"""run random envs"""
import gymnasium as gym
import pytest
from tests.envs.utils import all_testing_env_specs

def random_action_on_env(env_name, workaround_743=True):
    env = gym.make(env_name, render_mode="human")
    entry_point = env.spec.entry_point
    #print(env.metadata["render_modes"])
    _, _ = env.reset()
    for _ in range(10):
        action = env.action_space.sample()  # agent policy that uses the observation and info
        observation, reward, terminated, truncated, info = env.step(action)

        if terminated or truncated:
            observation, info = env.reset()

    env.close()


def random_action_on_env_without_reset(env_name):
    env = gym.make(env_name, autoreset=True)
    #entry_point = env.spec.entry_point
    #print(env.metadata["render_modes"])
    terminated, truncated = False, False
    observation, info = env.reset()
    while (not terminated) and (not truncated):
        action = env.action_space.sample()  # agent policy that uses the observation and info
        observation, reward, terminated, truncated, info = env.step(action)
    #env.close()
    return env, observation, reward, terminated, truncated, info


#envs_list = list(gym.registry.keys())
##envs_list.remove("GymV21Environment-v0")
#envs_list.remove("GymV26Environment-v0")

@pytest.mark.parametrize("env_name", all_testing_env_specs)
def test_random_actions(env_name):
    """random action on every env"""
    random_action_on_env(env_name)

