import requests  # Import requests to make HTTP calls

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    If the subreddit is invalid or an error occurs, returns 0.
    """

    # 1. Build the URL for the subreddit's about.json endpoint
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    # 2. Set a custom User-Agent to avoid getting blocked
    headers = {'User-Agent': 'MyRedditApp/0.0.1'}

    try:
        # 3. Make the GET request with headers and disable redirects
        response = requests.get(url, headers=headers, allow_redirects=False)

        # 4. If status code is not 200 (success), return 0
        if response.status_code != 200:
            return 0

        # 5. Parse the JSON response into a Python dictionary
        data = response.json()

        # 6. Try to get the number of subscribers from the JSON
        subscribers = data.get('data', {}).get('subscribers', 0)

        # 7. Return the number of subscribers
        return subscribers

    except requests.RequestException:
        # 8. If something goes wrong with the request, return 0
        return 0
