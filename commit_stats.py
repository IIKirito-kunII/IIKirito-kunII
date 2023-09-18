from github import Github
import datetime

g = Github("YOUR_PERSONAL_ACCESS_TOKEN")

repo = g.get_repo("IIKirito-kunII/IIKirito-kunII.git")

commits = repo.get_commits(since=datetime.datetime.now() - datetime.timedelta(days=30))

with open('README.md', 'w') as f:
    f.write("### Commit Activity by Time of Day\n\n")
    f.write("| Time of Day | Commits | Percentage |\n")
    f.write("|-------------|---------|------------|\n")
    f.write("| 🌞 Morning  | {}     | {:.2f}%     |\n".format(morning_commits, morning_percentage))
    f.write("| 🌆 Daytime  | {}     | {:.2f}%     |\n".format(daytime_commits, daytime_percentage))
    f.write("| 🌃 Evening  | {}     | {:.2f}%     |\n".format(evening_commits, evening_percentage))
    f.write("| 🌙 Night    | {}     | {:.2f}%     |\n".format(night_commits, night_percentage))
