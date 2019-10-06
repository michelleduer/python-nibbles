using System;

namespace FibonacciApp
{
    public class Fibonacci
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            Console.WriteLine("Enter fibonacci iteration value to calculate:");
            Console.WriteLine("(Example Input: 6, Output: 8)\n");
            string input = Console.ReadLine();
            int iteration = -1;

            Console.WriteLine($"input value: {input}");
            try {
                iteration = Int32.Parse(input);
            } catch (FormatException e) {
                Console.WriteLine($"Invalid input was provided. Error message: {e.Message}");
            }

            int fibonacciValue = iterativeFibonacci(iteration);
            Console.WriteLine($"Fibonacci Value = {fibonacciValue.ToString()}");
        }

        // take an iteration value and calculate the fibonacci value at that iteration
        public static int iterativeFibonacci(int iteration, int secondVal = 1) {
            if (iteration < 1) return 0;
            if (iteration < 3) return 1;

            int firstVal = 1;
            int fibonacci = 0;

            while (iteration > 2) {
                fibonacci = firstVal + secondVal;
                firstVal = secondVal;
                secondVal = fibonacci;
                iteration--;
            }

            return fibonacci;
        }

        // take an iteration value and calculate the fibonacci value at that iteration
        // using a recursive solution
        public static int recursiveFibonacci(int iteration, int firstVal = 1, int secondVal = 2) {
            if (iteration < 1) return 0;
            if (iteration < 3) return firstVal;

            return recursiveFibonacci(iteration - 1, secondVal, firstVal + secondVal);
        }
    }
}
