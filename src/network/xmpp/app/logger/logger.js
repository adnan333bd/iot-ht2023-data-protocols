const fs = require("fs");
const path = require("path");
const moment = require("moment");

const CSV_FILE_PATH = path.join(__dirname, "../csv");
const HEADER = [
  "From_Device_ID",
  "To_Device_ID",
  "Event_Type",
  "Message",
  "Time_Stamp",
];

function getFormattedDateTime() {
  const now = new Date();

  // Use moment to format the date in the local time zone
  const formattedDateTime = moment(now).format("YYYY-MM-DD HH:mm:ss.SSSSSS");

  return formattedDateTime;
}

function format_message(message, event_type, device) {
  return {
    From_Device_ID: device,
    To_Device_ID: "",
    Event_Type: event_type,
    Message: message,
    Time_Stamp: getFormattedDateTime(),
  };
}

function writeToCSV(rows, file_name) {
  // If the file doesn't exist, create it and write the header
  let file_path = path.join(CSV_FILE_PATH, file_name);
  if (!fs.existsSync(file_path)) {
    fs.writeFileSync(file_path, HEADER.join(",") + "\n");
  }

  let data = "";
  rows.forEach((row) => {
    // Format the data as a CSV row
    const csvRow = [
      row.From_Device_ID,
      row.To_Device_ID,
      row.Event_Type,
      row.Message,
      row.Time_Stamp,
    ].join(",");
    data += csvRow + "\n";
  });

  // Append the CSV row to the file
  fs.appendFileSync(file_path, data);
}

module.exports = { format_message, writeToCSV, getFormattedDateTime };
