.. _introduction:

Basic tutorial
===============

.. topic:: Section contents

    In this section, we introduce the basic devrant API wrappers


Get Rants
----------
Returns a given number of rants::
    >>> from pirant import DevRant
    >>> devrant = DevRant()
    >>> # Get Top 10 Rants
    >>> topRants = devrant.get_rants("top", 10, 0)
