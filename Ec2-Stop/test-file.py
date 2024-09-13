import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

def main():
    try:
        # Determine the directory where the script is located
        # script_dir = os.path.dirname(os.path.realpath(__file__))
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Construct the full path to the 'tags.txt' file
        file_path = os.path.join(script_dir, "tags.txt")
        
        # Log the file path
        logging.info(f"Looking for the file at: {file_path}")
        
        # Check if the file exists before attempting to read
        if not os.path.exists(file_path):
           raise FileNotFoundError(f"File '{file_path}' not found.")
        
        # Read the content of the file
        with open(file_path, 'r') as file:
            for tag in file.readlines():
                tag_value = tag.strip()
                print(tag_value)
            logging.info("Successfully read the file content.")
    
    except FileNotFoundError as fnf_error:
        logging.error(fnf_error)
    except Exception as e:
        logging.error(f"An error occurred while reading the file: {str(e)}")

if __name__ == "__main__":
    main()

