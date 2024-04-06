# Travel-Desk

This Python script implements a transport management system that efficiently handles vehicle trips and bookings between different locations. It provides functionalities for adding trips, booking trips, and querying available trips based on various parameters such as location, departure time, and destination. The system utilizes data structures like binary search trees and classes to organize and manage vehicle and trip data.

# Features:
**Vehicle Class:** Represents a vehicle with attributes for vehicle number, seating capacity, and associated trips. It includes methods for accessing and modifying vehicle details.</br>
**Trip Class:** Defines a trip with attributes for the vehicle, pick-up location, drop location, departure time, and booked seats. It provides methods for managing trip information.</br>
**BinaryTreeNode Class:** Implements a node for a binary search tree with attributes for left and right pointers, parent pointer, departure time, and trip node pointer. It includes methods for accessing and modifying node details.</br>
**TransportService Class:** Represents a transport service for a specific location with a binary search tree to organize trips by departure time. It includes methods for managing service details and adding trips.</br>
**BinarySearchTree Class:** Implements a binary search tree data structure with methods for finding minimum and maximum value nodes, searching for nodes with specific keys, and finding successors and predecessors.</br>
**Location Class:** Represents a location with attributes for location name, associated transport services, and trips. It includes methods for accessing and modifying location details.</br>
**TravelDesk Class:** Orchestrates the transport management system by managing vehicles, locations, and trips. It includes methods for adding trips, booking trips, and querying available trips.</br>
**File Input:** The script reads commands from an input file (iteration.txt) to add trips, show trips by destination, and book trips.</br>

# **How to Use:**
Ensure you have Python installed on your system.</br>
Download the script (transport_management.py) to your local machine.</br>
Prepare an input file (iteration.txt) containing commands for adding trips, showing trips by destination, and booking trips. Refer to the sample commands in the code comments for the required format.</br>
The script will read the commands from the input file, execute them, and display the results accordingly.

# **Note:**
This script provides a basic implementation of a transport management system and can be extended for additional features such as user authentication, real-time updates, and error handling.</br>
Ensure the input file (iteration.txt) follows the correct format for commands to be executed properly.</br>
For any issues or suggestions, please feel free to raise them in the repository.
