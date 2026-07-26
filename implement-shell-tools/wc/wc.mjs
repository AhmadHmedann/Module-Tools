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

const total = {
  linesCounter: 0,
  wordsCounter: 0,
  characterCounter: 0,
};
let hadError = false;
for (const path of paths) {
  try {
    const content = await fs.readFile(path, "utf-8");

    const linesCounter = content.split("\n").length - 1;
    const trimmedContent = content.trim();
    const wordsCounter =
      trimmedContent === "" ? 0 : trimmedContent.split(/\s+/).length;
    const characterCounter = content.length;

    total.linesCounter += linesCounter;
    total.wordsCounter += wordsCounter;
    total.characterCounter += characterCounter;

    let results = [];
    if (options.l) results.push(linesCounter);
    if (options.w) results.push(wordsCounter);
    if (options.c) results.push(characterCounter);

    if (!options.l && !options.w && !options.c)
      console.log(
        ` ${linesCounter}  ${wordsCounter} ${characterCounter} ${path}`,
      );
    else {
      console.log(results.join(" ") + " " + path);
    }
  } catch (error) {
    console.error(error.message);
    hadError = true;
  }
}
if (paths.length > 1) {
  if (!options.l && !options.w && !options.c) {
    console.log(
      ` ${total.linesCounter}  ${total.wordsCounter} ${total.characterCounter} total`,
    );
  } else {
    const totalWithFlags = [];
    if (options.l) totalWithFlags.push(total.linesCounter);
    if (options.w) totalWithFlags.push(total.wordsCounter);
    if (options.c) totalWithFlags.push(total.characterCounter);
    console.log(totalWithFlags.join(" ") + " total");
  }
}
if (hadError) {
  process.exitCode = 1;
}
