import requests
import dlt

BASE_URL = "https://us-central1-dlthub-analytics.cloudfunctions.net/data_engineering_zoomcamp_api"


@dlt.resource(name="trips", write_disposition="replace")
def trips():
    # Verified behavior of this API:
    # - no params returns 1000 rows (default page)
    # - page=0 returns 0 rows
    # - page=1 returns 1000 rows
    #
    # Therefore, start paging from 1 and stop when an empty page is returned.
    page = 1

    while True:
        r = requests.get(BASE_URL, params={"page": page}, timeout=60)
        r.raise_for_status()
        data = r.json()

        if not data:
            break

        for row in data:
            yield row

        page += 1


def main():
    pipeline = dlt.pipeline(
        pipeline_name="taxi_pipeline",
        destination="duckdb",
        dataset_name="taxi_data",
    )

    load_info = pipeline.run(trips())
    print(load_info)


if __name__ == "__main__":
    main()
