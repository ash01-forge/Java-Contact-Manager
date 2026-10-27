package com.mycompany.assignmentfinal2;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardOpenOption;

/** Creates a local contact store outside the source tree. */
final class ContactStorage {
    private ContactStorage() {
    }

    static String path() throws IOException {
        Path directory = Path.of("data");
        Files.createDirectories(directory);
        Path contacts = directory.resolve("contacts.txt");
        // CREATE + APPEND creates an empty store without overwriting existing data.
        try (var ignored = Files.newOutputStream(contacts,
                StandardOpenOption.CREATE, StandardOpenOption.APPEND)) {
            // The existing screens manage reading and writing contact records.
        }
        return contacts.toString();
    }
}
