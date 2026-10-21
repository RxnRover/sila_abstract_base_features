from abc import ABC, abstractmethod
from typing import Any

from unitelabs.cdk import sila


class PressureSensorControllerBase(sila.Feature, ABC):
    """Represents a pressure sensor."""

    def __init__(self, **kwarg: Any) -> None:
        """Instantiates the feature.

        In concrete features, be sure to set the feature metadata provided in
        `https://docs.unitelabs.io/connector-development/reference/feature-metadata/#version`__.
        """
        super().__init__(
            category="pressure",  # TODO: check for existing categories
            **kwarg,
        )

    @abstractmethod
    @sila.UnobservableCommand()
    def get_pressure(self) -> float:
        """Gets the current pressure measured by the sensor."""
