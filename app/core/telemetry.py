import pandas as pd
from typing import Dict, List, Any
from io import BytesIO


def process_telemetry_csv(file_content: bytes) -> Dict[str, Any]:
    """
    Process CSV telemetry data and extract basic information.
    
    Args:
        file_content: Raw bytes of the CSV file
        
    Returns:
        Dictionary with number of samples and list of available channels
        
    Raises:
        pd.errors.EmptyDataError: If the CSV file is empty
        pd.errors.ParserError: If the CSV file is malformed
    """
    try:
        df = pd.read_csv(BytesIO(file_content))
    except pd.errors.EmptyDataError:
        raise ValueError("CSV file is empty")
    except pd.errors.ParserError as e:
        raise ValueError(f"CSV file is malformed: {str(e)}")
    
    num_samples = len(df)
    channels = df.columns.tolist()
    
    return {
        "samples": num_samples,
        "channels": channels
    }
