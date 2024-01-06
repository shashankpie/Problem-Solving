export default function uniqueArray(array) {
  let res = []
  for (const ele of array){
    if (!res.includes(ele)){
      res.push(ele)
    }
  }
  return res
}
