# Liv Up Purchases

### Architecture

I made a architecture based in nano and micro services.
First, was built a nano service that read the sales files (in this case, has only one)
and save a raw data in a NoSql database (MongoDB).

After that, was built a micro service (an Rest API) which consumer data from a collection of MongoDB
and transform it in relational data saving in a relational database - PostgreSQl.


#### [Liv UP sales](https://github.com/matheuslins/livup_sales)

![LivUp Sales Diagram](https://github.com/matheuslins/livup_purchases/blob/master/docs/img/sales.jpg)

This is a job script which runs on a scheduled basis.
This job could run as a celery task inside an Aws container or an RunDeck job.

With this strategic is easier to scalability. We can scale according to the amount of data that will be injected.
For this reason I choose this architecture.

#### Liv UP Purchases

![LivUp Purchases Diagram](https://github.com/matheuslins/livup_purchases/blob/master/docs/img/purchases.jpg)

This is a Rest API which show the purchases.

```
1 - /insert
```

The endpoint will be transfer the data from one database to another one.
With this strategic, it is also necessary have a job scheduled that will insert the data.

```
2 - /purchases
```

Consult the Postgres database and show all purchases


```
3 - /purchases
```

Consult the Postgres database and show all purchases from a specific user
