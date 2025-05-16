import java.util.Scanner;
import java.util.Arrays;

public class Main {
    static int fib(int n){
        if(n <= 1){
            return 0;
        }
        if(n <= 3){
            return 1;
        }
        else{
            return fib(n-1) + fib(n-2);
        }
    }
    private static final int[] coins = {1, 5, 10, 20, 50};

    static int cc(int amt, int idx){
        if(amt == 0){
            return 1;
        }
        else if(amt < 0){
            return 0;
        }
        else if(idx >= coins.length){
            return 0;
        }
        else{
            return cc(amt - coins[idx], idx) + cc(amt, idx + 1);
        }
    }

    static Result splitArray(int[] arr, int n){
        int smaller = 0;
        int larger = 0;
        for (int j : arr) {
            if (j > n) {
                larger++;
            } else {
                smaller++;
            }
        }

        int[] smaller_arr = new int[smaller];
        int[] larger_arr = new int[larger];
        int smaller_idx = 0;
        int larger_idx = 0;

        for (int j : arr){
            if(j > n) {
                larger_arr[larger_idx] = j;
                larger_idx++;
            }
            else{
                smaller_arr[smaller_idx] = j;
                smaller_idx++;
            }
        }
        return new Result(smaller_arr, larger_arr);
    }

    public static class Result{
        int[] smaller_array;
        int[] larger_array;

        public Result(int[] smaller_arr, int[] larger_arr){
            this.smaller_array = smaller_arr;
            this.larger_array = larger_arr;
        }
    }

    public static void main(String[] args){
        System.out.println("######### 1a #########");
        for(int i = 0; i < 20; i += 2){
            System.out.printf("fib(%s): %s\n", i, fib(i));
        }
        System.out.println(" ");

        System.out.println("######### 2 #########");
        for(int i = 10; i < 100; i += 10){
            System.out.printf("cc(%s): %s\n", i, cc(i, 0));
        }
        System.out.println(" ");

        /* Scanner: prompts user to input amount */
        Scanner in = new Scanner(System.in);
        System.out.println("Amount to change: ");
        String amount = in.nextLine();
        System.out.printf("There are %s ways to count change!\n", cc(Integer.parseInt(amount), 0));
        System.out.println(" ");

        System.out.println("######### 3 #########");
        int[][] tests = {
                {14, 25, 0, 27, 33, 50, 41, 48, 17, 30, 22, 1, 13, 24, 8},
                {40, 50, 10, 7, 14, 1, 30, 15, 11, 3, 12, 0, 44, 8, 28},
                {19, 37, 5, 6, 4, 26, 35, 0, 41, 16, 12, 3, 49, 10, 11}
        };
        for(int[] arr : tests){
            System.out.print("Array: ");
            System.out.println(Arrays.toString(arr));
            Result ret = splitArray(arr, 20);
            System.out.print("smaller: ");
            System.out.println(Arrays.toString(ret.smaller_array));
            System.out.print("larger: ");
            System.out.println(Arrays.toString(ret.larger_array));
            System.out.println();
        }
    }
}

/*
1c) No, Java signed int is 32-bits by default and has a range of [-2147483648, 2147483647].
    The 48th fibonacci number is 2971215073, which causes an integer overflow
 */