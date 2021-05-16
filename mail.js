import { MailSlurp } from "mailslurp-client";

const inbox = await inboxController.createInbox({
    emailAddress: 'oscar.murrillo@imail.com',
})
print(inbox)