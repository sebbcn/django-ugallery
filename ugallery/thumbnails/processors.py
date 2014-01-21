
from easy_thumbnails.processors import scale_and_crop


def scale_and_crop_with_orientation(
        im, size, crop=False, upscale=False, **kwargs):
    ''' This processor change target size for portrait-oriented pictures
    ex: (800, 600) => (600, 800) '''

    source_x, source_y = im.size
    if source_x < source_y:
        vertical_size = (size[1], size[0])
        return scale_and_crop(im, vertical_size, crop, upscale, **kwargs)

    return scale_and_crop(im, size, crop, upscale, **kwargs)
