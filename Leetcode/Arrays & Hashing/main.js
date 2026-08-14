// Given an array arr, find the first repeating item in it and return it. If it does not exist, return undefined.

// Brute force
function firstRecurringCharacter(arr) {
  const seen = new Set();

  for (const item of arr) {
    if (seen.has(item)) {
      return item;
    }
    seen.add(item);
  }
  return undefined;
}

// Using Hash tables
function firstRecurringCharacter2(arr) {
  const map = {};

  for (const item of arr) {
    if (map[item] !== undefined) {
      return item;
    }
    map[item] = true; // we only care that it exists
  }

  return undefined;
}
