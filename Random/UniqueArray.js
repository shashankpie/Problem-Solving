// Solution 1

export default function uniqueArray(array) {
  let res = []
  for (const ele of array){
    if (!res.includes(ele)){
      res.push(ele)
    }
  }
  return res
}

// Solution 2

export default function uniqueArray(array) {
  let res = [];
  array.forEach((ele) => {
    if (!res.includes(ele)){
      res.push(ele)
    }
  });
  return res;
}
