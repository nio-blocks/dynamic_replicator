DynamicReplicator
=========

Each incoming signal is replicated x times, where x is the length of *list*. Each output signal will have a new attribute, *title*, with the value of the list.

If *list* fails to evaluate, then *title* will be set to None.

Properties
--------------

-   **title**: Name of attribute to be added with list value.
-   **list**: The list that specifies what new signals to create. Expression Property.

Dependencies
----------------
None

Commands
----------------
None

Input
-------
Any list of signals. It is likely that the signal will have a field from which *list* will reference.

Output
---------
Creates a new signal for each value in *list*. The new signals have a new attribute *title* that is the value of the list item.

-   *title*
