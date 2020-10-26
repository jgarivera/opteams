from django.db import models


class AssignmentManager(models.Manager):

    def in_date_due_order(self, *args, **kwargs):
        """
            Returns query set sorted by due date
        """
        # Return query set based on filters
        qs = self.all().filter(*args, **kwargs)
        # Evaluate query set as list
        qsl = list(qs)
        # Perform merge sort
        self.merge_sort(qsl)

        return qsl

    def merge_sort(self, array):
        # Skip if array does not contain more than two elements
        if len(array) < 2:
            return

        # Get the middle index
        mid_index = len(array) // 2

        # Retrieve the left and right partitions through array splicing
        left_part = array[:mid_index]
        right_part = array[mid_index:]

        # Perform recursive merge sort on each half partition
        self.merge_sort(left_part)
        self.merge_sort(right_part)

        # Current indices in traversing the two partitions
        i, j = 0, 0

        # Current index in traversing the main array
        k = 0

        # Traverse each half partition equally
        while i < len(left_part) and j < len(right_part):
            if left_part[i].date_due < right_part[j].date_due:
                # Set the value of current main array index to current left partition value
                array[k] = left_part[i]
                # Increment left index
                i += 1
            else:
                # Set the value of current main array index to current right partition value
                array[k] = right_part[j]
                # Increment right index
                j += 1
            # Increment main array index
            k += 1

        # Traverse remaining left partition values
        while i < len(left_part):
            array[k] = left_part[i]
            i += 1
            k += 1

        # Traverse remaining right partition values
        while j < len(right_part):
            array[k] = right_part[j]
            j += 1
            k += 1