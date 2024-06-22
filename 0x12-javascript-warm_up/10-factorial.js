#!/usr/bin/node
function Factorial (n) {
  if (isNaN(n) || n === 0) {
    return 1;
  } else {
    return (n * Factorial(n - 1));
  }
}
console.log(Factorial(process.argv[2]));
    