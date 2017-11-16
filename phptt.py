import sublime
import sublime_plugin
import os


class PhpttTestCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        print("Executing phptt test command!")
        file_name = self.view.file_name()
        if len(file_name) > 0:
            if not file_name.endswith('.phpt'):
                print("The file needs ends with '.phpt'")
            cmd = 'phptt ' + 'test ' + file_name
            print("Command: " + cmd)
            print(os.popen(cmd).read())
        return True


class PhpttLcovCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        print("Executing phptt lcov command!")
        file_name = self.view.file_name()
        if len(file_name) > 0:
            if not file_name.endswith('.phpt'):
                print("The file needs ends with '.phpt'")
            cmd = 'phptt ' + 'lcov ' + file_name
            print("Command: " + cmd)
            print(os.popen(cmd).read())
        return True
