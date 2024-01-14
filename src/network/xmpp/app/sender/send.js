const xmpp = require("simple-xmpp");
const { writeToCSV, format_message } = require("../logger/logger");

xmpp.on("online", (data) => {
  console.log("Hey you are online! ");
  console.log(`Connected as ${data.jid.user}`);
  const connected_msg = format_message('', "EVENT_CONNECTED", "pub_1");
  writeToCSV([connected_msg], "pub_1.csv");
  send_messages(1000);
});

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function send_messages(count) {
  let messages = [];
  for (let i = 1; i < count + 1; i++) {
    const message = `msg_${i}`;
    send(message);
    messages.push(format_message(message, "EVENT_MSG_SENT", "pub_1"));
    await sleep(50); // .05 sec    
  }
  writeToCSV(messages, "pub_1.csv");
}

function send(message) {
  xmpp.send("iamadit@host.docker.internal", message);
}

xmpp.on("error", (error) => console.log(`something went wrong!${error}`));

xmpp.on("chat", (from, message) => {
  console.log(`Got a message! ${message} from ${from}`);
});

xmpp.connect({
  jid: "goch6657@host.docker.internal",
  password: "123",
  host: "172.100.39.10",
  port: 5222,
});
const connect_msg = format_message('', "EVENT_CONN_REQUEST", "pub_1");
writeToCSV([connect_msg], "pub_1.csv");
