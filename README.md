# Python-4-Automation

<h1 align="center">EC2 Server Management Script & More</h1>
<p align="center">
  <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/Python-3.x-blue.svg" alt="Python Version"></a>
  <a href="https://boto3.amazonaws.com/v1/documentation/api/latest/index.html"><img src="https://img.shields.io/badge/AWS-Boto3-yellow.svg" alt="AWS Boto3 Library"></a>
</p>

<p align="center">Automate the management of your EC2 servers with ease!</p>

# Overview
This repository show cases the use of the Python programming language to automate tasks in the field of DevOps.It employs the use of AWS Boto3 SDK for Python.

As a strategy, I demonstrate how the Python program can be improved upon and made more robust and dynamic based on its use case.
These Python scripts automates the management of EC2 servers in AWS, providing an efficient way to stop instances based on specific tag values. Whether you're looking to save costs by stopping idle instances or streamline resource management, this script has you covered.

# Functionality
*The script performs the following tasks:*

__Read Tag Values:__ It reads tag values from a file named tags.txt, which should be located in the same directory as the script. Each line in the file represents a tag value for identifying EC2 instances to stop.

__Retrieve Instance Information:__ It retrieves information about all existing EC2 instances in the specified AWS region (us-east-1 in this case). It extracts instance IDs from the response for further processing.

__Identify Instances to Stop:__ It matches the tag values read from the file with the instances' tag values obtained from AWS. If a match is found and the instance is not already stopped, it adds the instance ID to a list of instances to stop.

__Stop Instances:__ It stops the instances identified in the previous step using the stop_instances API call. It continuously checks the state of the instances until they are stopped, ensuring that the script waits until the instances are successfully stopped before proceeding.

**Error Handling:**
The script incorporates error handling to gracefully handle potential issues that may arise during execution. It includes:

*File Not Found:* If the tags.txt file is not found in the specified directory, the script logs an error message and continues execution.

*Key Errors:* If the required keys are not found in the EC2 response (e.g., Reservations or Instances), the script logs an error message and continues execution.

*Other Exceptions:* Any other exceptions encountered during file reading, instance processing, or instance stopping are logged, allowing the script to continue execution without crashing.

# Requirements
1. **Python 3.x**
2. **boto3 library for AWS interactions (install via pip install boto3)**

# Usage
1. Ensure that you have Python 3.x installed on your system.
2. Install the boto3 library using: pip install boto3.
3. Create a file named tags.txt in the same directory as the script. Each line in the file should contain a tag value for identifying EC2 instances.
4. Run the script using *[ python script.py ]*

 # Contributions
*Contributions are welcome! If you find any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.*  

# Email Address
*samuelhaddison71@gmail.com*
