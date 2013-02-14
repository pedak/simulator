#!/usr/bin/python
"""
graphgenerator: Creation of a graph with interlinked web resources

Created by Peter Kalchgruber on 2013-02-10
"""
import time
import random
from node import Node
from edge import ResourceEdge
from resource import Resource

class GraphGenerator:
    """Creates graphes"""
    
    @staticmethod
    def link(node1,node2):
        """link resources of two nodes"""
        # node 2 (degree-in) 80% link to existing resource, 20% create new
        p=random.uniform(0,1)
        if p>0.8 or len(node2.resources)<1:
            r2=node2.addresource()
        else:
            r2=node2.resources[random.randint(0,len(node2.resources))-1]
        # node 1 degree-out: to 70% create a new resource, 30% use existing resource
        if p>0.3 or len(node1.resources)<1:
            r1=node1.addresource()
        else:
            r1=node1.resources[random.randint(0,len(node1.resources))-1]                    
        re=ResourceEdge(node1,r1,node2,r2)
        if re not in node1.redges:
            node1.redges.append(re)
            node2.redges.append(re)
            return True
        return False
    
    @staticmethod
    def create(num_nodes,num_links):
        """creates a graph"""
        ###bootstrap###
        nodes=[]
        num_nodes=num_nodes
        num_links=num_links
        totaldegree=0
        n1=Node(1)
        n2=Node(2)
        n1.linkto(n2)
        re=ResourceEdge(n1,n1.addresource(),n2,n2.addresource())
        n1.redges.append(re)
        n2.redges.append(re)
        nodes.append(n1)
        nodes.append(n2)
        totaldegree=2
        
        
        for x in range(3,num_nodes):
            node1=Node(x)
            nc=True
            for node2 in nodes:
                x=(float(node2.getdegree()))/(totaldegree)
                r = random.uniform(0, 1)
                if x>=r:
                    # define resources of nodes to establish link
                    for r in range(1,random.randint(1,num_links)):
                        done=False
                        while not done: #until new resource edge found
                            done=GraphGenerator.link(node1,node2)
                            nc=False
                            totaldegree+=2 
                            node1.linkto(node2)

            if nc==True:
                done=False
                while not done:
                    done=GraphGenerator.link(node1,node2)
            nodes.append(node1)
        return nodes
    
    @staticmethod        
    def printnodes(directory,nodes):
        """print nodes, edges between nodes, and edges between resources"""
        fh=open(directory+"sg-node-edges.csv","w+")
        fh.write("Source;Target;Type;Id;Label;Weight\r")
        for node in nodes:
            for out in node.eout:
                fh.write("%i;%i;Directed;;;1\r" % (node.id,out.id))
        fh.close();
    
        fh=open(directory+"sg-resource-edges.csv","w+")
        fh.write("Source;Target;Type;Id;Label;Weight\r")
        for node in nodes:
            for redge in node.redges:
                fh.write("%i.%i;%i.%i;Directed;;;1\r" % (redge.node1.id,redge.resource1.id,redge.node2.id,redge.resource2.id))
        fh.close();

        fh=open(directory+"sg-resources.csv","w+")
        fh.write("Id;Label;Modularity Class\r")
        for node in nodes:
            for resource in node.resources:
                fh.write("%i.%i;%i.%i;%i\r" % (node.id,resource.id,node.id,resource.id,node.id))
        fh.close()
    
        fh=open(directory+"sg-nodes.csv","w+")
        fh.write("Id;Label\r")
        for node in nodes:
            fh.write("%i;%i\r" % (node.id,node.id))
        fh.close()
    
        for node in nodes:
            print "%s: %i resources, %i edges" % (node,len(node.resources),len(node.redges))


def main():
    nodes=GraphGenerator.create(200,100)
    GraphGenerator.printnodes("graph/",nodes)
    

if __name__ == '__main__':
    main()

    
