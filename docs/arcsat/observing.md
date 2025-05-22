# ARCSAT observing and schedule

## Logistics

### Teams

These are the ARCSAT teams and their associated team names, numbers, and Slack channels.

| Team | Name                          | Team members                        | Slack channel                 |
| ---- | ----------------------------- | ----------------------------------- | ----------------------------- |
| 1    | The Binary Astrologers        | Juneau, Brody, Ryder, Marcos        | astr480-sp25-astrologers      |
| 2    |                               | Kayla, David, Alyssa                | astr480-sp25-team-2           |
| 3    | Transiting Acquaintances      | Sydney, Jehu, Max                   | astr480-sp25-acquaintances    |
| 4    | 3 Crabs in a Trench Coat      | Marina, Holland, Rowan              | astr480-sp25-3-crabs          |
| 5    | Scuti Stragglers              | Marno, Alaina, Nick                 | astr480-sp25-scuti-stragglers |
| 6    | Team 14                       | Grace, Japnit, Josh                 | astr480-sp25-team-14          |
| 7    | Nonchalant SPT                | Lauren, Elli, Maya, Molly           | astr480-sp25-nonchalant       |
| 8    | EPHEMERALS                    | Elliott, Tristen, Nathaniel, Angelo | astr480-sp25-ephemerals       |
| 9    | Red Delicious                 | Eliz, Charli, Alex, Dylan           | astr480-sp25-red-delicious    |
| 10   | UV the unknown variables      | Liam, Brian, Owen                   | astr480-sp25-uv               |
| 11   | Friends of Frobenius (MY Cam) | Alex, Cody                          | astr480-sp25-frobenius        |
| 12   |                               | Danbi, Kyleigh, Devanshi, Ishaani   | astr480-sp25-team-12          |
| 13   |                               | Thomas, Simon, Rachiel              | astr480-sp25-team-13          |

### Schedule

The following is the official schedule for the ARCSAT observations. Requests for changes to the schedule should be made in the `#astr480-sp25-arcsat` Slack channel. **The changes are not official until they are reflected here.**

| Date     |            1st half team             |          2nd half team          |
| -------- | :----------------------------------: | :-----------------------------: |
| Wed 5/7  |                Intro                 |                4                |
| Thu 5/8  |                  12                  |               10                |
| Fri 5/9  |                                      |                5                |
| Sat 5/10 |                                      |                3                |
| Sun 5/11 |                  8                   |               10                |
| Mon 5/12 |                  2                   |               11                |
| Tue 5/13 |                  8                   |                1                |
| Wed 5/14 |                  7                   |                3                |
| Thu 5/15 |                  12                  |               11                |
| Mon 5/26 |                  13                  |                5                |
| Tue 5/27 |                  9                   |                6                |
| Wed 5/28 |                  9                   |               13                |
| Thu 5/29 |                  1                   |                4                |
| Fri 5/30 |    <font color="darkred">2</font>    | <font color="darkred">1</font>  |
| Sat 5/31 |                  7                   | <font color="darkred">11</font> |
| Sun 6/1  |                  6                   | <font color="darkred">3</font>  |
| Mon 6/2  | <font color="darkred">10 & 12</font> | <font color="darkred">4</font>  |
| Tue 6/3  |    <font color="darkred">6</font>    | <font color="darkred">5</font>  |
| Wed 6/4  |    <font color="darkred">7</font>    | <font color="darkred">9</font>  |
| Thu 6/5  |    <font color="darkred">8</font>    | <font color="darkred">11</font> |

The first half of the night will run from evening twilight until 0:00 AM PDT. The second half of the night will run from 0:00 AM PDT until morning twilight. Small changes in the handover time to accommodate specific targets can be made as long as they are communicated to the instructors and both teams agree.

Groups marked in red correspond to the third observing night. Dates for these nights can be changed if you agree with a different team (or fully dropped if you think that you have enough data).

### Slack channels

Please make sure that you have joined the department of astronomy Slack workspace. An invitation link was sent in a Canvas announcement. Once yo have joined please make sure that you join the `#astr480-sp25-arcsat` channel as well as your team channel.

General discussion about the ARCSAT observations, schedule changes, requests for help, etc. will happen in the main `#astr480-sp25-arcsat` channel. During your observations the best way to communicate with your team and instructors is over your team Slack channel (or on Zoom).

### Zoom

The Zoom link for the ARCSAT observations was sent in a Canvas announcement. During your observations all team members must be connected to that Zoom.

### Passwords

Several passwords are needed to access the ARCSAT telescope and the associated computers. These passwords will only be provided in person. Please do not email or message them and do not share them with anyone outside of your team.

## Observing

### Instructor support

Either José or Sam will be available to help you with your observations. During your first observing night one of us will be present on Zoom to help you with any connection or setup issues. Once you are up and running and we confident that you can carry out the observations we will leave you to it but we will remain available on Slack for questions and can reconnect on Zoom if needed.

For your second observing night you will be responsible for your entire observing. One of the instructors will be available on Slack to help you if you have any questions.

Although you can communicate with the instructors at any time, if you are having technical issues with the telescope or the observing interface you should first contact the 3.5m observing specialist using TUI. They have more experience with debugging ARCSAT issues and have access to the telescope and dome controls.

### Before you start observing

Before you start observing you must have read the [user manual](https://www.apo.nmsu.edu/Telescopes/ARCSAT/Operations/ARCSAT_manual_v1.6.pdf) for the ARSCAT telescope and familiarised yourself with the telescope and instrumentation that you will be using.

Follow the instructions in the user manual to set up an SSH tunnel connection to the ARCSAT computer. On Linux/macOS you should be able to do this from a terminal using the following command:

```bash
ssh -L 1234:arcsat-user.apo.nmsu.edu:80 uwobserver@arc-gateway.apo.nmsu.edu
```

and then navigate to `http://localhost:1234` in your web browser. You will be asked for a username and password. After that you should see the ARCSAT control panel.

If you are using Windows you will need to use PuTTY to set up the SSH tunnel. The instructions for this are in the user manual.

You will also need to install TUI to be able to communicate with the 3.5m observing specialist. TUI can be downloaded from [this page](https://www.apo.nmsu.edu/arc35m/TUIdownloads_ARC35m.html). The current version only supports macOS. For Windows and Linux see the _Past Python2 Versions_ section on the same page. Since you will only be using TUI to communicate with the 3.5m observing specialist any version should work fine. Additional information about TUI can be found [here](https://www.apo.nmsu.edu/35m_operations/TUI/).

Once you have installed TUI open it and click on `TUI - Connect`.

```{image} ./images/tui-connect.png
:alt: TUI connect
:class: bg-light
:width: 50%
:align: center
```

Use your name or team name as `User Name` and the program and password provided by the instructors. See the user manual for more details.

Before you start any observations you should check the weather and communicate with the 3.5m observing specialist. they will give you additional information about the weather and, if the conditions allow to observe, they will enable ARCSAT for you.

Additionally your should install DS9 in your computer to be able to visualise and do quick analysis on the data your are taking.

```{note}
Not everybody in each team needs to install all the software. You and your team members are responsible for distributing tasks and observing time across the team.
```

### Calibrations

You are responsible for taking your own calibrations, _even if you are not the first team to observe_. Calibrations must include:

- At least 7 bias frames
- At least 5 dark frames. If you exposure times are longer than 5 minutes take 5x300s dark frames regardless of the exposure time of your science frames.
- At least 3 dome flat frames with good signal levels (the observing interface will do this for you).

Additionally you can choose to take twilight flats. This is not required but will be positively evaluated 😀.

### Communication with the 3.5m observers

You must _always_ keep an eye on the TUI chat window. The 3.5m observing specialist will communicate with you through TUI and may require that you close the dome or stop observing at any time if the weather conditions change. **If you are requested to stop observing you must do so immediately**.

### End of the night

At the end of the night, once you have parked the telescope and closed the dome (see the section in the user manual and follow all the steps), let the 3.5m observers know and wait until they confirm that everything is OK, at which point you disconnect.
