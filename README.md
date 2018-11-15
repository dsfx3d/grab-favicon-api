# :rocket: grab-favicon API

This is an API built to demostrate features and functionalities of [grabicon](http://github.com/dsfx3d/gunicorn).

### Endpoints
#### grab-favicons
> `GET` **/api/v1/grab-favicons**


Scrape all favicons from a requested url and return a list of favicon json objects.\

Favicon JSON Object:
* **url**: url of the favicon
* **extension**: extension of favicon file
* **size**: size of favicon in bytes

&nbsp;
#### Example
##### request:
`GET /api/v1/grab-favicons?url=github.com`
##### response: 

```
[
	{ "url": "https://github.com/favicon.ico", "extension": "ico", "size": 6518 },
    { "url": "https://github.com/apple-touch-icon.png", "extension": "png", "size": 10942 },
    { "url": "https://assets-cdn.github.com/favicon.ico", "extension": "ico", "size": 6518 } 
]
```
