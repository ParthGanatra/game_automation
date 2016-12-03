#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int n, m, max;
int **grid;
int *sol;
struct cor {
    int x,y;
} initial; 
int xMove[4] = {1, -1, 0, 0};
int yMove[4] = {0, 0, -1, 1};

bool is_safe(struct cor c)
{
    return ( c.x >= 0 && c.x < n && c.y >= 0 && c.y < m && grid[c.x][c.y]==0);
}
 
void printSolution()
{
    printf("Grid\n");
    for (int x = 0; x < n; x++)
    {
        for (int y = 0; y < m; y++)
            printf(" %2d ", grid[x][y]);
        printf("\n");
    }
    printf("Solution\n");
    for(int x=0; x<(max-1); x++)
        printf("%d ", sol[x]);
    printf("\n");
}
 
int solve_util(int x, int y, int movei)
{
    /*printf("Move %d\n",movei);*/
    int k;
    struct cor next;
    if (movei == max+1)
       return true;

    for (k = 0; k < 4; k++)
    {
       next.x = x + xMove[k];
       next.y = y + yMove[k];
       if (is_safe(next))
       {
         sol[movei-2] = k;
         grid[next.x][next.y] = movei;
         if (solve_util(next.x, next.y, movei+1) == true)
             return true;
         else
             grid[next.x][next.y] = 0;// backtracking
       }
    }

   return false;
}

bool solve_problem()
{
    if (solve_util(initial.x, initial.y, 2) == false)
    {
        printf("Solution does not exist");
        return false;
    }
    else
        printSolution();
 
    return true;
}

int main(){
    int i, j;
    FILE *fp, *fout;
    fp = fopen("que", "r");
    fout = fopen("ans", "w");
    fscanf(fp, "%d %d", &n, &m);

    grid = (int **)malloc(n * sizeof(int *));
    for (i=0; i<n; i++)
        grid[i] = (int *)malloc(m * sizeof(int));

    for(i=0; i<n; i++)
        for(j=0; j<m; j++)
            fscanf(fp, "%d",&grid[i][j]);

    fscanf(fp, "%d %d %d", &initial.x, &initial.y, &max);
    sol = (int *)malloc((max - 1) * sizeof(int));
    for (i=0; i<(max-1); i++)
        sol[i] = 9;
    solve_problem();

    for(int x=0; x<(max-1); x++)
        fprintf(fout, "%d ", sol[x]);
    fprintf(fout, "\n");
}
