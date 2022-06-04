# Shortest Path With Bellman Optimality Equations

## Cost Matrix

For the cost matrix, we calculate it from the *h(n)* function of the A Star algorithm that runs inside a simple game in Unity. the *h(n)* function is:

```c#
public float hCalculate(int idnode, int idTarget)
    {
        int col1, row1, col2, row2;
        double cost;

        col1 = GetCol(idnode);
        row1 = GetRow(idnode);
        col2 = GetCol(idTarget);
        row2 = GetRow(idTarget);
        //NodeA nodeAnalyzed = nodesA [row2, col2];

        cost = Math.Abs(col2 - col1) * sizecell;
        cost = cost + Math.Abs(row2 - row1) * sizecell;

        h[row1, col1] = (float)cost;

        return ((float)cost);
    }
```
and for all nodes in a grid, `nodesA[rows, cols]`, the *h* cost is:

```c#
for (int i = 0; i < rows; i++)
{
    for (int j = 0; j < cols; j++)
    {
        int cid = myGraph.nodesA[i, j].idNode;
        int sid = startNode.idNode;
        int tid = targetNode.idNode;
        float hcost = myGraph.hCalculate(myGraph.nodesA[i, j].idNode, targetNode.idNode);
        s += hcost + " ";

    }
    s += "\n";
}
File.WriteAllText("C:\\Users\\mariana\\Documents\\github-mariana\\code-journal\\path\\cost.txt", s);
```

In A Star algorithm, *h(n)* is a heuristic function that estimates the cost of the cheapest path from n to the goal. The heuristic function is problem-specific.

The cost matrix looks as follows, where the 0 value (lowest) is the target cell and any other cell can be the start cell.

![img](./costs1.png)