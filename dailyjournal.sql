CREATE TABLE `Moods` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `label` TEXT NOT NULL
);

CREATE TABLE `Instructor` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name`  TEXT NOT NULL
);

CREATE TABLE `Entries` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `date`  TEXT NOT NULL,
    `concept`   TEXT NOT NULL,
    `entry`     TEXT NOT NULL,
    `mood_id`   INTEGER NOT NULL,
    `instructor_id`   INTEGER NOT NULL,
	FOREIGN KEY(`mood_id`) REFERENCES `Mood`(`id`),
	FOREIGN KEY(`instructor_id`) REFERENCES `Instructor`(`id`)

);

INSERT INTO `Moods` VALUES (null, "Really confident");
INSERT INTO `Moods` VALUES (null, "I got it. for the most part.");
INSERT INTO `Moods` VALUES (null, "Wait What?");
INSERT INTO `Moods` VALUES (null, "Oh gosh no...");
INSERT INTO `Moods` VALUES (null, "Really not confident...");

INSERT INTO `Instructor` VALUES (null, "Steve Brownlee");
INSERT INTO `Instructor` VALUES (null, "Jack Parsons");
INSERT INTO `Instructor` VALUES (null, "Joe Shepard");


INSERT INTO `Entries` VALUES (null, "2020-10-17", "tings", "code tings", 5, 2);
INSERT INTO `Entries` VALUES (null, "2020-10-30", "testing", "code testing", 3, 1);
INSERT INTO `Entries` VALUES (null, "2020-11-07", "other tings", "other code tings", 2, 3);


SELECT * FROM `Moods`;
SELECT * FROM `Entries`;
SELECT * FROM `Instructor`;

SELECT
    m.id,
    m.label
FROM mood m