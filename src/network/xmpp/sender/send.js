const xmpp = require("simple-xmpp");

xmpp.on("online", (data) => {
  console.log("Hey you are online! ");
  console.log(`Connected as ${data.jid.user}`);
  send();
});

function send() {
  // setTimeout(send, 5000);
  xmpp.send("iamadit@host.docker.internal", `msg_${Date.now()}`);
  
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