import json, logging, requests, urllib.request, urllib.parse
from time import sleep
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction
from ulauncher.api.shared.event import PreferencesEvent
from ulauncher.api.shared.event import PreferencesUpdateEvent

from src.functions import strip_list
from src.items import no_input_item, no_results_item, generate_search_items
from src.discogs_search import DiscogsSearch

logger = logging.getLogger(__name__)

class DiscogsSearchExtension(Extension):

    api_token = None
    max_results = None

    def __init__(self):
        super(DiscogsSearchExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())
        self.subscribe(PreferencesEvent, PreferencesEventListener())
        self.subscribe(PreferencesUpdateEvent, PreferencesUpdateEventListener())
        print(self.api_token)


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = []
        logger.info('preferences %s' % json.dumps(extension.preferences))

        query = event.get_argument() or str()

        if len(query.strip()) == 0:
            return RenderResultListAction(no_input_item())

        params = strip_list(query.split(' '))  
        search = DiscogsSearch(params, extension.preferences['discogs_api_token'])

        if not search.has_query():
            return RenderResultListAction(show_used_args(parser))

        results = search.execute(int(extension.preferences['max_results']))

        if not results:
            return RenderResultListAction(no_results_item())


        return RenderResultListAction(generate_search_items(results, extension.preferences['description_template']))


class ItemEnterEventListener(EventListener):

    def on_event(self, event, extension):
        data = event.get_data()
        return RenderResultListAction([ExtensionResultItem(icon='images/icon.png',
                                                           name=data['new_name'],
                                                           on_enter=HideWindowAction())])

class PreferencesEventListener(EventListener):
    def on_event(self, event, extension):
        extension.api_token = event.preferences["discogs_api_token"]

class PreferencesUpdateEventListener(EventListener):
    def on_event(self, event, extension):
        if event.id == "discogs_api_token":
            extension.api_token = event.new_value


if __name__ == '__main__':
    DiscogsSearchExtension().run()