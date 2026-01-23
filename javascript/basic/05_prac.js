let prices = [10, 55, 200, 5, 80]
let filteredPrices = prices.filter((price) => price>20)
console.log("Filtered Prices: " + filteredPrices)
let discountedFilteredPrices = filteredPrices.map((u) => u*0.9)
console.log("Discounted & Filtered Prices: " + discountedFilteredPrices)