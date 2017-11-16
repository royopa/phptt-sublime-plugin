import sublime
import sublime_plugin
import os
import subprocess
from os.path import expanduser


class PhpttTestCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sublime.active_window().run_command(
            "show_panel", {"panel": "console", "toggle": True}
        )

        file_name = self.view.file_name()
        if len(file_name) > 0:
            if not file_name.endswith('.phpt'):
                print("Error! Are you using a .phpt file?")
                return
            cmd = ['phptt', 'test', file_name]
            shell_command = ShellCommand()
            print(shell_command.shell_out(cmd))
        return True


class PhpttLcovCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        sublime.active_window().run_command(
            "show_panel", {"panel": "console", "toggle": True}
        )

        file_name = self.view.file_name()
        if len(file_name) > 0:
            if not file_name.endswith('.phpt'):
                print("Error! Are you using a .phpt file?")
                return
            cmd = ['phptt', 'lcov', file_name]
            shell_command = ShellCommand()
            print(shell_command.shell_out(cmd))
        return True


class ShellCommand():
    """Base class for shelling out a command to the terminal"""

    def __init__(self):
        self.error_list = []

        # Default the working directory for the shell command to the user's
        # home dir.
        self.workingDir = expanduser("~")

    def debug_message(self, msg):
        print("[Phptt] " + str(msg))

    def setWorkingDir(self, dir):
        self.workingDir = dir

    def get_errors(self, path):
        self.execute(path)
        return self.error_list

    def shell_out(self, cmd):
        data = None

        for i, arg in enumerate(cmd):
            if isinstance(arg, str) and arg.startswith('~'):
                cmd[i] = os.path.expanduser(arg)

        self.debug_message(' '.join(cmd))

        info = None
        if os.name == 'nt':
            info = subprocess.STARTUPINFO()
            info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            info.wShowWindow = subprocess.SW_HIDE

        proc = subprocess.Popen(
            cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT, startupinfo=info, cwd=self.workingDir
        )

        if proc.stdout:
            data = proc.communicate()[0]

        return data.decode()

    def execute(self, path):
        self.debug_message('Command not implemented')
