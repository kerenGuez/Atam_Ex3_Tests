#include<stdio.h>

int get_element_from_matrix(int* matrix[], int n, int row, int col);
int inner_prod(int* mat_a[], int* mat_b[], unsigned int row_a, unsigned int col_b, unsigned int max_col_a, unsigned int max_col_b);
int matrix_multiplication(int* res[], int* mat_a[], int* mat_b[], unsigned int m, unsigned int n, unsigned int p, unsigned int q);

/* Auxiliary function to print the result. Use it to test yourselves. */
void print_result_matrix(int* matrix, unsigned int m, unsigned int n) {
    printf("[");
    for(int i=0; i<m; i++) {
        for(int j=0; j<n; j++) {
            if (j==n-1) printf("%d", *(matrix + i*n + j));
            else printf("%d ", *(matrix + i*n + j));
        }
        if (i<m-1) printf("\n");
    }
    printf("]\n");
}

int main() {
    int M, N, P, Q;
    //printf("Enter the values for M, N, P, Q: ");
    scanf("%d %d %d %d", &M, &N, &P, &Q);

    int mat_a[M][N];
    int mat_b[P][Q];
    int res[M][Q];

    //printf("Enter the elements of mat_a:\n");
    for(int i=0; i<M; i++) {
        for(int j=0; j<N; j++) {
            scanf("%d", &mat_a[i][j]);
        }
    }

    //printf("Enter the elements of mat_b:\n");
    for(int i=0; i<P; i++) {
        for(int j=0; j<Q; j++) {
            scanf("%d", &mat_b[i][j]);
        }
    }

    int n, row, col, row_a, col_b, max_col_a, max_col_b;

    //printf("Enter n:");
    scanf("%d", &n);
    //printf("Enter row: ");
    scanf("%d", &row);
    //printf("Enter col: ");
    scanf("%d", &col);

    //printf("Enter row_a: ");
    scanf("%d", &row_a);
    //printf("Enter col_b: ");
    scanf("%d", &col_b);
    //printf("Enter max_col_a: ");
    scanf("%d", &max_col_a);
    //printf("Enter max_col_b: ");
    scanf("%d", &max_col_b);


    printf("mat_a[%d][%d] = %d\n", row, col, get_element_from_matrix((int**)mat_a, n, row, col));
	if (N == P){
		printf("mat_a[%d]*mat_b[%d] = %d\n", row_a, col_b, inner_prod((int**)mat_a, (int**)mat_b, row_a, col_b, max_col_a, max_col_b));
		printf("mat_a*mat_b=\n");
		matrix_multiplication((int**)res, (int**)mat_a, (int**)mat_b, M, N, P, Q);
		print_result_matrix((int*)res, M, Q);
	}
	else {
		printf("mat_a*mat_b=%d\n", matrix_multiplication((int**)res, (int**)mat_a, (int**)mat_b, M, N, P, Q));
	}
    

    return 0;
}
