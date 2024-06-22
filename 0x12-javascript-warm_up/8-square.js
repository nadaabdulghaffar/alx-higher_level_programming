#!/usr/bin/node
const args = process.argv[2];
const size = parseInt(args);
if (args === undefined || isNaN(args)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
