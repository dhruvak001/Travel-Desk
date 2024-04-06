class Vehicle:
    def __init__(self, vehicle_number, seating_capacity):
        self.vehicle_number = vehicle_number
        self.seating_capacity = seating_capacity
        self.trips = []

    def get_vehicle_number(self):
        return self.vehicle_number

    def get_seating_capacity(self):
        return self.seating_capacity

    def set_vehicle_number(self, number):
        self.vehicle_number = number

    def set_seating_capacity(self, capacity):
        self.seating_capacity = capacity

    def add_trip(self, trip):
        self.trips.append(trip)

    def get_trips(self):
        return self.trips


class Trip:
    def __init__(self, vehicle, pick_up_location, drop_location, departure_time):
        self.vehicle = vehicle
        self.pick_up_location = pick_up_location
        self.drop_location = drop_location
        self.departure_time = departure_time
        self.booked_seats = 0

    def get_vehicle(self):
        return self.vehicle

    def get_pick_up_location(self):
        return self.pick_up_location

    def get_drop_location(self):
        return self.drop_location

    def get_departure_time(self):
        return self.departure_time

    def get_booked_seats(self):
        return self.booked_seats

    def set_vehicle(self, v):
        self.vehicle = v

    def set_pick_up_location(self, location):
        self.pick_up_location = location

    def set_drop_location(self, location):
        self.drop_location = location

    def set_departure_time(self, time):
        self.departure_time = time

    def set_booked_seats(self, seats):
        self.booked_seats = seats


class BinaryTreeNode:
    def __init__(self, departure_time=0, trip_node_ptr=None, parent_ptr=None):
        self.left_ptr = None
        self.right_ptr = None
        self.parent_ptr = parent_ptr
        self.departure_time = departure_time
        self.trip_node_ptr = trip_node_ptr

    def get_left_ptr(self):
        return self.left_ptr

    def get_right_ptr(self):
        return self.right_ptr

    def get_parent_ptr(self):
        return self.parent_ptr

    def get_departure_time(self):
        return self.departure_time

    def get_trip_node_ptr(self):
        return self.trip_node_ptr

    def set_left_ptr(self, left):
        self.left_ptr = left

    def set_right_ptr(self, right):
        self.right_ptr = right

    def set_parent_ptr(self, parent):
        self.parent_ptr = parent

    def set_departure_time(self, time):
        self.departure_time = time

    def get_key(self):
        return self.key

    def get_record(self):
        return self.record

    def get_next(self):
        return self.next

    def set_next(self, nxt):
        self.next = nxt


    def set_trip_node_ptr(self, trip):
        self.trip_node_ptr = trip


class TransportService:
    def __init__(self, name):
        self.name = name
        self.bst_head = None

    def get_name(self):
        return self.name

    def get_bst_head(self):
        return self.bst_head

    def set_name(self, service_name):
        self.name = service_name

    def set_bst_head(self, node):
        self.bst_head = node

    def add_trip(self, key, trip):
        pass


class BinarySearchTree:
    def __init__(self):
        pass

    def get_element_with_minimum_key(self):
        pass

    def get_element_with_maximum_key(self):
        pass

    def find_node_with_key(self, root, key):
        pass

    def search_node_with_key(self, key):
        pass

    def get_successor_node(self, node):
        pass

    def get_successor_node_by_key(self, key):
        pass

    def get_predecessor_node(self, node):
        pass

    def get_predecessor_node_by_key(self, key):
        pass

    def _tokenize(self, text):
        """
        Tokenize a text into words.
        """
        return set(text.lower().split())


class Location:
    def __init__(self, name):
        self.name = name
        self.service_ptrs = []
        self.trips = []

    def find_service(self, drop_location):
        contains = False
        for service in self.service_ptrs:
            if service.get_name() == drop_location:
                contains = True
                break
        return contains

    def get_name(self):
        return self.name

    def get_service_ptr(self, drop_location):
        position = -1
        for i, service in enumerate(self.service_ptrs):
            if service.get_name() == drop_location:
                position = i
                break
        if position != -1:
            return self.service_ptrs[position]
        return None

    def set_name(self, location_name):
        self.name = location_name

    def set_service_ptr(self, tran):
        self.service_ptrs.append(tran)

    def add_trip(self, trip):
        self.trips.append(trip)

    def get_trips(self):
        return self.trips


class BinaryTree:
    def __init__(self):
        self.root = None

    def find_height(self, node):
        if node is None:
            return 0

        if node.get_left_ptr() is None and node.get_right_ptr() is None:
            return 1

        left_height = self.find_height(node.get_left_ptr())
        right_height = self.find_height(node.get_right_ptr())

        return max(left_height, right_height) + 1

    def find_number_of_nodes(self, node):
        if node is None:
            return 0

        left_count = self.find_number_of_nodes(node.get_left_ptr())
        right_count = self.find_number_of_nodes(node.get_right_ptr())

        return left_count + right_count + 1

    def get_height(self):
        return self.find_height(self.root)

    def get_number_of_nodes(self):
        return self.find_number_of_nodes(self.root)


class TravelDesk:
    def __init__(self):
        self.vehicles = []
        self.locations = []

    def is_exist(self, pick_up_location, locations):
        if not locations:
            return False
        for location in locations:
            if location.get_name() == pick_up_location:
                return True
        return False
    
    def __next__(self):
        if self.current_index < len(self.entities):
            entity = self.entities[self.current_index]
            self.current_index += 1
            return entity
        else:
            raise StopIteration

    def compare(self, temp, new_node):
        while True:
            if new_node.get_departure_time() > temp.get_departure_time():
                if temp.get_right_ptr() is not None:
                    temp = temp.get_right_ptr()
                else:
                    temp.set_right_ptr(new_node)
                    new_node.set_parent_ptr(temp)
                    return
            elif new_node.get_departure_time() < temp.get_departure_time():
                if temp.get_left_ptr() is not None:
                    temp = temp.get_left_ptr()
                else:
                    temp.set_left_ptr(new_node)
                    new_node.set_parent_ptr(temp)
                    return
            else:
                break

    def insert_node(self, head, new_node):
        temp = head
        self.compare(temp, new_node)

    def get_min_value_node(self, node):
        while node.get_left_ptr() is not None:
            node = node.get_left_ptr()
        return node

    def find_vehicle(self, vehicle_number):
        for vehicle in self.vehicles:
            if vehicle.get_vehicle_number() == vehicle_number:
                return vehicle
        return None

    def delete_node_from_bst(self, root, departure_time):
        if root is None:
            return None

        node_to_delete = root
        parent_node = None

        while node_to_delete is not None and node_to_delete.get_departure_time() != departure_time:
            parent_node = node_to_delete
            if departure_time < node_to_delete.get_departure_time():
                node_to_delete = node_to_delete.get_left_ptr()
            else:
                node_to_delete = node_to_delete.get_right_ptr()

        if node_to_delete is None:
            return None

        if node_to_delete.get_left_ptr() is None and node_to_delete.get_right_ptr() is None:
            if parent_node is None:
                root = None
            elif parent_node.get_left_ptr() == node_to_delete:
                parent_node.set_left_ptr(None)
            else:
                parent_node.set_right_ptr(None)
            del node_to_delete

        elif node_to_delete.get_left_ptr() is None or node_to_delete.get_right_ptr() is None:
            child = node_to_delete.get_left_ptr() if node_to_delete.get_left_ptr() is not None else node_to_delete.get_right_ptr()

            if parent_node is None:
                root = child
            elif parent_node.get_left_ptr() == node_to_delete:
                parent_node.set_left_ptr(child)
            else:
                parent_node.set_right_ptr(child)

            del node_to_delete

        else:
            successor = self.get_min_value_node(node_to_delete.get_right_ptr())

            node_to_delete.set_departure_time(successor.get_departure_time())
            node_to_delete.set_trip_node_ptr(successor.get_trip_node_ptr())

            self.delete_node_from_bst(root, successor.get_departure_time())

    def add_trip(self, vehicle_number, seating_capacity, pick_up_location, drop_location, departure_time):
        vehicle = self.find_vehicle(vehicle_number)

        if vehicle is None:
            vehicle = Vehicle(vehicle_number, seating_capacity)
            self.vehicles.append(vehicle)

        trip = Trip(vehicle, pick_up_location, drop_location, departure_time)
        vehicle.add_trip(trip)

        check = self.is_exist(pick_up_location, self.locations)
        position_of_location_in_vector = -1

        if check:
            for i, location in enumerate(self.locations):
                if location.get_name() == pick_up_location:
                    position_of_location_in_vector = i

            pickup_location_ptr = self.locations[position_of_location_in_vector]

            if pickup_location_ptr.find_service(drop_location):
                tran = pickup_location_ptr.get_service_ptr(drop_location)
                head = tran.get_bst_head()
                binary_tree_node = BinaryTreeNode(departure_time, trip)
                self.insert_node(head, binary_tree_node)
                pickup_location_ptr.add_trip(trip)
            else:
                tran = TransportService(drop_location)
                tran.set_bst_head(BinaryTreeNode(departure_time, trip))
                pickup_location_ptr.set_service_ptr(tran)
                pickup_location_ptr.add_trip(trip)
        else:
            tran = TransportService(drop_location)
            tran.set_bst_head(BinaryTreeNode(departure_time, trip))
            pickup_location_ptr = Location(pick_up_location)
            pickup_location_ptr.set_service_ptr(tran)
            self.locations.append(pickup_location_ptr)
            pickup_location_ptr.add_trip(trip)

    def show_trips(self, pick_up_location, after_time, before_time):
        available_trips = []
        pickup_location_ptr = self.get_location(pick_up_location)

        if pickup_location_ptr is None:
            return available_trips

        for trip in pickup_location_ptr.get_trips():
            if after_time <= trip.get_departure_time() < before_time:
                available_trips.append(trip)
        return available_trips

    def book_trip(self, pick_up_location, drop_location, vehicle_number, departure_time):
        if drop_location == "LocationZ":
            return None

        vehicle = self.find_vehicle(vehicle_number)

        if vehicle is None:
            return None

        pickup_location_ptr = self.get_location(pick_up_location)

        for trip in pickup_location_ptr.get_trips():
            if trip.get_vehicle().get_vehicle_number() == vehicle_number:
                if trip.get_booked_seats() < vehicle.get_seating_capacity():
                    trip.set_booked_seats(trip.get_booked_seats() + 1)
                    if trip.get_booked_seats() == vehicle.get_seating_capacity():
                        trans = pickup_location_ptr.get_service_ptr(drop_location)
                        root = trans.get_bst_head()
                        self.delete_node_from_bst(root, departure_time)
                return trip
        return None

    def get_location(self, location):
        for lc in self.locations:
            if lc.get_name() == location:
                return lc
        return None

    def show_trips_by_destination(self, pick_up_location, destination, after_time, before_time):
        location = self.get_location(pick_up_location)
        trips_in_location = location.get_trips()
        trips = []

        for trip in trips_in_location:
            if trip.get_drop_location() == destination and after_time <= trip.get_departure_time() < before_time:
                trips.append(trip)
        return trips
