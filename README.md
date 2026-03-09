## Project architecture

## Data ingestion

## Lessons learned

## Lessons learned

During this project, I first tried to load CSV files manually with SQL commands inspired by a SQL Server tutorial.

Because I was working with PostgreSQL in VS Code, I ran into several issues:
- `BULK INSERT` was not supported
- `COPY` raised local file permission issues
- manually creating empty tables before loading data made debugging slower

To make the pipeline more reliable, I switched to Python-based ingestion using pandas and PostgreSQL connection tools.

This approach was much faster, easier to debug, and more aligned with a real data engineering workflow:

CSV files → Python ingestion → Bronze layer → SQL transformations → Silver → Gold

## Next steps
