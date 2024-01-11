const xmpp = require("simple-xmpp");
const { writeToCSV, getFormattedDateTime }= require("./logger");

xmpp.on("online", (data) => {
  console.log("Hey you are online! ");
  console.log(`Connected as ${data.jid.user}`);
});

xmpp.on("error", (error) =>
  console.log(`iamadit: something went wrong!${error} `)
);

xmpp.on("chat", (from, message) => {
  // console.log(`Got a message! ${message} from ${from}`);
  // Example usage:
  const sampleData = {
    From_Device_ID: "",
    To_Device_ID: "Sub_1",
    Event_Type: "EVENT_MSG_RECD",
    Message: message,
    Time_Stamp: getFormattedDateTime(),
  };
  writeToCSV(sampleData, 'sub_1.csv');
});

xmpp.connect({
  jid: "iamadit@host.docker.internal",
  password: "123",
  host: "host.docker.internal",
  port: 5222,
});
