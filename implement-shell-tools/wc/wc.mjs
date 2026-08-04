import { program } from "commander";

import { promises as fs } from "node:fs";

program
  .name("wc")
  .description("wc implementation")
  .argument("<paths...>", "the file path to process")
  .option("-l", "count  lines")
  .option("-w", "count  words")
  .option("-c", "count characters");

program.parse();

const paths = program.args;
const options = program.opts();
const noFlag = !options.l && !options.w && !options.c;

const total = {};
let hadError = false;
for (const path of paths) {
  try {
    const content = await fs.readFile(path, "utf-8");

    const linesCounter = content.split("\n").length - 1;
    const trimmedContent = content.trim();
    const wordsCounter =
      trimmedContent === "" ? 0 : trimmedContent.split(/\s+/).length;
    const characterCounter = content.length;

    const results = [];
    if (options.l || noFlag) {
      results.push(linesCounter);
      total["lineCounter"] = (total["lineCounter"] ?? 0) + linesCounter;
    }
    if (options.w || noFlag) {
      results.push(wordsCounter);
      total["wordsCounter"] = (total["wordsCounter"] ?? 0) + wordsCounter;
    }
    if (options.c || noFlag) {
      results.push(characterCounter);
      total["characterCounter"] =
        (total["characterCounter"] ?? 0) + characterCounter;
    }

     console.log(results.map(value=> String(value).padStart(4)).join(" ") +"    "+ path)
  
  } catch (error) {
    console.error(error.message);
    hadError = true;
  }
}
if (paths.length > 1) {

  console.log(Object.values(total).map(value=> String(value).padStart(4)).join(" "),"total")
  
}
if (hadError) {
  process.exitCode = 1;
}
