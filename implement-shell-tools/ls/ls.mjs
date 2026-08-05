import { promises as fs } from "node:fs";
import { program } from "commander";

program
  .name("ls ")
  .description("ls implementation")
  .argument("[path]", "The path to process") //zero or one path
  .option("-1, --one-per-line", "one file per line")
  .option("-a", "show hidden files");
program.parse();

const path = program.args[0] || ".";
const options = program.opts();
try {
  const files = await fs.readdir(path);
  console.log(files)
  const visibleFiles = files.filter(
    (file) => options.a || !file.startsWith("."),
  );
  if(options.onePerLine)
  {
    console.log(visibleFiles.join("\n"))
  }else{
    console.log(visibleFiles.join("     "))
  }
  
} catch (error) {
  console.error(error.message);
}