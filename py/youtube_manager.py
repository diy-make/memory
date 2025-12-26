import os
import argparse
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# --- CONFIGURATION ---
# Full management scope for YouTube account
SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]

# Paths for credentials - using relative paths for portability within the metagit
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# For initial setup, we might look for client_secret in a common location or the user provides it
CLIENT_SECRET_FILE = os.path.join(BASE_DIR, "..", "json", "client_secret.json")
TOKEN_FILE = os.path.join(BASE_DIR, "..", "json", "youtube_token.json")

def get_authenticated_service():
    """Handles the OAuth2 flow and returns an authorized YouTube API service."""
    creds = None
    # The file youtube_token.json stores the user's access and refresh tokens.
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            print("Refreshing expired token...")
            creds.refresh(Request())
        else:
            if not os.path.exists(CLIENT_SECRET_FILE):
                print(f"ERROR: client_secret.json not found at '{CLIENT_SECRET_FILE}'")
                print("Please download your credentials from Google Cloud Console and place them there.")
                return None
            
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            # Since we are in a headless/CLI environment, we use run_local_server
            # Note: This requires the user to have access to the local port or use a specific flow.
            # In some terminal setups, a console-based flow is better.
            creds = flow.run_local_server(port=0)
        
        # Save the credentials for the next run
        os.makedirs(os.path.dirname(TOKEN_FILE), exist_ok=True)
        with open(TOKEN_FILE, "w") as token:
            token.write(creds.to_json())

    return build("youtube", "v3", credentials=creds)

def list_channels(service):
    """Test function to list the user's channel details."""
    try:
        request = service.channels().list(
            part="snippet,contentDetails,statistics",
            mine=True
        )
        response = request.execute()
        
        if "items" in response:
            for item in response["items"]:
                print(f"Channel Title: {item['snippet']['title']}")
                print(f"Channel ID:    {item['id']}")
                print(f"Subscribers:   {item['statistics']['subscriberCount']}")
                print(f"View Count:    {item['statistics']['viewCount']}")
        else:
            print("No channel found.")
            
    except HttpError as e:
        print(f"An HTTP error {e.resp.status} occurred: {e.content}")

def main():
    parser = argparse.ArgumentParser(description="YouTube Account Manager for Swarm Memory")
    parser.add_argument("command", choices=["test", "setup"], help="Command to execute")
    args = parser.parse_args()

    if args.command == "setup":
        print("Initializing setup and authentication flow...")
        service = get_authenticated_service()
        if service:
            print("Authentication successful.")
            list_channels(service)
    elif args.command == "test":
        service = get_authenticated_service()
        if service:
            list_channels(service)

if __name__ == "__main__":
    main()
