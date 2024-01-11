const xmpp = require("simple-xmpp");
const writeToCSV = require("./logger");

xmpp.on("online", (data) => {
  console.log("Hey you are online! ");
  console.log(`Connected as ${data.jid.user}`);
});

xmpp.on("error", (error) =>
  console.log(`iamadit: something went wrong!${error} `)
);

xmpp.on("chat", (from, message) => {
  console.log(`Got a message! ${message} from ${from}`);
  // Example usage:
  const sampleData = {
    FROM_DEVICE_ID: "device1",
    TO_DEVICE_ID: "device2",
    EVENT_TYPE: "event_type",
    MSG: message,
    TIME_STAMP: "2022-01-11T12:00:00Z",
  };
  writeToCSV(sampleData, 'sub_1.csv');
});

xmpp.connect({
  jid: "iamadit@host.docker.internal",
  password: "123",
  host: "host.docker.internal",
  port: 5222,
});
