from services.ivoa_tap import fetch_raw_data

# Main loop
if __name__ == "__main__":
    tap_service_url = "https://exoplanetarchive.ipac.caltech.edu/TAP"
    try:
        raw_data = fetch_raw_data(tap_service_url)
        print(raw_data)
    except Exception as e:
        print(f"Error occurred: {e}")