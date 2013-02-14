#!/usr/bin/python
"""
node: Node of web of data
Created by Peter Kalchgruber on 2013-02-05
"""

from resource import Resource

class Node:
    """Node: node (data owner of linked data network)"""
    
    def __init__(self, id,ein=None,eout=None,resources=None):
        self.id = id
        self.ein = ein or []
        self.eout = eout or []
        self.resources = resources or []
        self.redges=[]
    
    def getdegree(self):
        return (len(self.ein)+len(self.eout))    
    
    def linkto(self,node):
        self.eout.append(node)
        node.ein.append(self)
    
    def addresource(self):
        resource=Resource(len(self.resources))
        self.resources.append(resource)
        return resource
        
    def __str__(self):
        return "Node: %s" % self.id


