from TikTokApi import TikTokApi

def download_tiktok_video(video_url):
    try:
        # Создание экземпляра TikTokApi
        api = TikTokApi()
        
        # Извлечение идентификатора видео из ссылки
        video_id = api.get_video_id(video_url)
        
        # Получение данных о видео
        video_data = api.get_video_by_id(video_id)
        
        # Получение ссылки на скачивание видео
        video_download_url = video_data['itemInfo']['itemStruct']['video']['downloadAddr']
        
        return video_download_url

    except Exception as e:
        print(f"Error while getting video URL: {str(e)}")

    return None
