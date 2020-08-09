import subprocess
import datetime
import os


class AutoUpdater:
    def __init__(self):
        with open("/Users/Michael/Documents/Programming/python/projects/AutoUpdater/output.txt", "a+") as self.output, open("/Users/Michael/Documents/Programming/python/projects/AutoUpdater/changes.txt", "a+") as self.changes:

            self.setup()

            self.update("brew upgrade", "", "Brew Upgraded!")
            self.update("brew cask upgrade", "==> No Casks to upgrade", "Casks Updated!")
            self.update("brew update", "Already up-to-date.", "Brew Updated!")
            # self.update("pip3 install -U pip", "Requirement already up-to-date:", "Pip Updated!", 0, 31)
            self.update("rvm install ruby@latest", "", "Ruby Updated!")
            self.update("brew cleanup", "", "Cleaned Up Brew!")

            self.end()
            
    def setup(self):
        self.changes_made = False
        self.date = datetime.datetime.now().strftime("%a %b %d %I:%M:%S %p %Z%Y")
        self.output.write(self.date + "\n")

    def end(self):
        self.output.write("———————————————————————————————————————————————————————————————————————————————————————————————————\n\n")

        if self.changes_made:
            self.changes.write("———————————————————————————————————————————————————————————————————————————————————————————————————\n\n")

    def update(self, command, default_string, notif_title, *rest):
        # terminal_output = subprocess.run(command.split(), stdout=subprocess.PIPE).stdout.decode("utf-8").strip()
        terminal_output = subprocess.run(command.split(), stdout=subprocess.PIPE).stdout.decode("utf-8").strip()
        # terminal_output = subprocess.check_output(command.split()).decode("utf-8").strip()
        self.output.write("\t" + command + "\n")
        for line in terminal_output.split("\n"):
            self.output.write("\t\t" + line + "\n")
        self.output.write("\n")

        condition = (terminal_output != default_string) if len(rest) == 0 else (terminal_output[rest[0]:rest[1]] != default_string)

        if condition:
            os.system(f'osascript -e \'display notification "{terminal_output}" with title "{notif_title}" subtitle "AutoUpdater"\'')

            if not self.changes_made:
                self.changes.write(self.date + "\n")
                self.changes_made = True
            self.changes.write("\t" + command + "\n")
            for line in terminal_output.split("\n"):
                self.changes.write("\t\t" + line + "\n")
            self.changes.write("\n")


if __name__ == "__main__":
    AutoUpdater()
