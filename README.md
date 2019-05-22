# gym-zelda-1

[![BuildStatus][build-status]][ci-server]
[![PackageVersion][pypi-version]][pypi-home]
[![PythonVersion][python-version]][python-home]
[![Stable][pypi-status]][pypi-home]
[![Format][pypi-format]][pypi-home]
[![License][pypi-license]](LICENSE)

[build-status]: https://travis-ci.com/Kautenja/gym-zelda-1.svg?branch=master
[ci-server]: https://travis-ci.com/Kautenja/gym-zelda-1
[pypi-version]: https://badge.fury.io/py/gym-zelda-1.svg
[pypi-license]: https://img.shields.io/pypi/l/gym-zelda-1.svg
[pypi-status]: https://img.shields.io/pypi/status/gym-zelda-1.svg
[pypi-format]: https://img.shields.io/pypi/format/gym-zelda-1.svg
[pypi-home]: https://badge.fury.io/py/gym-zelda-1
[python-version]: https://img.shields.io/pypi/pyversions/gym-zelda-1.svg
[python-home]: https://python.org

An [OpenAI Gym](https://github.com/openai/gym) environment for The Legend of
Zelda (i.e., Zelda 1) on The Nintendo Entertainment System (NES) based on
the [nes-py](https://github.com/Kautenja/nes-py) emulator.

## Installation

The preferred installation of `gym-zelda-1` is from `pip`:

```shell
pip install gym-zelda-1
```

## Usage

### Python

You must import `gym_zelda_1` before trying to make an environment.
This is because gym environments are registered at runtime. By default,
`gym_zelda_1` environments use the full NES action space of 256
discrete actions. To contstrain this, `gym_zelda_1.actions` provides
three actions lists (`RIGHT_ONLY`, `SIMPLE_MOVEMENT`, and `COMPLEX_MOVEMENT`)
for the `nes_py.wrappers.BinarySpaceToDiscreteSpaceEnv` wrapper. See
[gym_zelda_1/actions.py](gym_zelda_1/actions.py) for a
breakdown of the legal actions in each of these three lists.

```python
from nes_py.wrappers import BinarySpaceToDiscreteSpaceEnv
import gym_zelda_1
from gym_zelda_1.actions import SIMPLE_MOVEMENT
env = gym_zelda_1.make('Zelda1-v0')
env = BinarySpaceToDiscreteSpaceEnv(env, SIMPLE_MOVEMENT)

done = True
for step in range(5000):
    if done:
        state = env.reset()
    state, reward, done, info = env.step(env.action_space.sample())
    env.render()

env.close()
```

**NOTE:** `gym_zelda_1.make` is just an alias to `gym.make` for
convenience.

**NOTE:** remove calls to `render` in training code for a nontrivial
speedup.

### Command Line

`gym_zelda_1` features a command line interface for playing
environments using either the keyboard, or uniform random movement.

```shell
gym_zelda_1 -m <`human` or `random`>
```

## Step

Info about the rewards and info returned by the `step` method.

### Reward Function

TODO

### `info` dictionary

The `info` dictionary returned by the `step` method contains the following
keys:

| Key         | Type   | Description
|:------------|:-------|:------------------------------------------------------|
| `x_pos`     | `int`  | Link's _x_ position in the screen (from the left)
| `y_pos`     | `int`  | Link's _y_ position in the screen (from the top)
| `direction` | `str`  | Link's direction as one of _{"N", "S", "E", "W"}_

## Citation

Please cite `gym-zelda-1` if you use it in your research.

```tex
@misc{gym-zelda-1,
  author = {Christian Kauten},
  title = {{The Legend of Zelda} for {OpenAI Gym}},
  year = {2019},
  publisher = {GitHub},
  howpublished = {\url{https://github.com/Kautenja/gym-zelda-1}},
}
```
