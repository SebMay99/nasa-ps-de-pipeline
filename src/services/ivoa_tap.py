# IVOA TAP Service for NASA Exoplanet Archive
import pyvo as vo
import pandas as pd

def fetch_raw_data():
    # Define the TAP service URL for NASA Exoplanet Archive
    tap_service_url = "https://exoplanetarchive.ipac.caltech.edu/TAP"

    # Create a TAP service object
    tap_service = vo.dal.TAPService(tap_service_url)

    # Define the ADQL query to fetch exoplanet data
    adql_query = """
        SELECT TOP 5
        pl_name, pl_orbper, pl_rade, pl_bmasse, st_teff, st_rad
        FROM ps
        WHERE pl_orbper IS NOT NULL AND pl_rade IS NOT NULL
        """

    # Execute the query and fetch results
    try:
        result = tap_service.search(adql_query)
        df = result.to_table().to_pandas()
        print("Fetched data successfully:")
        print(df)
    except Exception as e:
        print(f"Error occurred while fetching data: {e}")