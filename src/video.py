class Video:
    """
    Класс Video представляет видео с заданными атрибутами.

    Attributes:
        video_id (str): Уникальный идентификатор видео.
        title (str): Название видео.
        url (str): Ссылка на видео.
        views (int): Количество просмотров видео (по умолчанию 0).
        likes (int): Количество лайков видео (по умолчанию 0).
    """

    def __init__(self, video_id, title='', url='', views=0, likes=0):
        """
        Инициализирует экземпляр класса Video с заданными атрибутами.

        Args:
            video_id (str): Уникальный идентификатор видео.
            title (str, optional): Название видео. По умолчанию пустая строка.
            url (str, optional): Ссылка на видео. По умолчанию пустая строка.
            views (int, optional): Количество просмотров видео. По умолчанию 0.
            likes (int, optional): Количество лайков видео. По умолчанию 0.
        """
        self.video_id = video_id
        self.title = title
        self.url = url
        self.views = views
        self.likes = likes

    def __str__(self):
        """
        Возвращает строковое представление объекта Video (название видео).

        Returns:
            str: Название видео.
        """
        return self.title


class PLVideo(Video):
    """
    Класс PLVideo представляет видео, связанное с определенным плейлистом.

    Attributes:
        playlist_id (str): Уникальный идентификатор плейлиста, к которому принадлежит видео.
    """

    def __init__(self, video_id, playlist_id, title='', url='', views=0, likes=0):
        """
        Инициализирует экземпляр класса PLVideo с заданными атрибутами.

        Args:
            video_id (str): Уникальный идентификатор видео.
            playlist_id (str): Уникальный идентификатор плейлиста.
            title (str, optional): Название видео. По умолчанию пустая строка.
            url (str, optional): Ссылка на видео. По умолчанию пустая строка.
            views (int, optional): Количество просмотров видео. По умолчанию 0.
            likes (int, optional): Количество лайков видео. По умолчанию 0.
        """
        super().__init__(video_id, title, url, views, likes)
        self.playlist_id = playlist_id