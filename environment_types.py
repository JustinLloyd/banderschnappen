import copy
import json
import random
from itertools import combinations

import networkx as nx

from climate_type import ClimateData
from location_types import Location
from zone_types import ZoneData, Zone


class EnvironmentData:
    def __init__(self, name: str = None, minimum_level: int = 0, maximum_level: int = 0, zones: [ZoneData] = None, climates: [ClimateData] = None):
        self.name = name
        self.minimum_level = minimum_level
        self.maximum_level = maximum_level
        self.zones = zones
        self.climates = climates

    def __repr__(self):
        return f"{self.name} {self.minimum_level} {self.maximum_level} {self.zones} {self.climates}"

    def validate(self):
        if not self.name:
            raise ValueError("Each environment must have a name, and it cannot be empty.")

        if not isinstance(self.minimum_level, int) or not isinstance(self.maximum_level, int):
            raise ValueError("Minimum and maximum level must be integers.")

        if self.minimum_level >= self.maximum_level:
            raise ValueError("Minimum level must be less than maximum level.")

        if not self.zones or not isinstance(self.zones, list):
            raise ValueError("Each environment must have a zones list, and it cannot be empty.")

        if len(self.zones) < 2:
            raise ValueError(f"The {self.name} environment must have at least two zones.")

        for zone in self.zones:
            if not isinstance(zone, ZoneData):
                raise ValueError(f"Each zone must be a ZoneData object. {zone} is not a ZoneData object.")
            zone.validate()

        if not self.climates or not isinstance(self.climates, list):
            raise ValueError("Each environment must have a climates list, and it cannot be empty.")

        # TODO verify there are no duplicate climates


class Environment:
    def __init__(self, data: EnvironmentData = None):
        self.name = data.name
        self.minimum_level = data.minimum_level
        self.maximum_level = data.maximum_level
        self.possible_zones = copy.deepcopy(data.zones)
        self.possible_climates = copy.deepcopy(data.climates)
        self.zones = []
        self.climate = None
        self.level = 0
        self.description = ''
        self.graph = nx.Graph()

    def select_random_zones(self):
        number_of_zones = random.randint(max(1, len(self.possible_zones) // 2), len(self.possible_zones))
        # always take the first zone, that's the reason this environment exists
        selected_zones = [self.possible_zones[0]] + random.sample(self.possible_zones[1:], number_of_zones - 1)

        for zone_data in selected_zones:
            zone = Zone(zone_data)
            zone.depth = random.randint(1, len(selected_zones))
            zone.randomize_zone()
            self.zones.append(zone)

    def build_environment(self):
        self.select_random_zones()
        self._build_graph()
        self._connect_nodes_within_zones()
        self._remove_zones()
        self._connect_all_zones()

    def __str__(self):
        return f"{self.name}"

    def _build_graph(self):
        min_locations = 3
        max_locations = 6

        if not self.zones or len(self.zones) == 0:
            raise ValueError("No zones provided")

        # n_zones=len(zone_list)
        # if n_zones==0:
        #     raise ValueError("No zones provided")

        # print(n_zones,len(zone_list))

        for zone in self.zones:
            # zone_depth = random.randint(1, n_zones)

            self.graph.add_node(zone.constructed_name(), type="zone", zone=zone)

            # # Generate locations for this zone
            # min_locations = zone.minimum_locations_to_use
            # n_locations = random.randint(min_locations, max_locations)
            for location in zone.locations:
                # loc_name = f"{zone.name}_{location.name}_{location.depth}"
                self.graph.add_node(location.constructed_name(), type="location", location=location)
                self.graph.add_edge(zone.constructed_name(), location.constructed_name())

            # Interconnect locations in the same zone

            # locations = [n for n in self.graph.nodes if self.graph.nodes[n]['type'] == 'location' and self.graph.nodes[n]['location'].zone.name == zone.name]
            for zone_location in zone.locations:
                # Find the locations that satisfy the depth rule
                # NOTE this could be a list comprehension, but that makes the code hard to follow and debug
                # so instead, we use a for loop and keep the logic simple
                # don't be tempted to change this to make it more "pythonic"
                locs_in_depth_range = []
                for possible_location in zone.locations:
                    if possible_location == zone_location:
                        continue
                    # if the location is not within depth range, ignore it
                    if abs(possible_location.depth - zone_location.depth) > 1:
                        continue
                    locs_in_depth_range.append(possible_location)

                # Select a random number (between 1 and the number of locations in depth range) of locations to connect
                # if there are no locations in the depth range, skip this location
                if not locs_in_depth_range:
                    continue
                # select a few locations to connect, not too many, not too few
                num_locs_to_connect = random.randint(1, max(1, len(locs_in_depth_range) // 2))
                locs_to_connect = random.sample(locs_in_depth_range, num_locs_to_connect)
                # and now we connect up the locations
                for location in locs_to_connect:
                    self.graph.add_edge(zone.constructed_name(), location.constructed_name())

        # Create connections between locations in different zones
        for zone_i, zone_j in combinations(self.zones, 2):
            if abs(zone_i.depth - zone_j.depth) > 1:
                continue

            # Get locations in each zone
            locs_zone_i = zone_i.locations  # [n for n in self.graph.neighbors(zone_list[zone_i])]
            locs_zone_j = zone_j.locations  # [n for n in self.graph.neighbors(zone_list[zone_j])]

            # # Get locations in the appropriate depth range
            # locs_zone_i_in_range = [n for n in  if
            #                         abs(self.graph.nodes[n]['depth'] - self.graph.nodes[zone_list[zone_i]]['depth']) <= 1]
            # locs_zone_j_in_range = [n for n in locs_zone_j if
            #                         abs(self.graph.nodes[n]['depth'] - self.graph.nodes[zone_list[zone_j]]['depth']) <= 1]

            # Make the connections only if there are locations in range in both zones
            if locs_zone_i and locs_zone_j:
                # Determine the number of connections to make
                n_connections = random.randint(1, min(len(locs_zone_i), len(locs_zone_j)))

                # Make the connections
                for _ in range(n_connections):
                    loc1 = random.choice(locs_zone_i)
                    loc2 = random.choice(locs_zone_j)

                    self.graph.add_edge(loc1.constructed_name(), loc2.constructed_name())

    # remove the zones, we no longer need to know about them, we're just interested in the locations
    def _remove_zones(self):
        zones = [n for n in self.graph.nodes if self.graph.nodes[n]['type'] == 'zone']
        for zone in zones:
            self.graph.remove_node(zone)

    def _connect_nodes_within_zones(self):
        zones = [n for n in self.graph.nodes if self.graph.nodes[n]['type'] == 'zone']

        for zone in zones:
            # Get locations in the zone
            locs_zone = [n for n in self.graph.neighbors(zone)]

            # Find the disconnected components within the zone
            subgraph = self.graph.subgraph(locs_zone)
            components = list(nx.connected_components(subgraph))

            # If there is more than one component, create connections to make the graph connected
            while len(components) > 1:
                # Randomly select two components and a node from each to create a connection
                comp1, comp2 = random.sample(components, 2)
                node1 = random.choice(list(comp1))
                node2 = random.choice(list(comp2))
                self.graph.add_edge(node1, node2)

                # Recompute the connected components
                components = list(nx.connected_components(self.graph.subgraph(locs_zone)))

    def _connect_all_zones(self):
        zones = [n for n in self.graph.nodes if self.graph.nodes[n]['type'] == 'zone']

        # Now we need to make sure that all zones are connected.
        # For this we can use the connected_components function again, but this time on the whole graph.
        components = list(nx.connected_components(self.graph))

        while len(components) > 1:
            comp1, comp2 = random.sample(components, 2)
            node1 = random.choice(list(comp1))
            node2 = random.choice(list(comp2))
            self.graph.add_edge(node1, node2)

            components = list(nx.connected_components(self.graph))

    @staticmethod
    def custom_serializer(obj):
        if isinstance(obj, Location) or isinstance(obj, Zone):
            return obj.to_dict()
        raise TypeError(f"Type {type(obj)} not serializable")

    def to_dict(self):
        data = nx.node_link_data(self.graph)
        graph_data = json.loads(json.dumps(data, default=Environment.custom_serializer))
        return {
            'name': self.name,
            'graph': graph_data,
            'zones': [zone.to_dict() for zone in self.zones],
            'minimum_level': self.minimum_level,
            'maximum_level': self.maximum_level,
            'possible_zones': [zone.to_dict() for zone in self.possible_zones],
            'possible_climates': [climate.to_dict() for climate in self.possible_climates],
            'climate': self.climate.to_dict(),
            'level': self.level,
            'description': self.description,
        }


