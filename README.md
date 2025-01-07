# Boxing Gym

boxing_gym is a Mike Tyson's Punch Out!! Gymnasium environment using [GymNESium](https://github.com/Hal609/GymNESium).

# Installation

The preferred installation of `boxing_gym` is from `pip`:

```shell
pip install boxing_gym
```

# Usage

Import the module
```
from boxing_gym import make_env
```

Create the environment
```
env = make_env()
```

Step the environment
```
env.step_async(action)
observation_, reward, done_, trun_, info = env.step_wait()
```

For a full example see: [MTPO-RL](https://github.com/Hal609/GymNESium)

# Disclaimer

**This project is provided for educational purposes only. It is not
affiliated with and has not been approved by Nintendo.**