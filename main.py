import requests

def fetch_github_user_activity(username):
    url = f'https://api.github.com/users/{username}/events'
    try:
        request = requests.get(url)
        request.raise_for_status()
        events = request.json()

        if not events:
            print(f'No public activity found for user {username}')
            return
        print(f"Recent Activity for GitHub User: {username}")
        print("-" * 40)

        for event in events[:10]:  # Fetch up to 10 recent events
            event_type = event.get("type", "Unknown Event")
            repo_name = event["repo"]["name"]
            created_at = event["created_at"]

            print(f"Event: {event_type}")
            print(f"Repository: {repo_name}")
            print(f"Time: {created_at}")
            print("-" * 40)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching activity: {e}")
    except KeyError as e:
        print(f"Unexpected response structure: {e}")



def main():
    user = input("Enter user name: ")
    fetch_github_user_activity(user)


if __name__ == "__main__":
    main()