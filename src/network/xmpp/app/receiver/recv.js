const xmpp = require("simple-xmpp");
const { writeToCSV, format_message } = require("../logger/logger");

xmpp.on("online", (data) => {
  console.log("Hey you are online! ");
  console.log(`Connected as ${data.jid.user}`);
  const connected_msg = format_message('', "EVENT_CONNECTED", "sub_1");
  writeToCSV([connected_msg], "sub_1.csv");
});

xmpp.on("error", (error) =>
  console.log(`iamadit: something went wrong!${error} `)
);

xmpp.on("chat", (from, message) => {
  const msg = format_message(message, "EVENT_MSG_RECD", "sub_1");
  writeToCSV([msg], 'sub_1.csv');
});

xmpp.connect({
  jid: "iamadit@host.docker.internal",
  password: "123",
  host: "172.100.39.10",
  port: 5222,
});
const connect_msg = format_message('', "EVENT_CONN_REQUEST", "sub_1");
writeToCSV([connect_msg], "sub_1.csv");
