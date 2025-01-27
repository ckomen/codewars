//Let's consider a table consisting of n rows and n columns. The cell located at the intersection of the i-th row and the j-th column contains number i × j. 
// The rows and columns are numbered starting from 1.You are given a positive integer x. Your task is to count the number of cells in a table that contain number x.

function countOccurrences(n, x) {
    let count = 0;
    
    // Iterate over all divisors of x from 1 to min(n, sqrt(x))
    for (let i = 1; i <= Math.min(n, Math.sqrt(x)); i++) {
        if (x % i === 0) {
            let j = x / i;
            
            // Check if both i and j are <= n
            if (i <= n && j <= n) {
                if (i === j) {
                    count += 1;  // if i == j, count once
                } else {
                    count += 2;  // count both (i, j) and (j, i)
                }
            }
        }
    }
    
    return count;
}


