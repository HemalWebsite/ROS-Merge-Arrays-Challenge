import rclpy
from std_msgs.msg import Int32MultiArray

#initallizes rclpy
rclpy.init()

#global variables
publisher = None
array1_data = None
array2_data = None


#callback functions
def callback1(msg):
    global array1_data
    array1_data = msg.data
    print("Received array1")
    check_and_publish()

def callback2(msg):
    global array2_data
    array2_data = msg.data
    print("Received array2")
    check_and_publish()


#core nodes+subscriber+publishers
node = rclpy.create_node('merge_arrays_node')
publisher1 = node.create_publisher(Int32MultiArray, '/output/array', 10)
subscriber1 = node.create_subscription(Int32MultiArray,'/input/array1',callback1,10)
subscriber2 = node.create_subscription(Int32MultiArray,'/input/array2',callback2,10)

#merge_sorted_arrays
def merge_sorted_arrays(arr1, arr2):
    
    result = []
    p1 = 0  
    p2 = 0  

    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] < arr2[p2]:
            result.append(arr1[p1])
            p1 += 1
        else:
            result.append(arr2[p2])
            p2 += 1

   
    while p1 < len(arr1):
        result.append(arr1[p1])
        p1 += 1

    
    while p2 < len(arr2):
        result.append(arr2[p2])
        p2 += 1

    return result

#check and publish
def check_and_publish():
    global array1_data, array2_data, publisher
    if array1_data is not None and array2_data is not None:
        merged_array = merge_sorted_arrays(array1_data, array2_data)
        
        output_msg = Int32MultiArray()
        output_msg.data = merged_array
        
        publisher.publish(output_msg)
        print(f"Published merged array: {merged_array}")
        array1_data = None
        array2_data = None



#spin
rclpy.spin(node)
