#!/usr/bin/node

function second (myArray) {
  if (myArray.length === 2 || myArray.length === 3) { return (0); }

  let max = Number(myArray[2]);
  let secondMax = Number(myArray[2]);

  for (let i = 2; i < myArray.length; i++) {
    if (Number(myArray[i]) > max) {
      secondMax = max;
      max = Number(myArray[i]);
      console.log('new max:', max);
      console.log('new second:', secondMax);
    } else if (Number(myArray[i]) > secondMax) {
      secondMax = Number(myArray[i]);
    }
  }
  return (secondMax);
}

console.log(second(process.argv));
