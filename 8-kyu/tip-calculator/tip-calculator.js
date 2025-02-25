function calculateTip(amount, rating) {
    // Convert rating to lowercase to handle case insensitivity
    let service = rating.toLowerCase();
​
    // Define the tipping percentages
    const tips = {
        "terrible": 0,
        "poor": 0.05,
        "good": 0.10,
        "great": 0.15,
        "excellent": 0.20
    };
​
    // Check if the rating exists in the tips object
    if (service in tips) {
        return Math.ceil(amount * tips[service]); // Always round up
    } else {
        return "Rating not recognised";
    }
}
​
// Test cases
console.log(calculateTip(100, "great"));     // 15
console.log(calculateTip(50, "poor"));       // 3
console.log(calculateTip(200, "excellent")); // 40
console.log(calculateTip(100, "average"));   // "Rating not recognised"
​