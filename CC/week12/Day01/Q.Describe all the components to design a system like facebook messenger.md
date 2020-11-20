# Question: Describe all the components to design a system like facebook messenger.

## Ans:

Designing Facebook Messenger:

❏ Let's design an instant messaging service like Facebook Messenger where
users can send text messages to each other through web and mobile
interfaces.

❏ Facebook Messenger is a software application which provides text-based
instant messaging services to its users.

❏ Messenger users can chat with their Facebook friends both from cell-phones
and Facebook’s website.

Requirements and Goals of the System:

❏ Functional Requirements:

❏ Messenger should support one-on-one conversations between users.

❏ Messenger should keep track of the online/offline statuses of its users.

❏ Messenger should support persistent storage of chat history.

❏ Non-functional Requirements:

❏ Users should have real-time chat experience with minimum latency.

❏ Our system should be highly consistent; users should be able to see the same chat history on
all their devices.

❏ Messenger’s high availability is desirable; we can tolerate lower availability in the interest of
consistency.

Capacity Estimation and Constraints:

❏ Let’s assume that we have 500 million daily active users and on average each
user sends 40 messages daily; this gives us 20 billion messages per day.

❏ Storage Estimation: Let’s assume that on average a message is 100 bytes,
so to store all the messages for one day we would need 2TB of storage.

❏ 20 billion messages * 100 bytes => 2 TB/day

❏ To store five years of chat history, we would need 3.6 petabytes of storage.

❏ 2 TB * 365 days * 5 years ~= 3.6 PB

❏ Bandwidth Estimation: If our service is getting 2TB of data every day, this
will give us 25MB of incoming data for each second.

❏ 2 TB / 86400 sec ~= 25 MB/s

Capacity Estimation and Constraints:

❏ High level estimates:

❏ Total messages 20 billion per day

❏ Storage for each day 2TB

❏ Storage for 5 years 3.6PB

❏ Incoming data 25MB/s

❏ Outgoing data 25MB/s

High Level Design:

❏ At a high-level, we will need a chat server that will be the central piece,
orchestrating all the communications between users.

❏ When a user wants to send a message to another user, they will connect to
the chat server and send the message to the server; the server then passes
that message to the other user and also stores it in the database.

❏ The detailed workflow would look like this:

    ❏ User-A sends a message to User-B through the chat server.

    ❏ The server receives the message and sends an acknowledgment to User-A.

    ❏ The server stores the message in its database and sends the message to User-B.

    ❏ User-B receives the message and sends the acknowledgment to the server.

    ❏ The server notifies User-A that the message has been delivered successfully to User-B.

Detailed Component Design:

❏ At the high level our system needs to handle the following use cases:

❏ Receive incoming messages and deliver outgoing messages.

❏ Store and retrieve messages from the database.

❏ Keep a record of which user is online or has gone offline, and notify all the relevant users
about these status changes.

Messages Handling:

❏ How would we efficiently send/receive messages?

❏ To send messages, a user needs to connect to the server and post messages for the other
users. To get a message from the server, the user has two options:

❏ Pull model: Users can periodically ask the server if there are any new messages for
them.

❏ Push model: Users can keep a connection open with the server and can depend upon
the server to notify them whenever there are new messages.

❏ How many chat servers we need?

❏ Let’s plan for 500 million connections at any time.

❏ Assuming a modern server can handle 50K concurrent connections at any time, we would
need 10K such servers.

❏ How do we know which server holds the connection to which user?

❏ We can introduce a software load balancer in front of our chat servers; that can map each
UserID to a server to redirect the request.

❏ How does the messenger maintain the sequencing of the messages?

❏ We can store a timestamp with each message, which is the time the message
is received by the server.

❏ This will still not ensure correct ordering of messages for clients.

❏ The scenario where the server timestamp cannot determine the exact order of
messages would look like this:

    ❏ User-1 sends a message M1 to the server for User-2.

    ❏ The server receives M1 at T1.

    ❏ Meanwhile, User-2 sends a message M2 to the server for User-1.

    ❏ The server receives the message M2 at T2, such that T2 > T1.

    ❏ The server sends message M1 to User-2 and M2 to User-1.

    ❏ To resolve this, we need to keep a sequence number with every message for
        each client.

Storing and retrieving the messages from the database:

❏ We need to have a database that can support a very high rate of small
updates and also fetch a range of records quickly.

❏ We cannot use RDBMS like MySQL or NoSQL like MongoDB because we
cannot afford to read/write a row from the database every time a user
receives/sends a message.

❏ This will not only make the basic operations of our service run with high
latency, but also create a huge load on databases.

❏ Both of our requirements can be easily met with a wide-column database
solution like HBase.

Managing user’s status:

❏ We need to keep track of user’s online/offline status and notify all the relevant
users whenever a status change happens.

❏ Whenever a client starts the app, it can pull the current status of all users in their friends’ list.

❏ Whenever a user sends a message to another user that has gone offline, we can send a
failure to the sender and update the status on the client.

❏ Whenever a user comes online, the server can always broadcast that status with a delay of a
few seconds to see if the user does not go offline immediately.

❏ Whenever the client starts a new chat with another user, we can pull the status at that time.