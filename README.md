# LeKiwi_ROS

A ROS (Robot Operating System) project combining Python and CMake for robot control and automation.

## Technology Stack

- **Python** (87.3%) - Core logic and scripting
- **CMake** (12.7%) - Build system configuration

## Prerequisites

- ROS (Robot Operating System) installed
- Python 3.6+
- CMake 3.0+
- C++ compiler (for building C++ components if any)

## Getting Started

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mohmedatwa/LeKiwi_ROS.git
   cd LeKiwi_ROS
   ```

2. Build the project:
   ```bash
   mkdir build
   cd build
   cmake ..
   make
   ```

3. Source the ROS setup:
   ```bash
   source /opt/ros/<distro>/setup.bash
   ```

## Project Structure

```
LeKiwi_ROS/
├── CMakeLists.txt
├── package.xml
├── src/
│   └── [Python and C++ source files]
├── launch/
│   └── [ROS launch files]
└── README.md
```

## Usage

[Add specific usage instructions here]

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Resources

- [ROS Documentation](http://wiki.ros.org/)
- [Python ROS Tutorials](http://wiki.ros.org/ROS/Tutorials)
