from requests import get
from bs4 import BeautifulSoup


def search(request,
           num_results=10,
           date_from=None,
           date_to=None,
           lang=None):
    """
    Execute google search imitation.
    :param request: the text of your request. Be careful to use special symbols.
    :param num_results: max number of results.
    :param date_from: the min date of publication in format 'date/month/year'. If not necessary -- leave as None.
    :param date_to: the max date of publication in format 'date/month/year'. If not necessary -- leave as None.
    :param lang: specific language of search results. If not necessary -- leave as None.
    :return: list of urls of search results.
    """

    usr_agent = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/61.0.3163.100 Safari/537.36'}

    def fetch_results(search_term, number_results, date_from, date_to, language_code):

        escaped_search_term = search_term.replace(' ', '+')
        search_settings = []

        if date_from is not None:
            search_settings.append('cd_min:' + date_from)
        if date_to is not None:
            search_settings.append('cd_max:' + date_to)
        search_settings = ','.join(search_settings)

        google_url = 'https://www.google.com/search?{}&q={}&num={}'.format(search_settings, escaped_search_term,
                                                                           number_results)
        if language_code is not None:
            google_url += '&hl={}'.format(language_code)

        print(google_url)

        response = get(google_url, headers=usr_agent)
        response.raise_for_status()

        return response.text

    def parse_results(raw_html):
        soup = BeautifulSoup(raw_html, 'html.parser')
        result_block = soup.find_all('div', attrs={'class': 'g'})
        for result in result_block:
            link = result.find('a', href=True)
            title = result.find('h3')
            if link and title:
                yield link['href']

    html = fetch_results(request, num_results, date_from, date_to, lang)
    return list(parse_results(html))