// View Challenge here - https://projecteuler.net/problem=1
// Solved with Arithmetic progression

function sumMultiplesOf3And5(limit) {
  // Calculate the number of multiples of 3 below the limit
  const numMultiplesOf3 = Math.floor((limit - 1) / 3);
  // Calculate the sum of multiples of 3 using the arithmetic progression formula
  const sumMultiplesOf3 = (numMultiplesOf3 * (numMultiplesOf3 + 1) * 3) / 2;

  // Calculate the number of multiples of 5 below the limit
  const numMultiplesOf5 = Math.floor((limit - 1) / 5);
  // Calculate the sum of multiples of 5 using the arithmetic progression formula
  const sumMultiplesOf5 = (numMultiplesOf5 * (numMultiplesOf5 + 1) * 5) / 2;

  // Calculate the number of multiples of 15 (common multiples of 3 and 5) below the limit
  const numMultiplesOf15 = Math.floor((limit - 1) / 15);
  // Calculate the sum of multiples of 15 using the arithmetic progression formula
  const sumMultiplesOf15 = (numMultiplesOf15 * (numMultiplesOf15 + 1) * 15) / 2;

  // Calculate the final sum by subtracting the sum of multiples of 15 from the sum of multiples of 3 and 5
  const result = sumMultiplesOf3 + sumMultiplesOf5 - sumMultiplesOf15;

  return result;
}

const limit = 1000; // You can change this limit as needed
const result = sumMultiplesOf3And5(limit);
console.log(result);
