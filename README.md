## What is this ##
This is a scraper designed to hit the COVID Tracking Project every four hours and gather daily testing, confirmed cases and deaths for the coronavirus across the state.

## How to develop locally ##
1. Clone this repo
2. Run `pipenv install`
3. Create a `.env` file that contains the following environment variables:

| Variable name | Description |
| ------------- | ----------- |
| SLACK_TOKEN | The slack token for the DMN slack, allowing the scraper to post to the appropriate channel |
| AWS_ACCESS_KEY_ID | AWS key used to publish the scraper to Lambda |
| AWS_SECRET_ACCESS_KEY | AWS secret access key used to publish the scraper to Lambda |

4. Run `pipenv shell`, and `python service.py` to test the scraper


## To deploy to lambda ##
1. Update the `zappa_settings.json` file with project name, description and interval
2. Run `zappa deploy` to deploy to lambda
3. Run `zappa update` to update the deployment with any changes post deployment
