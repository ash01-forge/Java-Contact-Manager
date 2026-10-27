# Java Contact Manager

A Java Swing desktop application for managing contact records, created as an academic Java project by **Adeeb Sharar**.

The project focuses on graphical interfaces, event handling, and local text-file storage. It is part of my Computer Science and Engineering learning portfolio.

## Run the original Java app in your browser

This repository includes a GitHub Codespaces configuration with Java 17 and a lightweight desktop. The app remains a Java Swing application; it is displayed through a virtual desktop, not rewritten as a web app.

1. Upload the complete repository, including **.devcontainer**, **.vscode**, and **scripts**.
2. In GitHub, select **Code → Codespaces → Create codespace on main** (or your default branch).
3. Wait for container setup and the automatic Java build/start to finish.
4. In the Codespaces editor, open **PORTS** and find **6080 — Java Contact Manager Desktop**.
5. Keep its **Port Visibility set to Private**, then select **Open in Browser** (the globe icon).
6. In noVNC, select **Connect** and enter the configured desktop password: **vscode**.
7. The Java welcome window should appear. Select Start to open the contact menu.

If the window is closed, use **Terminal → Run Task → Contact Manager: Open app**. The equivalent terminal command inside Codespaces is:

```text
python3 scripts/run.py --background
```

The included launcher compiles the Java source into build/classes, waits for the desktop, and starts the existing Start class. The Java files and .form layouts are shared with the local desktop version.

### Session and data

- Your forwarded desktop port should remain **Private**. A virtual desktop includes more than the contact manager, so it is not a public visitor-demo link. Each person who wants to run the code can create their own codespace.
- Contacts are stored in the current codespace's Git-ignored data folder. Stopping and resuming the same codespace retains its workspace; deleting a codespace deletes its local data unless separately backed up.
- Stop your codespace after use through the Codespaces menu or https://github.com/codespaces. Active compute and retained storage count toward Codespaces usage; included quotas and billing depend on your account.
- The desktop password above is a documented default for the private Codespaces desktop, not your GitHub account password. Do not make port 6080 public.
- This configuration was checked locally, but a live Codespaces container must still be started after repository upload to confirm the complete browser-desktop session.

See [Codespaces startup guide](CODESPACES-GUIDE-BN.md) for Bangla instructions.

## Features

- Add a contact with a name, phone number, and email address.
- Search for a contact by exact name.
- View saved contact records.
- Delete contacts by exact name.
- Navigate between a start screen, menu, and separate feature screens.
- Keep records locally between sessions.

## Technology

- Java 17 or newer
- Java Swing and the NetBeans GUI Builder
- Java file I/O
- Maven project structure; no external application libraries

## Screens

| Class | Purpose |
| --- | --- |
| Start | Application welcome screen and entry point |
| Menu | Navigation between contact operations |
| Add | Enter and save contact details |
| Search | Find contacts by name |
| Display | View the saved records |
| Delete | Remove contacts by name |
| ContactStorage | Create and locate the local data file |

The matching .form files are included so the original layouts remain editable in NetBeans.

## Run with NetBeans

1. Install a JDK 17 or newer and open the project folder in NetBeans.
2. Open the Maven project containing pom.xml.
3. Run the project. If asked for a main class, choose com.mycompany.assignmentfinal2.Start.

## Build with Maven

Requires Maven 3.6.3+ and JDK 17+. Maven may need internet access on the first build to download its build plugins.

```text
mvn clean package
java -jar target/java-contact-manager-1.0-SNAPSHOT.jar
```

Run from the project folder so the data folder is created in a predictable location.

## Compile without Maven

From the project root, compile the Java source files into a build folder:

```text
javac --release 17 -d build src/main/java/com/mycompany/assignmentfinal2/*.java
java -cp build com.mycompany.assignmentfinal2.Start
```

A desktop environment is required to display the Swing windows.

## Data and privacy

The application creates **data/contacts.txt** relative to its working directory when a contact operation first needs it. No personal contact records are shipped in this repository. The data folder is ignored by Git.

For a demo, enter fictional values such as Demo User, 0000000000, and demo@example.com. Do not commit real names, phone numbers, or email addresses.

## Current limitations

This is an academic learning project, not a production contact system.

- Records are stored in a plain text file, without encryption or user accounts.
- Search uses an exact, case-sensitive name match.
- Duplicate names are allowed; deletion removes matching names.
- The legacy record format uses hyphens as separators. Avoid hyphens or line breaks inside input fields.
- Validation is basic; input checks, storage structure, error messages, and accessibility can be improved in future versions.
- Contact editing is not implemented.

## Repository preparation

The original GUI layouts and contact operations are preserved. Publishing preparation corrected the configured main class to Start, added runnable JAR configuration, and moved runtime contact storage out of the source tree into an automatically created, Git-ignored data folder.

## Author

[Adeeb Sharar](https://github.com/ash01-forge)
