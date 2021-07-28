PLUGIN_NAME = 'Archiving Plugin'
DESCRIPTION = 'A plugin for managing archives of previous version of articles'
AUTHOR = 'Drew Stimson and Daniel Evans'
VERSION = '0.1'

SHORT_NAME = 'archive_plugin'
MANAGER_URL = 'archive_index'

from utils import plugins
from utils.install import update_settings
from events import logic as event_logic
from plugins.archive_plugin.events import register_update_time


event_logic.Events.register_for_event(event_logic.Events.ON_AUTHOR_PUBLICATION, register_update_time)


class ArchivePlugin(plugins.Plugin):
    plugin_name = PLUGIN_NAME
    display_name = PLUGIN_NAME
    description = DESCRIPTION
    author = AUTHOR
    short_name = SHORT_NAME

    manager_url = MANAGER_URL

    version = VERSION
    janeway_version = "1.4.0"

    is_workflow_plugin = False


def install():
    ArchivePlugin.install()
    update_settings(
        file_path='plugins/archive_plugin/install/settings.json'
    )


def hook_registry():
    """
    Run when sites with hooks are loaded to define function to be run
    """
    return {'journal_archive_list': {'module': 'plugins.archive_plugin.hooks', 'function': 'inject_journal_archive'},
            'article_archive_list': {'module': 'plugins.archive_plugin.hooks', 'function': 'inject_article_archive'},
            'edit_article': {'module': 'plugins.archive_plugin.hooks', 'function': 'inject_edit_article'},
            'request_edit': {'module': 'plugins.archive_plugin.hooks', 'function': 'inject_request_edit'}
            }
