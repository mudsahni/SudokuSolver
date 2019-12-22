public class SodukuSolver {

    private int[][] board;

    public SodukuSolver(int[][] board) {
        this.board = board;
    }

    public void printBoard() {
        for (int i = 0; i < board.length; i++) {
            if (i % 3 == 0 && i != 0) {
                System.out.println("- - - - - - - - - - - - - - ");
            }

            for (int j = 0; j < board[0].length; j++) {
                if (j % 3 == 0) {
                    System.out.println(" | " + "\n");
                }

                if (j == 8) {
                    System.out.println(board[i][j]);
                } else {
                    System.out.println(board[i][j] + " " + "\n");
                }

            }
        }

    }

    public static void main(String[] args) {
        int[][] board = {
                {7, 8, 0, 4, 0, 0, 1, 2, 0},
                {6, 0, 0, 0, 7, 5, 0, 0, 9},
                {0, 0, 0, 6, 0, 1, 0, 7, 8},
                {0, 0, 7, 0, 4, 0, 2, 6, 0},
                {0, 0, 1, 0, 5, 0, 9, 3, 0},
                {9, 0, 4, 0, 6, 0, 0, 0, 5},
                {0, 7, 0, 3, 0, 0, 0, 1, 2},
                {1, 2, 0, 0, 0, 7, 4, 0, 0},
                {0, 4, 9, 2, 0, 6, 0, 0, 7}
        };

        SodukuSolver SS = new SodukuSolver(board);
        SS.printBoard();


    }

}
