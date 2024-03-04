# annotations are import from __future so that the delayed type checking does
# not have to use "Collector" but can just use Collector.
# from typing import Dict, List, Union

# from typing import TYPE_CHECKING

# if TYPE_CHECKING:
#     from .collector import Collector

# CollectorsType = Union[Counter, Gauge, Histogram, Summary]


# class Registry:
#     """This class implements a container to hold metrics collectors.

#     Collectors in the registry must comply with the Collector interface
#     which means that they inherit from the base Collector object and implement
#     a no-argument method called 'get_all' that returns a list of Metric
#     instance objects.
#     """

#     def __init__(self) -> None:
#         self.collectors = {}  # type: Dict[str, Collector]

#     def register(self, collector: "Collector") -> None:
#         """Register a collector into the container.

#         The registry provides a container that can be used to access all
#         metrics when exposing them into a specific format.

#         :param collector: A collector to register in the registry.

#         :raises: ValueError if collector is already registered.
#         """
#         if collector.name in self.collectors:
#             raise ValueError(f"A collector for {collector.name} is already registered")

#         self.collectors[collector.name] = collector

#     def deregister(self, name: str) -> None:
#         """Deregister a collector.

#         This will stop the collector metrics from being emitted.

#         :param name: The name of the collector to deregister.

#         :raises: KeyError if collector is not already registered.
#         """
#         del self.collectors[name]

#     def get(self, name: str) -> "Collector":
#         """Get a collector by name.

#         :param name: The name of the collector to fetch.

#         :raises: KeyError if collector is not found.
#         """
#         return self.collectors[name]

#     def get_all(self) -> List["Collector"]:
#         """Return a list of all collectors"""
#         return list(self.collectors.values())

#     def clear(self):
#         """ Clear all registered collectors.

#         This function is mainly of use in tests to reset the default registry
#         which may be used in multiple tests.
#         """
#         for name in list(self.collectors.keys()):
#             self.deregister(name)

# REGISTRY = Registry()
