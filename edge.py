#!/usr/bin/python
"""
edge: Edge between two resources
Created by Peter Kalchgruber on 2013-02-05
"""



class ResourceEdge:
    """Link from one resource to another resource"""
    
    def __init__(self,node1,resource1,node2,resource2):
        self.node1=node1
        self.node2=node2
        self.resource1=resource1
        self.resource2=resource2
    
    def __eq__(self, other): 
        return self.__dict__ == other.__dict__
    def __ne__(self,other):
        return self.__dict__ != other.__dict__
    def __str__(self):
        return "%s.%s;%s.%s" % (self.node1.id,self.resource1,self.node2.id,self.resource2)