import config
from linkedin_api import Linkedin


class linkedin_mercuryo_io():
    api = None
    LINKEDIN_USER = config.LINKEDIN_USER
    LINKEDIN_PASS = config.LINKEDIN_PASS

    def __init__(self):
        pass
        self.api = Linkedin(config.LINKEDIN_USER, config.LINKEDIN_PASS)

    def get_posts(self):
        items = self.api.get_company_updates(public_id='mercuryo-io', urn_id='', max_results=1)
        #with open("company_updates.json", "w") as fp:
        #    json.dump(items, fp)
        #with open("company_updates.json", "r") as fp:
        #    items = json.load(fp)
        return items

    def parse_posts(self, items):
        urls = []
        for item in items:
            try:
                post_ip = item['id']
                url = item['permalink']
            except Exception:
                url = None,
            try:
                title = item['value']['com.linkedin.voyager.feed.render.UpdateV2']['content'][
                            'com.linkedin.voyager.feed.render.ArticleComponent']['title']['text']
            except Exception:
                title = 'Mercuryo posted on Linkedin'

            if url:
                urls.append({
                    'id': post_ip,
                    'url': url,
                    'title': title,
                })

        return urls

