import pandas as pd
from typing import Dict, List
from io import BytesIO


def process_telemetry_csv(file_content: bytes) -> Dict[str, any]:
    """
    Process CSV telemetry data and extract basic information.
    
    Args:
        file_content: Raw bytes of the CSV file
        
    Returns:
        Dictionary with number of samples and list of available channels
    """
    df = pd.read_csv(BytesIO(file_content))
    
    num_samples = len(df)
    channels = df.columns.tolist()
    
    return {
        "samples": num_samples,
        "channels": channels
    }
