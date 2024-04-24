import streamlit as st
from googleapiclient.discovery import build

# YouTube API
youtube_api_key = 'API KEY HERE'
youtube = build('youtube', 'v3', developerKey=youtube_api_key)

# Country codes for the five countries
country_codes = {
    'India': 'IN',
    'Australia': 'AU',
    'USA': 'US',
    'UK': 'GB',
    'China': 'CN'
}

# Mapping of category names to category IDs
categories = {
    'Film & Animation': 1,
    'Autos & Vehicles': 2,
    'Music': 10,
    'Pets & Animals': 15,
    'Sports': 17,
    'Short Movies': 18,
    'Travel & Events': 19,
    'Gaming': 20,
    'Videoblogging': 21,
    'People & Blogs': 22,
    'Comedy': 23,
    'Entertainment': 24,
    'News & Politics': 25,
    'Howto & Style': 26,
    'Education': 27,
    'Science & Technology': 28,
    'Nonprofits & Activism': 29,
    'Movies': 30,
    'Anime/Animation': 31,
    'Action/Adventure': 32,
    'Classics': 33,
    'Documentary': 35,
    'Drama': 36,
    'Family': 37,
    'Foreign': 38,
    'Horror': 39,
    'Sci-Fi/Fantasy': 40,
    'Thriller': 41,
    'Shorts': 42,
    'Shows': 43,
    'Trailers': 44
}

# Function to fetch top trending videos and hashtags for a given country and category
def fetch_trending_videos(country_code, category_id):
    youtube_response = youtube.videos().list(
        part='snippet',
        chart='mostPopular',
        regionCode=country_code,
        videoCategoryId=category_id,
        maxResults=10
    ).execute()

    trending_videos = []
    for video in youtube_response['items']:
        video_id = video['id']
        title = video['snippet']['title']
        hashtags = video['snippet']['tags'] if 'tags' in video['snippet'] else []
        trending_videos.append((title, video_id, hashtags))

    return trending_videos

# Streamlit app
st.title('Top Trending YouTube Videos with Hashtags')
selected_country = st.selectbox('Select a country:', list(country_codes.keys()))
selected_category = st.selectbox('Select a category:', list(categories.keys()))

country_code = country_codes[selected_country]
category_id = categories[selected_category]
trending_videos = fetch_trending_videos(country_code, category_id)

for title, video_id, hashtags in trending_videos:
    st.video(f'https://www.youtube.com/watch?v={video_id}')
    st.write('Title:', title)
    st.write('Hashtags:', ', '.join(hashtags) if hashtags else 'None')
