# lego-data-explorer
Exploring the Rebrickable Lego Dataset using SQLAlchemy, FastAPI, and Polars.

# Data 
Data is provided by <a href="https://rebrickable.com/downloads/" target="_blank">Rebrickable</a> downloadable CSV files following the provided Schema-diagram for the most part. Some table and column names are changed to make them more meaningful without context (e.g. in the `parts` table we changed `id -> part_id` or `name -> part_name`). The data in some CSV files contains additional columns not mentioned in the schema diagram (e.g. image URLs). Data is stored in a PostgreSQL database. ![schema diagram provided by Rebrickable](https://rebrickable.com/static/img/diagrams/downloads_schema_v3.png)
