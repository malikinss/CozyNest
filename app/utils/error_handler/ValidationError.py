class ValidationError(Exception):
    """
    Exception raised for validation errors.

    Attributes:
        text (str): The error text.
    """

    def __init__(self, text: str):
        """
        Initializes the ValidationError with a given error text.

        Args:
            text (str): The error text describing the issue.
        """
        super().__init__(text)
        self.text: str = text

    def __str__(self) -> str:
        """
        Custom string representation for the exception.

        Returns:
            str: The string representation in the format
                    'ValidationError: text'.
        """
        return f"ValidationError: {self.text}"
