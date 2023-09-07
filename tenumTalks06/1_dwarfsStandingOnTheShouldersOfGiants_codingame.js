/**
 * View Challenge here - https://www.codingame.com/training/medium/dwarfs-standing-on-the-shoulders-of-giants
 * Solved using a stack-based approach to explore and traverse the graph, which is a common technique in graph traversal and manipulation.
 */

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

const n = parseInt(readline()); // the number of relationships of influence
let relationships = {};
for (let i = 0; i < n; i++) {
  var inputs = readline().split(" ");
  const x = parseInt(inputs[0]); // a relationship of influence between two people (x influences y)
  const y = parseInt(inputs[1]);
  relationships[x] === undefined
    ? (relationships[x] = [y])
    : relationships[x].push(y);
}

// Write an answer using console.log()
// To debug: console.error('Debug messages...');
console.error(relationships);
let max = 0,
  i = 1;
let keys = Object.keys(relationships);

for (key in keys) {
  let stack = [keys[key]];
  let visited = new Set();
  while (stack.length > 0) {
    let current = stack.pop();
    visited.add(current);
    if (keys.includes(current.toString())) {
      for (let neighbor of relationships[current]) {
        if (!visited.has(neighbor)) {
          stack.push(neighbor);
        }
      }
      i++; //2
    } else {
      max = visited.size > max ? visited.size : max;
      visited = new Set();
      visited.add(keys[key]);
    }
  }
}
// The number of people involved in the longest succession of influences
console.log(max);
