// trying to create an array manually

class MyArray {
  constructor() {
    this.length = 0;
    this.data = {};
  }

  get(index) {
    return this.data[index];
  }

  push(item) {
    this.data[this.length] = item;
    this.length++;
    return this.length;
  }

  pop() {
    if (this.length == 0) return undefined;

    const lastItem = this.data[this.length - 1];
    delete this.data[this.length - 1];
    this.length--;
    return lastItem;
  }

  delete(index) {
    if (index < 0 || index >= this.length) return undefined;

    const item = this.data[index];
    this.shiftItems(index);
    return item;
  }

  shiftItems(index) {
    for (let i = index; i < this.length - 1; i++) {
      this.data[i] = this.data[i + 1];
    }
    delete this.data[this.length - 1];
    this.length--;
  }
}

// Exercise: Reverse a string

function reverse(str) {
  if (!str || str.length < 2 || typeof str !== "string") {
    return str; // or return "";  depending on what you prefer
  }

  const backwards = [];
  for (let i = str.length - 1; i >= 0; i--) {
    backwards.push(str[i]);
  }
  return backwards.join("");
}

// Alternative
const reverse1 = (str) => str.split("").reverse().join("");
// Alternative
const reverse2 = (str) => [...str].reverse().join("");

// Create one sorted list by merging two sorted list
function mergeSortedArrays(arr1, arr2) {
  const merged = [];
  let i = 0;
  let j = 0;

  while (i < arr1.length && j < arr2.length) {
    if (arr1[i] < arr2[j]) {
      merged.push(arr1[i]);
      i++;
    } else {
      merged.push(arr2[j]);
      j++;
    }
  }

  while (i < arr1.length) {
    merged.push(arr1[i]);
    i++;
  }

  while (j < arr2.length) {
    merged.push(arr2[j]);
    j++;
  }

  return merged;
}

// console.log(mergeSortedArrays([0, 3, 5, 7, 31], [4, 6, 30]));
