import pytest

from rxnrover.sila.abf import ExampleControllerBase


def test_example():
    """The ABF should not be able to be instantiated."""
    with pytest.raises(TypeError):
        ExampleControllerBase()


def test_create_concrete_feature():
    """A concrete feature should be able to be instantiated."""

    class ConcreteExample(ExampleControllerBase):
        def action(self) -> int:
            return 0

    feature = ConcreteExample()

    assert feature.action() == 0
