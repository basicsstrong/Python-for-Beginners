import requests

# URL of the public API
url = "https://jsonplaceholder.typicode.com/posts"

# Make a GET request to the API
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    posts = response.json()
    
    # Get the title of the first post
    first_post_title = posts[0]['title']
    
    # Print the title of the first post
    print(f"The title of the first post is: {first_post_title}")
else:
    print("Failed to retrieve data. Status code:", response.status_code)
