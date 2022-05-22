public class main {
    public static void main(String[] args) {
        int[] c = new int[] {3, 0, 3, -6, 0, 0, 8, -8, 0, 2};
        int[] x = main.createNonZeroVector(c);
        main.sortVector(x);
        main.printVector(x);
    }

    public static int[] createNonZeroVector(int[] vector) {
        int new_size = 0;
        for (int i: vector) {
            if (i != 0)
                new_size++;
        }

        int[] new_vector = new int[new_size];
        int k = 0;
        for (int i = 0; i < vector.length; i++) {
            if (vector[i] != 0) {
                new_vector[k] = (int)Math.pow(vector[i], 2);
                k++;
            }
        }
        return new_vector;
    }

    public static void sortVector(int[] vector) {
        int tmp;
        for (int i = 0; i < vector.length; i++) {
            for (int j = i; j < vector.length; j++) {
                if (vector[i] > vector[j]) {
                    tmp = vector[i];
                    vector[i] = vector[j];
                    vector[j] = tmp;
                }
            }
        }
    }

    public static void printVector(int[] vector) {
        for (int i: vector) {
            System.out.print(i + "\t");
        }
        System.out.println();
    }
}
