from abc import ABC, abstractmethod

from unitelabs.cdk import sila


class ExampleControllerBase(ABC, sila.Feature):
    """Example abstract base feature for an example controller feature."""

    @abstractmethod
    def action(self) -> int:
        """Example virtual action to be overridden.

        :return: Just an example value returned for us to check.
        :rtype: int
        """
        pass
