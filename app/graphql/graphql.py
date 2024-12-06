import strawberry
from typing import List


@strawberry.type
class Details:
    message: str
    is_positive: bool

    """

query {
  hello(num: 42, greeting: "Hi") {
    message
    isPositive
  }
}
    """


@strawberry.type
class Query:
    @strawberry.field
    def hello(self, num: int, greeting: str = "Hello") -> Details:
        """
        A complex hello field that customizes the greeting and analyzes positivity.

        Args:
        - num (int): A number to evaluate.
        - greeting (str): Customizable greeting text.

        Returns:
        - Details: Includes a message and positivity analysis.
        """
        is_positive = num > 0
        message = f"{greeting} World, {num} is {'positive' if is_positive else 'negative or zero'}!"
        return Details(message=message, is_positive=is_positive)
