// create all the folders
const fs = require("fs");

const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

const ROOT_DIR = "./";

let talkFolderName = "";
let numberOfTasksTackled = "";
let numberOfLanguagesUsed = "";
let taskNames = [];
let languagesUsed = [];

readline.question("Enter talk number?", (number) => {
  talkFolderName = "tenumTalks" + (number < 10 ? `0${number}` : number);
  console.log(`Folder name: ${talkFolderName}`);

  readline.question("Enter number of tasks tackled?", (number) => {
    numberOfTasksTackled = number;
    console.log(`Number of Tasks: ${numberOfTasksTackled}`);

    // Function to collect task names asynchronously
    const collectTaskNames = (index) => {
      if (index < numberOfTasksTackled) {
        readline.question(
          "Enter task tackled? (eg. 1_twoSum_leetcode)",
          (task) => {
            taskNames.push(task);
            collectTaskNames(index + 1);
          }
        );
      } else {
        // All task names collected, now collect languages used
        readline.question(
          "Enter number of languages used during session?",
          (number) => {
            numberOfLanguagesUsed = number;
            console.log(`Number of Languages Used: ${numberOfLanguagesUsed}`);

            // Function to collect languages used asynchronously
            const collectLanguagesUsed = (index) => {
              if (index < numberOfLanguagesUsed) {
                readline.question(
                  "Enter language used during session?",
                  (language) => {
                    languagesUsed.push(language);
                    collectLanguagesUsed(index + 1);
                  }
                );
              } else {
                // All languages used collected, close the interface
                readline.close();
                // Now you can use the collected data as needed.
                console.log("Task Names:", taskNames);
                console.log("Languages Used:", languagesUsed);
                createFolderStructure();
              }
            };

            // Start collecting languages used
            collectLanguagesUsed(0);
          }
        );
      }
    };

    // Start collecting task names
    collectTaskNames(0);
  });
});

function createFolderStructure() {
  // Specify the path for the new folder
  const talkFolderPath = `${ROOT_DIR}/${talkFolderName}`;

  // Use fs.mkdir to create the folder
  fs.mkdir(talkFolderPath, (err) => {
    if (err) {
      console.error(`Error creating folder: ${err}`);
    } else {
      console.log(`Folder '${talkFolderPath}' created successfully.`);
      taskNames.map((taskFolder) => {
        let taskFolderPath = `${talkFolderPath}/${taskFolder}`;
        fs.mkdir(taskFolderPath, (err) => {
          if (err) {
            console.error(`Error creating folder: ${err}`);
          } else {
            console.log(`Folder '${taskFolderPath}' created successfully.`);
            // create a questions.md file
            const filePath = `${taskFolderPath}/QUESTION.md`;

            fs.writeFile(filePath, "", (err) => {
              if (err) {
                console.error(`Error creating the empty file: ${err}`);
              } else {
                console.log(
                  `Question file '${filePath}' created successfully.`
                );
              }
            });
            languagesUsed.map((languageFolder) => {
              let languageFolderPath = `${taskFolderPath}/${languageFolder}`;
              fs.mkdir(languageFolderPath, (err) => {
                if (err) {
                  console.error(`Error creating folder: ${err}`);
                } else {
                  console.log(
                    `Folder '${languageFolderPath}' created successfully.`
                  );
                }
              });
            });
          }
        });
      });
    }
  });
}
