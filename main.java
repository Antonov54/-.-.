public class main {
    public static int rows = 4;
    public static int columns = 4;
    public static int min = 1;
    public static int max = 9;
    public static int i = 3;

    public static void main(String[] args) {
        i--;
        int[][] mat = main.createMatrix(main.rows, main.columns, main.min, main.max);
        int[] B = main.createVector(mat, main.i);
        main.printVector(B);
        System.out.println("Количество четных числе в i-й строке: " + B.length);
    }

    public static int[][] createMatrix(int rows, int columns, int min, int max) {
        int[][] matrix = new int[rows][columns];

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                matrix[i][j] = min + (int)Math.round(Math.random() * (max - min));
            }
        }

        return matrix;
    }

    public static int[] createVector(int[][] matrix, int i) {
        int length_vector = 0;
        for (int c = 0; c < main.columns; c++) {
            if (matrix[i][c] % 2 == 0)
                length_vector++;
        }

        int[] vector = new int[length_vector];

        int k = 0;
        for (int c = 0; c < main.columns; c++) {
            if (matrix[i][c] % 2 == 0) {
                vector[k] = matrix[i][c];
                k++;
            }
        }

        return vector;
    }

    public static void printVector(int[] vector) {
        for (int с: vector) {
            System.out.print(с + " ");
        }
        System.out.println();
    }
}
