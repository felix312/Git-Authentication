import requests

def get_github_user_info(token):
    headers = {
        'Authorization': f'token {token}'
    }
    response = requests.get('https://api.github.com/user', headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

def main():
    token = input("Enter your GitHub Personal Access Token: ")
    
    user_info = get_github_user_info(token)
    if user_info:
        print("GitHub Username:", user_info.get('login'))
        print("GitHub Name:", user_info.get('name'))
        print("GitHub Email:", user_info.get('email'))
    else:
        print("Failed to authenticate with GitHub. Please check your token.")

if __name__ == "__main__":
    main()
