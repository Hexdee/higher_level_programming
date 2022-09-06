#!/usr/bin/node

function second (myArray) {
  if (myArray.length === 2 || myArray.length === 3) { return (0); }

  let max = Number(myArray[2]);
  let secondMax = 0;

  for (let i = 3; i < myArray.length; i++) {
    if (Number(myArray[i]) > max) {
      secondMax = max;
      max = Number(myArray[i]);
    } else if (Number(myArray[i]) > secondMax) {
      secondMax = Number(myArray[i]);
    }
  }
  return (secondMax);
}

console.log(second(process.argv));
