# LeKiwi_ROS

A ROS (Robot Operating System) project for arm controller and arm description packages.

## Technology Stack

- **Python** (87.3%) - Core logic and scripting
- **CMake** (12.7%) - Build system configuration

## Prerequisites

- ROS (Robot Operating System) installed
- Python 3.6+
- CMake 3.0+
- Colcon build tool

## Getting Started

### Installation

1. Clone the repository into your ROS workspace:
   ```bash
   cd ~/lekiwi_ws/src
   git clone https://github.com/mohmedatwa/LeKiwi_ROS.git
   cd ..
   ```

2. Build the project with colcon:
   ```bash
   colcon build
   ```

3. Source the setup file:
   ```bash
   source install/setup.bash
   ```

## Project Structure

```
LeKiwi_ROS/
├── lekiwi_controller/      # ARM controller package
│   ��── [Controller implementation and configurations]
├── lekiwi_description/     # ARM description package
│   └── [Robot URDF and description files]
├── LICENSE                 # Apache 2.0 License
└── README.md              # This file
```

## Packages

### lekiwi_controller
Handles arm controller functionality and control logic.

### lekiwi_description
Contains the robot description files (URDF) and related configuration for the arm.

## Usage

[Add specific usage instructions here]

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Resources

- [ROS Documentation](http://wiki.ros.org/)
- [Colcon Documentation](https://colcon.readthedocs.io/)
- [Python ROS Tutorials](http://wiki.ros.org/ROS/Tutorials)
