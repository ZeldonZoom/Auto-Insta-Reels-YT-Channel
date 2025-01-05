# Auto-Insta-Reels-YT-Channel  
An automated solution for scraping Instagram reels and compiling them into YouTube videos with automated uploads.  

## Features  
- 🎥 Automatically scrapes video content from Instagram profiles you follow  
- 🔄 Compiles multiple video clips into a single video  
- 🎬 Adds intro video to compiled content  
- 📤 Automated YouTube upload functionality  
- 🔐 Secure Google OAuth2.0 authentication  
- 🎯 Customizable video upload settings  

## Prerequisites  
- Python 3.x  
- Google API credentials  
- Instagram account credentials  

## Installation  

### Clone the repository:  
```bash  
git clone https://github.com/zeldonzoom/auto-insta-reels-yt-channel.git  
cd auto-insta-reels-yt-channel
```
### Install required packages:
```bash
pip install moviepy  
pip install pyttsx3  
pip install instaloader  
pip install instalooter  
pip install google-auth-oauthlib  
pip install google-api-python-client  
```

### Set up Google API credentials:
1. Create a project in Google Cloud Console
2. Enable YouTube Data API v3
3. Download the client secret file and rename it to `client_secret.json`

## Configuration
### Update Instagram credentials in `VideoScrape.py`:
```bash
L.login('your_username', 'your_password')
```
### onfigure YouTube upload settings in `setup_google.py`:
```bash
request_body = {  
    'snippet': {  
        'categoryId': 23,  
        'title': 'Your Video Title',  
        'description': 'Your Description',  
        'tags': ['your', 'tags']  
    }  
}  
```

## Usage
### Run the video scraper:
```bash
python VideoScrape.py
```
### Compile videos:
```bash
python Compiler.py
```
### Upload to YouTube:
```bash
python setup_google.py
```

## How It Works
**Video Scraping**: The script logs into Instagram and downloads recent videos from profiles you follow.
**Compilation**: Videos are randomly shuffled and concatenated with an intro video.
**Upload**: The final video is automatically uploaded to YouTube with specified metadata.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer
This tool should be used responsibly and in accordance with Instagram's and YouTube's terms of service and API usage guidelines.

## Acknowledgments
This project was inspired by ["Making A Fully Automated Youtube Channel With Computer Science"](https://youtu.be/O-6kbagEmKA?si=VOR8SaLl4usf6WeW) by *nang* and the corresponding GitHub repository created by [nang-dev/automated_youtube_channel](https://github.com/nang-dev/automated_youtube_channel). Their work served as a foundation and provided valuable insights for developing this solution.
