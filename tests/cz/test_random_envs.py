"""run random envs"""
import gymnasium as gym
import pytest

def random_action_on_env(env_name, workaround_743=True):
    env = gym.make(env_name, render_mode="human")
    #entry_point = env.spec.entry_point
    #print(env.metadata["render_modes"])

    if workaround_743 and "mujoco" in entry_point:
    #Workaround for bug: https://github.com/Farama-Foundation/Gymnasium/issues/743
        env.close()
        return
    observation, info = env.reset()
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


envs_list = list(gym.registry.keys())
envs_list.remove("GymV21Environment-v0")
envs_list.remove("GymV26Environment-v0")

@pytest.mark.parametrize("env_name", envs_list)
def test_random_actions(env_name):
    """random action on every env"""
    random_action_on_env(env_name)



def test_bug_on_mujoco_lib():
    """Use this case to locate root cause of a special bug relating to mujoco lib"""
    random_action_on_env("Reacher-v2", workaround_743=False)
    random_action_on_env("Reacher-v5", workaround_743=False)
    random_action_on_env("Pusher-v2", workaround_743=False)


