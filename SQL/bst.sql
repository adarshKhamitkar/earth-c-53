/*
You are given a table, BST, containing two columns: N and P, where N represents the value of a node in Binary Tree, and P is the parent of N.
Write a query to find the node type of Binary Tree ordered by the value of the node. Output one of the following for each node:

Root: If node is root node.
Leaf: If node is leaf node.
Inner: If node is neither root nor leaf node.
*/

select b.N,
          CASE WHEN b.P is null THEN "Root"
                    WHEN b.N not in (SELECT distinct(b2.P) from BST b2 where b2.P is not null) THEN "Leaf" 
                    ELSE "Inner" END as Type_Node
from BST b
order by b.N;
