import { readFileSync, readFile } from 'fs';
import compile from './wat2wasm.js';

// Get input as int list: ex. [6758,  5199, 0, 1029, ...] 
const input = readFileSync('input.txt')
    .toString().split("\n")
    .map(x => (x == "")? 0 : x)
    .map(x => parseInt(x, 10));

// Terminate input with double zero
input.push(0);
input.push(0);

// Read Web Assembly Text file 
readFile('p1.wat', (err, watString) => {
    if (err) throw err;

    // Compile WAT to WASM
    compile(watString).then((wasmModule) => {
        const wasmInstance = new WebAssembly.Instance(wasmModule, {
            console: { log: (arg) => console.log(arg) }
        });

        const { main, memory } = wasmInstance.exports;

        // Use shared memory buffer to provied WASM with
        // access to AoC input
        const i32_mem = new Int32Array(memory.buffer);
        i32_mem.set(input);

        // Run WASM main routine and print output 
        let res = main();
        console.log(res);
    }).catch(e => {
        console.log(e);
    });
});
