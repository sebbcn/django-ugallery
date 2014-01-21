
THUMBNAIL_ALIASES = {
    '': {
        'small': dict(size=(250, 250), quality=75, crop="smart"),
        'big': dict(size=(800, 600), quality=85, crop="smart")
    },
}

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'ugallery.thumbnails.processors.scale_and_crop_with_orientation',
    'easy_thumbnails.processors.filters',
)
