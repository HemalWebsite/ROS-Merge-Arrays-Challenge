# ROS-Merge-Arrays-Challenge

This repository contains the solution to the Wisconsin Autonomous ROS Coding Challenge. The challenge required the creation of a ROS 2 node that merges two sorted integer arrays from different topics into a single, sorted array.

## Project Structure

The files and folders in this repository are part of the `merge_arrays` ROS 2 package. The file structure is shown below:

```
├── README.md
├── src
│   └── merge_arrays_node.py
├── CmakeLists.txt
├── package.xml
├── setup.py
```

  * `src/merge_arrays_node.py`: The Python script for the ROS 2 node.
  * `CmakeLists.txt` and `package.xml`: Standard ROS 2 configuration files.
  * `setup.py`: The Python-specific build file.

**Note on Repository Structure**: Due to an issue with RAM allocation in the Ubuntu virtual machine, the parent folder was not added to the repository. The folders and files are at the root level of this repository, mirroring the local file structure as seen in the photo provided.

-----

## Challenge Description

The objective was to design a node, **`merge_arrays_node`**, in a package named **`merge_arrays`**.

The node subscribes to two ROS topics:

  * `/input/array1` (Type: `std_msgs/Int32MultiArray`, Content: a sorted `Int32` array)
  * `/input/array2` (Type: `std_msgs/Int32MultiArray`, Content: a sorted `Int32` array)

The node merges these two arrays into a single, sorted array and publishes the result to the `/output/array` topic (Type: `std_msgs/Int32MultiArray`).

**Example**: Given `[1 4 8 12 26]` and `[3 9 18 20 30]`, the node should publish `[1 3 4 8 9 12 18 20 26 30]`.

-----

## Submission Specifications

  * The node is written in **Python**.
  * The package name is **`merge_arrays`** and the node name is **`merge_arrays_node`**.
  * The node will be evaluated with the command `ros2 run merge_arrays merge_arrays_node`.
  * No non-ROS dependencies were used.
  * The full package is available in this public GitHub repository.

-----

## How to Build and Run

1.  Clone this repository into your ROS 2 workspace's `src` directory.
    ```bash
    cd <your_ros2_workspace>/src
    git clone [repository-url]
    ```
2.  Navigate to the root of your workspace and build the package.
    ```bash
    cd <your_ros2_workspace>
    colcon build --packages-select merge_arrays
    ```
3.  Source your workspace to make the package available.
    ```bash
    source install/setup.bash
    ```
4.  Run the node.
    ```bash
    ros2 run merge_arrays merge_arrays_node
    ```
