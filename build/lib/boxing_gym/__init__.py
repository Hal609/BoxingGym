"""Registration code of Gym environments in this package."""
from .mtpo_env import PunchOutEnv
from .MTPOPreprocessing import MTPOPreprocessingCustom
import gymnasium as gym
import os

def make_env(envs_create:int=1, framestack:int=4, headless:bool=False) -> gym.vector.AsyncVectorEnv:
    '''
    Create a vectorised MTPO environment.

    Args:
        envs_create (int): The number of parallel environments to create. Defaults to 1
        framestack (int): The number of frames which are stacked together to form 1 observation. Defaults to 4
        headless (bool): Whether the environments should be headless, i.e. no window is displayed. Defaults to False

    Returns:
        gym.vector.AsyncVectorEnv: Vectorised Gym environment.
    '''
    rom = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.bin")

    print(f"Creating {envs_create} envs")

    def create_env():
        gym.register(
            id="gymnasium_env/mtpo-v5",
            entry_point=PunchOutEnv,
        )
        env = MTPOPreprocessingCustom(gym.make("gymnasium_env/mtpo-v5", rom_path=rom, headless=headless, fps_limit=60))

        return gym.wrappers.FrameStackObservation(env, stack_size=framestack)
    
    return gym.vector.AsyncVectorEnv(
        [lambda: create_env() for _ in range(envs_create)],
        context="spawn",  # Required for Windows
    )

# define the outward facing API of this package
__all__ = [make_env.__name__]