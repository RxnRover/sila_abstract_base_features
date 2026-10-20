from abc import ABC, abstractmethod
from typing import Any

from unitelabs.cdk import sila


class KeypadControllerBase(sila.Feature, ABC):
    """Represents a keypad on a device that can be disabled."""

    def __init__(self, **kwarg: Any) -> None:
        """Instantiates the feature.

        In concrete features, be sure to set the feature metadata provided in
        `https://docs.unitelabs.io/connector-development/reference/feature-metadata/#version`__.
        """
        super().__init__(
            category="security",  # TODO: check for existing categories
            **kwarg,
        )

    @abstractmethod
    @sila.UnobservableCommand()
    def enable(self) -> None:
        """Enables the keypad to allow physical operation."""

    @abstractmethod
    @sila.UnobservableCommand()
    def disable(self) -> None:
        """Disables the keypad to prevent physical operation."""

    @abstractmethod
    @sila.UnobservableProperty()
    def get_is_enabled(self) -> bool:
        """Gets the enabled state of the keypad.

        :return: Whether the keypad is enabled (True) or or not (False)
        :rtype: bool
        """
