const xmpp = require("simple-xmpp");
const { writeToCSV, getFormattedDateTime }= require("./logger");

xmpp.on("online", (data) => {
  console.log("Hey you are online! ");
  console.log(`Connected as ${data.jid.user}`);
  send_messages(1000);
});

function send_messages(count) {
  for(let i = 1; i < count + 1; i++) {
    send(`msg_${i}`);
  }
}

function send(message) {
  xmpp.send("iamadit@host.docker.internal", message);
  const sampleData = {
    From_Device_ID: "pub_1",
    To_Device_ID: "",
    Event_Type: "EVENT_MSG_SENT",
    Message: message,
    Time_Stamp: getFormattedDateTime(),
  };
  writeToCSV(sampleData, 'pub_1.csv');
}

xmpp.on("error", (error) =>
  console.log(`something went wrong!${error}`)
);

xmpp.on("chat", (from, message) => {
  console.log(`Got a message! ${message} from ${from}`);
});

xmpp.connect({
  jid: "goch6657@host.docker.internal",
  password: "123",
  host: "host.docker.internal",
  port: 5222,
});