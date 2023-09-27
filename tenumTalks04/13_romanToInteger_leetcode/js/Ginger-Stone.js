/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function (s) {
  const symbols = {
    I: 1,
    IV: 4,
    V: 5,
    IX: 9,
    X: 10,
    XL: 40,
    L: 50,
    XC: 90,
    C: 100,
    CD: 400,
    D: 500,
    CM: 900,
    M: 1000,
  };

  let num = 0;

  for (let i = 0; i < s.length; i++) {
    if (symbols.hasOwnProperty([s[i] + s[i + 1]])) {
      num += symbols[s[i] + s[i + 1]];
      i++;
    } else {
      num += symbols[s[i]];
    }
  }

  return num;
};
