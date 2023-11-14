module.exports = {
    "dryRun": false,
    "branches": ["next", "next-major", "main"],
    "plugins": [
      "@semantic-release/commit-analyzer",
      "@semantic-release/release-notes-generator",
      [
        "@semantic-release/changelog",
        {
          "changelogFile": "CHANGELOG.md"
        }
      ],
      "@semantic-release/github",
      [
        "@semantic-release/git",
        {
          "assets": [
            "CHANGELOG.md",
            "client/package.json",
            "client/package-lock.json",
            "requirements/local.txt",
          ],
          "message": "chore(release): ${nextRelease.version} [skip ci]\n\n${nextRelease.notes}"
        }
      ]
    ]
  };
