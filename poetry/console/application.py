from typing import List

from cleo import Application as BaseApplication
from cleo import Command

from poetry.__version__ import __version__

from .commands.about import AboutCommand
from .commands.add import AddCommand
from .commands.build import BuildCommand
from .commands.cache.clear import CacheClearCommand
from .commands.cache.list import CacheListCommand
from .commands.check import CheckCommand
from .commands.config import ConfigCommand
from .commands.debug.info import DebugInfoCommand
from .commands.debug.resolve import DebugResolveCommand
from .commands.env.info import EnvInfoCommand
from .commands.env.list import EnvListCommand
from .commands.env.remove import EnvRemoveCommand
from .commands.env.use import EnvUseCommand
from .commands.export import ExportCommand
from .commands.init import InitCommand
from .commands.install import InstallCommand
from .commands.lock import LockCommand
from .commands.new import NewCommand
from .commands.publish import PublishCommand
from .commands.remove import RemoveCommand
from .commands.run import RunCommand
from .commands.search import SearchCommand
from .commands.self.update import SelfUpdateCommand
from .commands.shell import ShellCommand
from .commands.show import ShowCommand
from .commands.update import UpdateCommand
from .commands.version import VersionCommand


class Application(BaseApplication):
    def __init__(self):
        super(Application, self).__init__("poetry", __version__)

        self._poetry = None

    @property
    def default_commands(self) -> List[Command]:
        default_commands = super().default_commands

        commands = [
            AboutCommand(),
            AddCommand(),
            BuildCommand(),
            CheckCommand(),
            ConfigCommand(),
            ExportCommand(),
            InitCommand(),
            InstallCommand(),
            LockCommand(),
            NewCommand(),
            PublishCommand(),
            RemoveCommand(),
            RunCommand(),
            SearchCommand(),
            ShellCommand(),
            ShowCommand(),
            UpdateCommand(),
            VersionCommand(),
        ]

        # Cache commands
        commands += [
            CacheClearCommand(),
            CacheListCommand(),
        ]

        # Debug commands
        commands += [DebugInfoCommand(), DebugResolveCommand()]

        # Env commands
        commands += [
            EnvInfoCommand(),
            EnvListCommand(),
            EnvRemoveCommand(),
            EnvUseCommand(),
        ]

        # Self commands
        commands += [SelfUpdateCommand()]

        return default_commands + commands

    @property
    def poetry(self):
        from pathlib import Path

        from poetry.factory import Factory

        if self._poetry is not None:
            return self._poetry

        self._poetry = Factory().create_poetry(Path.cwd())

        return self._poetry

    def reset_poetry(self):  # type: () -> None
        self._poetry = None


if __name__ == "__main__":
    Application().run()
