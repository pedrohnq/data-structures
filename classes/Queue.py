from typing import Any, Union


class Queue:
    """
    A simple queue implementation using a list.

    Returns:
        Queue: A queue object
    """

    _items = []

    def enqueue(self, item: Any) -> None:
        """
        Adds an element to the rear of the queue.

        Args:
            item (Any): The value to be added to the queue.
        """
        self._items.append(item)
    
    def dequeue(self) -> Union[None, Any]:
        """
        Removes and returns the front element of the queue.

        Returns:
            Union[None, Any]: The front element of the queue if the queue is not empty, else None.
        """
        if self.is_empty():
            return None
        return self._items.pop(0)
    
    def is_empty(self) -> bool:
        """
        Returns True if the queue is empty, else False.

        Returns:
            bool: Boolean value indicating if the queue is empty or not.
        """
        return len(self._items) == 0
    
    def front(self) -> Union[None, Any]:
        """
        Returns the front element of the queue without removing it.

        Returns:
            Union[None, Any]: The front element of the queue if the queue is not empty, else None.
        """
        if self.is_empty():
            return None
        return self._items[0]

    def rear(self) -> Union[None, Any]:
        """
        Returns the rear element of the queue without removing it.

        Returns:
            Union[None, Any]: The rear element of the queue if the queue is not empty, else None.
        """
        if self.is_empty():
            return None
        return self._items[-1]
    
    def __str__(self):
        return str(self._items)
    
    def __repr__(self):
        return str(self._items)
