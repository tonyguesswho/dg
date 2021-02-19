# dg

###  Setting Up For Local Development

-   Check that python 3 is installed:

    ```
    python --version
    >> Python 3.7.0
    ```

-   Clone the dg repo and cd into it:

    ```
    git clone https://github.com/tonyguesswho/dg.git
    ```

-   Create and activate a virtual environment:

    ```
    python3 -m venv venv

	source venv/bin/activate
    ```
-   Install dependencies from requirements.txt file:

    ```
    pip install -r requirements.txt
    ```



-   Apply migrations:

    ```
	python manage.py migrate
    ```



*   Run the application with the command

    ```
    python manage.py runserver
    ```

*   Deactivate the virtual environment once you're done:
    ```
    exit
    ```

Database is django default sqlite
secret_key can be added in an .env filee but a fall back exist in the code for testing purposes