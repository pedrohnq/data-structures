from typing import Any, Union


class Stack:
    """
    A simple stack implementation using a list.

    Returns:
        Stack: A stack object.
    """
    _stack = []
    
    def pop(self) -> Any:
        """
        Removes and returns the top element of the stack.

        Returns:
            Any: The top element of the stack.
        """
        return self._stack.pop
    
    def push(self, value: Any) -> None:
        """
        Adds an element to the top of the stack.

        Args:
            value (Any): The value to be added to the stack.
        
        Returns:
            None
        """
        self._stack.append(value)
    
    def peek(self) -> Union[None, Any]:
        """
        Returns the top element of the stack without removing it.

        Returns:
            Union[None, Any]: The top element of the stack if the stack is not empty, else None.
        """
        if self.is_empty():
            return None
        return self._stack[-1]
    
    def is_empty(self) -> bool:
        """
        Returns True if the stack is empty, else False.

        Returns:
            bool: Boolean value indicating if the stack is empty or not.
        """
        return len(self._stack) == 0

    def __str__(self):
        return str(self._stack)
    
    def __repr__(self):
        return str(self._stack)