#!/usr/bin/node
const args = process.argv[2];
if (!parseInt(process.argv[2])) {
  console.log('Missing size');
} else {
  let i = 0;
  while (i < args) {
    console.log('X'.repeat(args));
    i++;
  }
}