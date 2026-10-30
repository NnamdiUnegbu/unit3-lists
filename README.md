# unit3-lists
CMSC 315 Unit 3 discussion: Python list operations
# Unit 3 Discussion: List Operations

## Overview

This project demonstrated Python list operations, including insertion, deletion, and searching. A music playlist management application was used as a real-world example to demonstrate how list elements were added, removed, and searched.

## Learning Objectives

The assignment demonstrated the following concepts:

- Inserting values into a list.
- Deleting values from a list.
- Searching for values within a list.
- Understanding how list elements shifted during insertion and deletion.
- Analyzing the performance of different list operations.
- Handling empty lists and invalid operations.

## Implementation

Three functions were implemented to demonstrate the required list operations.

### 1. Insert Operation

The `insert_at(lst, index, value)` function used Python's built-in `insert()` method to add values at specified positions.

The implementation demonstrated insertion at the beginning, middle, and end of a music playlist. Existing elements shifted to the right when new elements were inserted before them.

### 2. Delete Operation

The `delete_at(lst, index)` function used the `pop()` method to remove and return an element at a specified index.

Index validation was implemented to prevent errors when an invalid position was provided. The function returned `None` when the index was invalid.

### 3. Search Operation

The `search_value(lst, value)` function performed a linear search by examining list elements sequentially.

The function returned the index when a value was found and returned `-1` when the value was not present.

## Testing and Results

The application was tested using a music playlist containing several song titles.

The following operations were demonstrated:

- Insertion of songs at the beginning, middle, and end.
- Deletion of songs from the beginning, middle, and end.
- Searching for an existing song.
- Searching for a song that was not present in the playlist.
- Inserting an item into an empty list.
- Attempting to delete an item from an empty list.
- Attempting deletion using an invalid index.
- Searching within an empty list.

All demonstrated operations executed successfully, and the program completed without runtime errors.

## Performance Analysis

The implementation demonstrated different time complexities associated with Python list operations.

| Operation | Time Complexity |
|---|---|
| Insertion at beginning or middle | O(n) |
| Insertion at end | O(1) amortized |
| Deletion at beginning or middle | O(n) |
| Deletion at end | O(1) |
| Linear search | O(n) |

The analysis showed that insertion and deletion at the beginning or middle required elements to shift positions. Searching required sequential examination of elements until a match was found or the end of the list was reached.

## Conclusion

This assignment provided practical experience with Python list operations and demonstrated how lists could be used in real-world applications such as music playlist management. It also illustrated the importance of validating indexes, handling empty lists, and understanding how different operations affected application performance.
