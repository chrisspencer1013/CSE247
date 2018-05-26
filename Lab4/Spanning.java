
//package SpanningTree;

import java.util.Scanner;

public class Spanning {

	private static final int MAX = 10;
	static Scanner scan; 

	public static void main(String[] args){

		int[][] cost = new int[MAX][MAX];
		int n, i, j;

		scan = new Scanner(System.in);

		System.out.println("Enter the number of vertices:");

		n = scan.nextInt();

		System.out.println("Enter the cost adjacency matrix (Enter large value if there is no edge):");

		for (i = 0; i<n; i++){
			for (j = 0; j<n; j++){
				cost[i][j] = scan.nextInt();
			}
		}
		prims(cost,n,1);
	}
	private static void prims(int[][] cost, int n, int source) {
		int[] d = new int[MAX];
		int[] visited = new int[MAX];
		int[] nele = new int[MAX];
		int i=0, sum = 0, j=0, u=0, min=0;
		for (i = 0; i < n; i++){
			d[i] = cost[source][i];
			visited[i] = 0;
			nele[i] = source;
		}
		visited[source] = 1;
		for (i = 0; i < n; i++){
			min = 99;
			for (j = 0; j < n; j++){
				if ((d[j] < min) && (visited[j] == 0)){
					min = d[j];
					u = j;
				}
			}
			visited[u] = 1;
			for (j = 0; j < n; j++){
				if ((cost[u][j] < d[j]) && (visited[j] == 0)){
					d[j] = cost[u][j];
					nele[j] = u;
				}
			}
		}
		System.out.println("The following edges have been selected:");
		for (i = 0; i<n; i++){
			System.out.println(i+"-"+ nele[i]+"="+ cost[i][nele[i]]);
			sum = sum + cost[i][nele[i]];
		}
		System.out.println("Total cost is :"+sum);
	}
}