using System;
using Xunit;

namespace FibonacciApp.UnitTests
{
    public class Fibonacci_Tests
    {
        [Theory]
        [InlineData(0)]
        [InlineData(-2)]
        [InlineData(-15)]
        public void FibonacciLessThanOne_MatchesZero(int iteration)
        {
            Assert.Equal(0, Fibonacci.iterativeFibonacci(iteration));
            Assert.Equal(0, Fibonacci.recursiveFibonacci(iteration));
        }

        [Theory]
        [InlineData(1)]
        [InlineData(2)]
        public void FibonacciLessThanThree_MatchesOne(int iteration)
        {
            Assert.Equal(1, Fibonacci.iterativeFibonacci(iteration));
            Assert.Equal(1, Fibonacci.recursiveFibonacci(iteration));
        }

        [Theory]
        [InlineData(2, 3)]
        [InlineData(3, 4)]
        [InlineData(8, 6)]
        [InlineData(21, 8)]
        [InlineData(233, 13)]
        public void FibonacciIterationInput_MatchesCorrectOutput(int output, int iteration)
        {
            Assert.Equal(output, Fibonacci.iterativeFibonacci(iteration));
            Assert.Equal(output, Fibonacci.recursiveFibonacci(iteration));
        }
    }
}
