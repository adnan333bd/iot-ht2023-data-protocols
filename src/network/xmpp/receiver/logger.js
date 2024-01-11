const fs = require('fs');
const path = require('path');
console.log(__dirname);
const CSV_FILE_PATH = path.join(__dirname, 'csv');
const HEADER = [
  'FROM_DEVICE_ID',
  'TO_DEVICE_ID',
  'EVENT_TYPE',
  'MSG',
  'TIME_STAMP'
];

function writeToCSV(data, file_name) {
  // If the file doesn't exist, create it and write the header
  let file_path = path.join(CSV_FILE_PATH, file_name); 
  if (!fs.existsSync(file_path)) {
    fs.writeFileSync(file_path, HEADER.join(',') + '\n');
  }

  // Format the data as a CSV row
  const csvRow = [
    data.FROM_DEVICE_ID,
    data.TO_DEVICE_ID,
    data.EVENT_TYPE,
    data.MSG,
    data.TIME_STAMP
  ].join(',');

  // Append the CSV row to the file
  fs.appendFileSync(file_path, csvRow + '\n');
}

module.exports = writeToCSV;