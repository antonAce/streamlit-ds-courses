import json
import scrapy


class SkillShareSpider(scrapy.Spider):
    name = 'skillshare'
    allowed_domains = ['www.skillshare.com']
    api_url = 'https://www.skillshare.com/api/graphql'
    start_index = -1
    step_index = 15
    total_count = 1029
    has_next_page = True

    def build_body(self, index):
        graphql_query = {
            "operationName": "GetClassesQuery",
            "variables": {
                "query": "Data Science",
                "where": {
                    "level": [
                        "ALL_LEVELS",
                        "BEGINNER",
                        "INTERMEDIATE",
                        "ADVANCED"
                    ]
                },
                "after": f"{index}",
                "first": self.step_index
            },
            "query": "fragment ClassFields on Class {  badges {    type    __typename  }  durationInSeconds  id  "
                     "largeCoverUrl  sku  studentCount  teacher {    id    name    username    vanityUsername    "
                     "__typename  }  title  url  viewer {    hasSavedClass    __typename  }  __typename}query "
                     "GetClassesQuery($query: String!, $where: SearchFilters!, $after: String!, $first: Int!) {  "
                     "search(query: $query, where: $where, analyticsTags: [\"src:browser\", \"src:browser:search\"], "
                     "after: $after, first: $first) {    totalCount    searchId    pageInfo {      startCursor      "
                     "endCursor      hasNextPage      hasPreviousPage      __typename    }    edges {      cursor      "
                     "node {        ...ClassFields        __typename      }      __typename    }    __typename  }} "
        }

        return json.dumps(graphql_query)

    def start_requests(self):
        yield scrapy.Request(self.api_url, callback=self.parse,
                             method='POST', headers={"Content-Type": "application/json"},
                             body=self.build_body(self.start_index))

    def parse(self, response, **kwargs):
        search_info = response.json().get("data", {}).get("search", {})
        page_info = search_info.get("pageInfo", {})
        self.start_index = int(page_info.get("endCursor", self.start_index + self.step_index))
        self.has_next_page = bool(page_info.get("hasNextPage", False))

        elements = search_info.get("edges", [])

        for element in elements:
            node = element.get("node", {})

            yield {
                'title': node.get("title", None),
                'authors': [node.get("teacher", {}).get("name", None)],
                'students_count': node.get("studentCount", None),
                'duration': node.get("durationInSeconds", None),
                'platform': 'Skillshare',
                'free': True,
                'url': node.get("url", None)
            }

        if self.has_next_page:
            yield scrapy.Request(self.api_url, callback=self.parse,
                                 method='POST', headers={"Content-Type": "application/json"},
                                 body=self.build_body(self.start_index))
