from abc import ABC, abstractmethod
from typing import Any

from unitelabs.cdk import sila


# TODO: Define potential custom Exceptions? See UniteLabs' WeighingServiceBase
# implementation:
# https://gitlab.com/unitelabs/cdk/python-cdk/-/blob/main/src/unitelabs/cdk/features/weighing/weighing_service/weighing_service_base.py
class InvalidFlowRate(Exception):
    """Report an invalid flow rate value provided."""


# TODO: How to handle units on different pumps?


class MeteringPumpControllerBase(sila.Feature, ABC):
    """Metering pumps deliver a continous rate of flow."""

    def __init__(self, **kwarg: Any) -> None:
        """Instantiates the feature.

        In concrete features, be sure to set the feature metadata provided in
        `https://docs.unitelabs.io/connector-development/reference/feature-metadata/#version`__.
        """
        super().__init__(
            category="pumps",  # TODO: check for existing categories
            **kwarg,
        )

    @abstractmethod
    @sila.UnobservableCommand()
    def start(self) -> None:
        """Starts the flow of the pump.

        :meth:``set_flow_rate()`` should be used to define a flow rate before
        starting the pump, although the pump will likely have a flow rate set
        already, so it is likely okay for setting the flow rate to not be a
        hard prerequisite for this method.
        """

    @abstractmethod
    @sila.UnobservableCommand()
    def stop(self) -> None:
        """Stops the flow of the pump."""

    # TODO: Potential candidate for observability
    @abstractmethod
    @sila.UnobservableProperty()
    def is_running(self) -> bool:
        """Checks if the pump is currently running.

        Use :meth:``start()`` and :meth:``stop()`` to control pump operation.

        :return: _description_
        :rtype: bool
        """

    @abstractmethod
    @sila.UnobservableCommand()
    def set_flow_rate(self, value: float) -> None:
        """Sets the flow rate for the pump.

        :raises InvalidFlowRate: Flow rate was outside of acceptable operating
            range (usually [0, :meth:``get_max_flow_rate()``])

        :param value: Flow rate value
        :type value: float
        """

    @abstractmethod
    @sila.UnobservableProperty()
    def get_flow_rate(self) -> float:
        """Gets the current flow rate setting of the pump.

        :return: Currently set flow rate for the pump
        :rtype: float
        """

    # TODO: I think this makes sense as a potential observable property
    @abstractmethod
    @sila.UnobservableProperty()
    def get_volume_dispensed(self) -> float:
        """Gets the current volume dispensed since the last reset.

        :return: Volume dispensed
        :rtype: float
        """

    @abstractmethod
    @sila.UnobservableProperty()
    def get_max_flow_rate(self) -> float:
        """Gets the maximum allowable flow rate of the pump.

        :return: Maximum allowable flow rate of the pump
        :rtype: float
        """
