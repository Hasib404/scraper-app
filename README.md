# Scraping app based on Fastapi and MongoDB

- [API Endpoints](#api-endpoints)
- [Install](#install)
- [Test locally](#test-locally)
- [Additional Info](#additional-info)

## API Endpoints

#### POST `/url`

Post a specific url for scrapping. Under the hood, the system will find all the pages url (`including pagination`). When a url is found, app will store the url to the database collection and fetch all the products along with price from the specific page. Then the product informations are stored in a separate collection.

**Request**

```
{
  "url": "https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067?rt=nc&_dmd=1"
}
```

**Example Response**

```
{
  "status": "Complete",
  "page_collected": 63,
  "total_product": 3000
}
```

## Install

A dockerfile for backend server added. A `docker-compose.yml` file consists of 2 services `backend` & `MongoDB` added.

To run, execute the following command:

```
docker-compose rm -f; docker-compose -f docker-compose.yml up --build --force-recreate
```

(It will clean up existing containers and force to be recreated)

---

## Test locally

To test the system follow the steps,

1. First install the app using docker
2. Then check `http://localhost/docs` on your browser to find a beautiful Swagger API documentation provided by FastAPI.
3. After that try the `/url` endpoint, put the following as request body,

```
{
  "url": "https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067?rt=nc&_dmd=1"
}
```

4. After request completion, you will see a response providing the status and how many pages was successfully found and fetched.

5. You can check the data locally in any Mongo CLient using the following url,

```
    mongodb://admin:password123@localhost:27017
```

## Additional Info

- For scrapping `3-10` seconds required for each page (Depending on the internet connection)
- It might take `2-3` minutes for fetching all the products info from all the available pages.
