# -*- coding: UTF-8 -*-

import re
from resources.lib.modules import client,cleantitle,source_utils


class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['deepmovie.ch']
        self.base_link = 'https://www.deepmovie.ch'
        self.search_link = '/%s/'


    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            url = self.base_link + self.search_link % imdb
            return url
        except:
            return


    def sources(self, url, hostDict, hostprDict):
        try:
            sources = []
            r = client.request(url)
            try:
                qual = re.compile('class="quality">(.+?)<').findall(r)
                for i in qual:
                    if 'HD' in i:
                        quality = 'HD'
                    else:
                        quality = 'SD'
                match = re.compile('<iframe.+?src="(.+?)"').findall(r)
                for url in match:
                    info = i
                    valid, host = source_utils.is_host_valid(url, hostDict)
                    if 'youtube' in host: continue
                    if valid:
                        sources.append({ 'source': host, 'quality': quality, 'language': 'en', 'info': info, 'url': url, 'direct': False, 'debridonly': False })
            except:
                return
        except Exception:
            return
        return sources


    def resolve(self, url):
        return url

