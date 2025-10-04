import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log',  # Log messages will be written to app.log
    filemode='a'         # Append mode
)

def main():
    logging.info("Application started.")
    try:
        # Your application logic here
        logging.info("Running main logic.")
        # Example: simulate a warning
        logging.warning("This is a warning message.")
        # Example: simulate an error
        # raise ValueError("An example error.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        logging.info("Application finished.")

if __name__ == "__main__":
    main()