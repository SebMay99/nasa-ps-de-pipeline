from services.ivoa_tap import fetch_raw_data

# Main loop
if __name__ == "__main__":
    try:
        fetch_raw_data()
    except Exception as e:
        print(f"Error occurred: {e}")