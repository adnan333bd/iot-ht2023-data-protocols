const fs = require('fs');
const path = require('path');
console.log(__dirname);
const CSV_FILE_PATH = path.join(__dirname, 'csv');
const HEADER = [
  'From_Device_ID',
  'To_Device_ID',
  'Event_Type',
  'Message',
  'Time_Stamp'
];

function getFormattedDateTime() {
  const now = new Date();

  // Extract date and time components
  const year = now.getFullYear();
  const month = String(now.getMonth() + 1).padStart(2, '0');
  const day = String(now.getDate()).padStart(2, '0');
  const hours = String(now.getHours()).padStart(2, '0');
  const minutes = String(now.getMinutes()).padStart(2, '0');
  const seconds = String(now.getSeconds()).padStart(2, '0');
  const milliseconds = String(now.getMilliseconds()).padStart(3, '0');

  // Ensure that milliseconds have exactly 6 digits
  const formattedMilliseconds = milliseconds.padEnd(6, '0').slice(0, 6);

  // Combine components into the desired format
  const formattedDateTime = `${year}-${month}-${day} ${hours}:${minutes}:${seconds}.${formattedMilliseconds}`;

  return formattedDateTime;
}

function writeToCSV(data, file_name) {
  // If the file doesn't exist, create it and write the header
  let file_path = path.join(CSV_FILE_PATH, file_name); 
  if (!fs.existsSync(file_path)) {
    fs.writeFileSync(file_path, HEADER.join(',') + '\n');
  }

  // Format the data as a CSV row
  const csvRow = [
    data.From_Device_ID,
    data.To_Device_ID,
    data.Event_Type,
    data.Message,
    data.Time_Stamp
  ].join(',');

  // Append the CSV row to the file
  fs.appendFileSync(file_path, csvRow + '\n');
}

module.exports = { writeToCSV, getFormattedDateTime };