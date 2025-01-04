Auto-Insta-Reels-YT-Channel
An automated solution for scraping Instagram reels and compiling them into YouTube videos with automated uploads.

Features
🎥 Automatically scrapes video content from Instagram profiles you follow
🔄 Compiles multiple video clips into a single video
🎬 Adds intro video to compiled content
📤 Automated YouTube upload functionality
🔐 Secure Google OAuth2.0 authentication
🎯 Customizable video upload settings
Prerequisites
Python 3.x
Google API credentials
Instagram account credentials
Installation
Clone the repository:
bash
Copy code
git clone https://github.com/zeldonzoom/auto-insta-reels-yt-channel.git
cd auto-insta-reels-yt-channel
Install required packages:
bash
Copy code
pip install moviepy
pip install pyttsx3
pip install instaloader
pip install instalooter
pip install google-auth-oauthlib
pip install google-api-python-client
Set up Google API credentials:
Create a project in Google Cloud Console
Enable YouTube Data API v3
Download client secret file and rename it to client_secret.json
Configuration
Update Instagram credentials in VideoScrape.py:
python
Copy code
L.login('your_username', 'your_password')
Configure YouTube upload settings in setup_google.py:
python
Copy code
request_body={
    'snippet':{
        'categoryId': 23,
        'title': 'Your Video Title',
        'description': 'Your Description',
        'tags': ['your', 'tags']
    }
}
Usage
Run the video scraper:
bash
Copy code
python VideoScrape.py
Compile videos:
bash
Copy code
python Compiler.py
Upload to YouTube:
bash
Copy code
python setup_google.py
How It Works
Video Scraping: The script logs into Instagram and downloads recent videos from profiles you follow
Compilation: Videos are randomly shuffled and concatenated with an intro video
Upload: The final video is automatically uploaded to YouTube with specified metadata
File Structure
VideoScrape.py: Instagram video scraping functionality
Compiler.py: Video compilation and processing
Google.py: Google API authentication handler
setup_google.py: YouTube upload configuration
Uploader.py: YouTube upload functionality
Security Note
Never commit your credentials or API keys
Use environment variables for sensitive information
Keep your token_youtube_v3.pickle file secure
Contributing
Fork the repository
Create your feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request
License
This project is licensed under the MIT License - see the LICENSE file for details

Disclaimer
This tool should be used responsibly and in accordance with Instagram's and YouTube's terms of service and API usage guidelines.

Created and maintained by zeldonzoom
