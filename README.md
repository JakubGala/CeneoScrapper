# CeneoScraper

## Analiza struktury opinii w serwisie [Ceneo.pl](https://www.ceneo.pl/)

|Składowa|Selektor|Zmienna|Typ Zmiennej|
|--------|--------|-------|------------|
|opinia|div.js_product-review|review|
|identyfikator opinii|\[data-entry-id\]|review_id|str|
|autor|span.user-post__author-name|author|str|
|rekomendacja|span.user-post__author-recomendation > em|recommendation|bool|
|liczba gwiazdek|span.user-post__score-count|stars|float|
|treść|div.user-post__text|content|
|data wystawienia|span.user-post__published > time:nth-child(1)\[datetime\]|publish_date|
|data zakupu|span.user-post__published > time:nth-child(2)\[datetime\]|purchase_date|
|dla ilu przydatna|button.vote-yes[data-total-vote]<br>button.vote-yes > span<br>span[id^=votes-yes]|useful|
|dla ilu nieprzydatna|button.vote-no[data-total-vote]<br>button.vote-no > span<br>span[id^=votes-no]|useless|
|lista zalet|div.review-feature__title--positives ~ div.review-feature__item <br>div.review-feature__col:has( > div.review-feature__title--positives) > div.review-feature__item<br>div.review-feature__item:has( ~ div.review-feature__title--positives)|pros|
|lista wad|div.review-feature__title--negatives ~ div.review-feature__item <br>div.review-feature__col:has( > div.review-feature__title--negatives) > div.review-feature__item<br>div.review-feature__item:has( ~ div.review-feature__title--negatives)|cons|

- pobranie opinii do niezaleznych zmiennych
- zapisanie skladowych pojedynczych opinii do obiektu slownika
- pobranie wszystkich opinii z pojedynczej strony i zapisanie ich do listy slownikow.
