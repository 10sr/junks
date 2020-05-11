Airflow
=======


https://airflow.apache.org/docs/stable/tutorial.html


Testing
-------


    # List available dags
    ./airflow.sh list_dags
    # Test specific task with target date
    ./airflow.sh test tutorial print_date 2015-06-01


Run Server
----------

    pipenv run honcho start

And access to `localhost:8080`
