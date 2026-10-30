"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # Insert the value at the specified index.
    # Existing elements at that position and beyond shift one
    # position to the right to create space for the new value.
    #
    # Insertion at the beginning or middle takes O(n) time
    # because elements must shift. Insertion at the end takes
    # O(1) amortized time.

    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # Check whether the index is valid before deleting an element.
    # Negative indexes are allowed if they refer to existing positions.
    # This prevents errors when the list is empty or the index is invalid.

    if not isinstance(index, int) or not (-len(lst) <= index < len(lst)):
        return None

    # pop() removes the element at the specified index and returns its value.
    # Elements after the deleted position shift one position to the left.
    # Deletion at the beginning or middle takes O(n) time,
    # while deletion at the end takes O(1) time.

    return lst.pop(index)


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # Linear search checks each element one at a time, starting
    # from the first position and moving sequentially through the list.
    # The worst-case time complexity is O(n) because every element
    # may need to be examined before finding a match or reaching the end.

    for index in range(len(lst)):
        if lst[index] == value:
            return index

    # Return -1 if the requested value does not exist in the list.
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")
    # Create a music playlist containing several songs.
    playlist = ["Perfect", "Shape of You", "Levitating", "Memories"]

    # Display the original playlist before making changes.
    print("Original playlist:", playlist)

    # Insert a song at the beginning of the playlist (index 0).
    insert_at(playlist, 0, "Blinding Lights")
    print("After insertion at beginning:", playlist)

    # Insert a song into the middle of the playlist.
    middle_index = len(playlist) // 2
    insert_at(playlist, middle_index, "Stay")
    print("After insertion in middle:", playlist)

    # Insert a song at the end of the playlist.
    insert_at(playlist, len(playlist), "Flowers")
    print("After insertion at end:", playlist)

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    # Remove the first song from the playlist.
    # The remaining songs shift one position to the left.
    removed = delete_at(playlist, 0)
    print("Removed from beginning:", removed)
    print("Updated playlist:", playlist)

    # Remove a song from the middle of the playlist.
    middle_index = len(playlist) // 2
    removed = delete_at(playlist, middle_index)
    print("Removed from middle:", removed)
    print("Updated playlist:", playlist)

    # Remove the last song from the playlist.
    removed = delete_at(playlist, len(playlist) - 1)
    print("Removed from end:", removed)
    print("Updated playlist:", playlist)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    # Search for a song that exists in the playlist.
    existing_song = "Shape of You"
    result = search_value(playlist, existing_song)

    # Display the index where the song was found.
    print(f"Searching for '{existing_song}': Index {result}")

    # Search for a song that does not exist in the playlist.
    missing_song = "Someone Like You"
    result = search_value(playlist, missing_song)

    # A result of -1 means the song was not found.
    print(f"Searching for '{missing_song}': Index {result}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
    # Edge case 1: Insert a song into an empty playlist.
    # Python allows insertion at index 0 when the list is empty.
    empty_list = []
    print("Original empty list:", empty_list)

    insert_at(empty_list, 0, "First Song")
    print("After inserting into empty list:", empty_list)

    # Edge case 2: Attempt to delete from an empty list.
    # The function should return None instead of raising an error.
    empty_list = []
    removed = delete_at(empty_list, 0)
    print("Attempt to delete from empty list:", removed)

    # Edge case 3: Attempt deletion using an invalid index.
    # The function should safely return None.
    removed = delete_at(playlist, 100)
    print("Attempt to delete using invalid index:", removed)

    # Edge case 4: Search for a value in an empty list.
    # The search function should return -1.
    result = search_value([], "Unknown Song")
    print("Searching in an empty list:", result)



if __name__ == "__main__":
    main()
