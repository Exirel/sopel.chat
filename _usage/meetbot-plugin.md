---
title: Using the meetbot plugin
migrated: true
source: wiki
order: 1000
previously:
  - /usage/meetbot-module/
---

Sometimes, you might want to have meetings, and meetbot is here so you won't need to manually write down everything that was discussed. It simply does that for you.

The meetbot plugin is available in Sopel, and is rather simple to use. It was inspired by [Debian's Meetbot](https://wiki.debian.org/MeetBot/) and is almost identical in functionality and commands.
## Making and running a meeting - a complete tutorial
To make a meeting, first pick a quiet channel (and make sure Sopel is there) which is not the main network channel. Then, use the `.startmeeting`  command. When called without an argument (like in the previous example), the meeting will not have a title. If you want a title for the meeting, you can supply it as an argument, like this: `.startmeeting Board Meeting`.

The first stage of each well organized meeting should be doing a roll call, making sure everyone needed is present. Since more than one subject can be set for a meeting, and a roll call is the first subject in our example, change the subject using `.subject Roll Call`.

After you made sure everyone is present, it is time to set the chairs. Not all meetings has chairs. Chairs are people who can issue meeting-related commands to the meetbot. By default, only the one who started the meeting can issue meeting-related commands unless they assign chairs using the appropriate command, as follows: `.chairs Elad Tyrope` the argument of this command is a list of nicks, separated by spaces. There should be at least one nick on the list, otherwise there is no point in using this command.

After setting chairs, it might also be useful to make an informational item for people who are present, for example `.info Everyone is here` or `.info Elad is on vacation thus missing` 

Now that you are done with the roll call, you can move to the first subject on the agenda, using `.subject Something` like we did for the roll call. More informational items might be useful. In addition to the simple information item, there are also `.action` (for example `.action Elad will write more documentation`) and `.agreed` (for example `.agreed Unicorns are just horny horses`) which are used exactly the same as `.info`, and `.link` which needs a URL as an argument, for example `.link https://xkcd.com/353/`. Don't forget to use the `.subject` command to change current subject when needed.

After discussing all subjects on the meeting agenda, it is advised the last subject will be "Open Floor", to give time for people to raise misc. concerns, questions and so on.

When it's time to end the meeting, simply use `.endmeeting` to end it. Sopel will supply a link to the meeting summary, which will contain all subjects, informational items and links neatly organized for later reference, as well as a link to a plain text full log of the meeting.
 
## Meetbot Commands Summary
We don't expect you to remember all commands from the top of your head, so this cheat sheet might be useful:

| Commands | Example | Purpose |
| ------- | ------- | ------- |
| .startmeeting | .startmeeting<br>.startmeeting title | Start a meeting, title is optional |
| .chairs | .chairs Embolalia Elad | Chairs are people who can control the meeting, when no chairs are set, only the person who started the meeting can issue meeting-related commands. The list of nicknames is separated by spaces. |
| .info | .info Things happened | Note an informational list item in the meeting summary |
| .action | .action Elad to improve meetbot | Note an action item in the meeting summary |
| .agreed | .agreed Unicorns are just horny horses | Note an agreement in the meeting summary |
| .link | .link https://xkcd.com/353/ | Note a link item in the meeting summary |
| .subject | .subject roll call | Change current subject for the meeting summary |
| .endmeeting | .endmeeting | End the meeting, finalize the log file and provide a link to it | 