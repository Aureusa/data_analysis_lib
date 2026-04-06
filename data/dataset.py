import pandas as pd
from typing import List, Dict, Any


class DataFrame:
    def __init__(self, data: Any) -> None:
        """
        Initialize a DataFrame wrapper.
        
        :param data: Data to initialize the DataFrame
        :type data: Any
        :return: None
        :rtype: None
        """
        self.df = pd.DataFrame(data)

    def __repr__(self) -> str:
        return self.df.__repr__()
    
    def __str__(self) -> str:
        return self.df.__str__()

    @property
    def shape(self) -> tuple:
        """
        Get the shape of the DataFrame.
        
        :return: Tuple of (rows, columns)
        :rtype: tuple
        """
        return self.df.shape
    
    @property
    def columns(self) -> List[str]:
        """
        Get column names as a list.
        
        :return: List of column names
        :rtype: List[str]
        """
        return self.df.columns.tolist()
    
    @property
    def dtypes(self) -> Dict[str, Any]:
        """
        Get data types of each column.
        
        :return: Dictionary mapping column names to data types
        :rtype: Dict[str, Any]
        """
        return self.df.dtypes.to_dict()
    
    def head(self, n: int = 5) -> "DataFrame":
        """
        Get the first n rows.
        
        :param n: Number of rows to return
        :type n: int
        :return: New DataFrame with first n rows
        :rtype: DataFrame
        """
        return DataFrame(self.df.head(n))
    
    def tail(self, n: int = 5) -> "DataFrame":
        """
        Get the last n rows.
        
        :param n: Number of rows to return
        :type n: int
        :return: New DataFrame with last n rows
        :rtype: DataFrame
        """
        return DataFrame(self.df.tail(n))

    def select(self, columns: List[str]) -> "DataFrame":
        """
        Select specific columns.
        
        :param columns: Column names to select
        :type columns: List[str]
        :return: New DataFrame with selected columns
        :rtype: DataFrame
        """
        return DataFrame(self.df[columns])
    
    def to_numpy(self) -> Any:
        """
        Convert DataFrame to numpy array.
        
        :return: Numpy array representation
        :rtype: Any
        """
        return self.df.values
    
    def from_csv(self, file_path: str) -> None:
        """
        Load DataFrame from CSV file.
        
        :param file_path: Path to CSV file
        :type file_path: str
        :return: None
        :rtype: None
        """
        self.df = pd.read_csv(file_path)

    def to_csv(self, file_path: str) -> None:
        """
        Save DataFrame to CSV file.
        
        :param file_path: Path to save CSV
        :type file_path: str
        :return: None
        :rtype: None
        """
        self.df.to_csv(file_path, index=False)
        