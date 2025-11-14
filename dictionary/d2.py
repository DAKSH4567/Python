const test_dict: Record<string, number> = {
  Codingal: 2,
  is: 2,
  best: 2,
  for: 2,
  Coding: 1
};

console.log("The original dictionary : " + JSON.stringify(test_dict));

const K = 2;
let res = 0;

for (const key in test_dict) {
  if (test_dict[key] === K) {
    res = res + 1;
  }
}

console.log("Frequency of K is : " + res);
