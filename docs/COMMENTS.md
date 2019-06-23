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


#### Liv UP Purchases

![LivUp Purchases Diagram](https://github.com/matheuslins/livup_purchases/blob/master/docs/img/purchases.jpg)
