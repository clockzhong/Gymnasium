"""run random envs"""
import gymnasium as gym
import pytest

envs_list = list(gym.registry.keys())

@pytest.mark.parametrize("env_name", envs_list)
def test_random_actions(env_name):
    """random action on one env"""
    env = gym.make(env_name, render_mode="human")
    print(f"Executing {env_name}")
    observation, info = env.reset()
    for _ in range(10):
        action = env.action_space.sample()  # agent policy that uses the observation and info
        observation, reward, terminated, truncated, info = env.step(action)

        if terminated or truncated:
            observation, info = env.reset()

    env.close()

def random_action_on_env(env_name):
    env = gym.make(env_name, render_mode="human")
    observation, info = env.reset()
    for _ in range(100):
        action = env.action_space.sample()  # agent policy that uses the observation and info
        observation, reward, terminated, truncated, info = env.step(action)

        if terminated or truncated:
            observation, info = env.reset()

    env.close()



def test_bug_on_mujoco_lib():
    """random action on one env"""
    random_action_on_env("Reacher-v2")
    random_action_on_env("Reacher-v5")
    random_action_on_env("Pusher-v2")
