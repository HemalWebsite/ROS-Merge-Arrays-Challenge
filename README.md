#ROS-Merge-Arrays-Challenge
This repository contains the solution to the Wisconsin Autonomous ROS Coding Challenge. The challenge required the creation of a ROS2 node that merges two sorted integer arrays from different topics into a single, sorted array.

##Project Structure
The files and folders in this repository represent the merge_arrays ROS 2 package. The structure of the project is as follows:

├── README.md
├── src
│   └── merge_arrays_node.py
├── CmakeLists.txt
├── package.xml
├── setup.py
src/merge_arrays_node.py: The Python script containing the ROS 2 node that handles the merging logic.

CmakeLists.txt and package.xml: Standard ROS 2 configuration files.

setup.py: The Python-specific build file for the ROS 2 package.

##Note on Repository Structure:

Due to an issue with RAM allocation in the Ubuntu virtual machine, the main repository folder was not committed as the parent. As a result, the src folder, CmakeLists.txt, package.xml, and setup.py are at the root level of this repository, as shown in the screenshot of my local file structure.

##Challenge Description
The objective of this challenge was to create a ROS 2 node, merge_arrays_node, within a package named merge_arrays.

This node subscribes to two topics:

/input/array1 (Type: std_msgs/Int32MultiArray)

/input/array2 (Type: std_msgs/Int32MultiArray)

It then merges the two sorted integer arrays received from these topics into a single sorted array. This merged array is published to the /output/array topic, which also has the type std_msgs/Int32MultiArray.

For example, given [1 4 8 12 26] and [3 9 18 20 30], the node should publish [1 3 4 8 9 12 18 20 26 30].

##Solution
The solution is implemented in Python and follows the provided submission specifications. The node handles the subscription to both input topics and uses a callback function to perform the merging and publishing operations. The logic is designed to be efficient for sorted arrays.

##Prerequisites
Operating System: Ubuntu 22.04 LTS (Jammy Jellyfish)

ROS 2 Distribution: Humble Hawksbill

Python: Version 3.8+

###How to Build and Run
Clone this repository into your ROS 2 workspace src directory.

Bash

cd <your_ros2_workspace>/src
git clone [your-github-repo-url]
Navigate to the root of your workspace and build the package.

Bash

cd <your_ros2_workspace>
colcon build --packages-select merge_arrays
Source your workspace to make the new package available.

Bash

source install/setup.bash
Run the node.

Bash

ros2 run merge_arrays merge_arrays_node
