"""An OpenAI Gym environment for The Legend of Zelda."""
import collections
import os
from nes_py import NESEnv
import numpy as np


# the directory that houses this module
MODULE_DIR = os.path.dirname(os.path.abspath(__file__))


# the path to the Zelda 1 ROM
ROM_PATH = os.path.join(MODULE_DIR, '_roms', 'Zelda_1.nes')


# a mapping of numeric values to cardinal directions
# $08=North, $04=South, $01=East, $02=West
DIRECTIONS = collections.defaultdict(lambda: None, {
    0x08: 'N',
    0x04: 'S',
    0x01: 'E',
    0x02: 'W',
})


class Zelda1Env(NESEnv):
    """An environment for playing The Legend of Zelda with OpenAI Gym."""

    # the legal range of rewards for each step
    reward_range = (-float('inf'), float('inf'))

    def __init__(self):
        """Initialize a new Zelda 1 environment."""
        super().__init__(ROM_PATH)
        # reset the emulator, skip the start screen, and create a backup state
        self.reset()
        self._skip_start_screen()
        self._backup()

    # MARK: Memory access

    @property
    def _x_pixel(self):
        """Return the current x pixel of Link's location."""
        return self.ram[0x70]

    @property
    def _y_pixel(self):
        """Return the current y pixel of Link's location."""
        return self.ram[0x84]

    @property
    def _direction(self):
        """Return the current direction that Link is facing."""
        return DIRECTIONS[self.ram[0x98]]

    @property
    def _is_paused(self):
        """Return True if the game is paused, False otherwise."""
        return bool(self.ram[0xE0])

    # MARK: RAM Hacks

    def _skip_start_screen(self):
        """Press and release start to skip the start screen."""
        # press and release the start button
        # self._frame_advance(8)
        # self._frame_advance(0)
        # # Press start until the game starts
        # while self._time == 0:
        #     # press and release the start button
        #     self._frame_advance(8)
        #     # if we're in the single stage, environment, write the stage data
        #     if self.is_single_stage_env:
        #         self._write_stage()
        #     self._frame_advance(0)
        #     # run-out the prelevel timer to skip the animation
        #     self._runout_prelevel_timer()
        # # set the last time to now
        # self._time_last = self._time
        # # after the start screen idle to skip some extra frames
        # while self._time >= self._time_last:
        #     self._time_last = self._time
        #     self._frame_advance(8)
        #     self._frame_advance(0)

    # MARK: Reward Function

    # MARK: nes-py API calls

    def _will_reset(self):
        """Handle and RAM hacking before a reset occurs."""
        pass

    def _did_reset(self):
        """Handle any RAM hacking after a reset occurs."""
        pass

    def _did_step(self, done):
        """
        Handle any RAM hacking after a step occurs.

        Args:
            done: whether the done flag is set to true

        Returns:
            None

        """
        pass

    def _get_reward(self):
        """Return the reward after a step occurs."""
        return 0
        # return self._x_reward + self._time_penalty + self._death_penalty

    def _get_done(self):
        """Return True if the episode is over, False otherwise."""
        return False

    def _get_info(self):
        """Return the info after a step occurs"""
        return dict(
            x_pos=self._x_pixel,
            y_pos=self._y_pixel,
            direction=self._direction,
            is_paused=self._is_paused,
        )


# explicitly define the outward facing API of this module
__all__ = [Zelda1Env.__name__]
