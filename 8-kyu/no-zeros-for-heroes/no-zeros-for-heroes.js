function noBoringZeros(num) {
  // Special case for zero
  if (num === 0) return 0;
  
  // Convert to string, remove trailing zeros, then convert back to number
  return Number(num.toString().replace(/0+$/, ''));
}
​
// Test cases
console.log(noBoringZeros(1450));    // 145
console.log(noBoringZeros(960000));  // 96
console.log(noBoringZeros(1050));    // 105
console.log(noBoringZeros(-1050));   // -105
console.log(noBoringZeros(0));       // 0
​