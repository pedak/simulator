#!/usr/bin/python
"""
resource: a resource of a node
Created by Peter Kalchgruber on 2013-02-05
"""

class Resource:
    """Resource: a web resource of a data node"""
    
    def __init__(self, id):
        self.id = id
    
    def __str__(self):
        return int(self.id)


