from PIL import Image, ImageFilter


def expand2square(pil_img, background_color):
    width, height = pil_img.size
    if width == height:
        return pil_img
    elif width > height:
        result = Image.new(pil_img.mode, (width, width), background_color)
        result.paste(pil_img, (0, (width - height) // 2))
        return result
    else:
        result = Image.new(pil_img.mode, (height, height), background_color)
        result.paste(pil_img, ((height - width) // 2, 0))
        return result


def trim_and_resize(file_name, size):
    new_file = 'cropped_' + file_name
    im = Image.open(file_name)

    # 余白を切り出し
    cropped = im.crop(im.getbbox())
    square = expand2square(cropped, (255, 255, 255, 0)).resize(size)
    square.save(new_file, quality=95)
    return new_file


if __name__ == '__main__':
    file_path = 'standard-network-tier-512-color.png'
    new_file_path = trim_and_resize(file_path, (512, 512))
