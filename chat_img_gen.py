# -*- coding: UTF-8 -*-

import sys

try:
    from PIL import Image, ImageFont, ImageDraw
except ImportError:
    import sys
    print >> sys.stderr, "Error importing Pillow, try to use `pip install Pillow` to install it"


RESULT_PATH = "./result.jpg"

msg_font = ImageFont.truetype('./HiraginoSans_W4.ttf', 31)
anchor_text = "good suggestion"

# text width of anchor_text in HiraginoSans W4, 31 size.
anchor_text_size = 252
# (x, y) = image_editable.textsize(msg, font=msg_font)
# print(image_editable.textsize(msg, font=msg_font))

my_image = Image.open("Template.jpg")
# Size of the image: 476 x 138
left_margin_len = 220
right_margin_len = 55


def extend(pil_img, delta_in_pixel):
    pad_len = 40

    width, height = pil_img.size
    new_width = width + delta_in_pixel
    result = Image.new(pil_img.mode, (new_width, height), 0)
    result.paste(pil_img, (0, 0))

    right_part = result.crop((width - right_margin_len, 0, width, height))
    right_part_lt = width - right_margin_len + delta_in_pixel
    result.paste(right_part, (right_part_lt, 0, width + delta_in_pixel, height))

    current_lt = left_margin_len
    end_lt = new_width - right_margin_len
    while current_lt < end_lt:
        current_len = min(end_lt - current_lt, pad_len)
        pad = pil_img.crop((left_margin_len, 0, left_margin_len + current_len, height))

        print("Padding:", (current_lt, 0, current_lt + current_len, height))
        result.paste(pad, (current_lt, 0, current_lt + current_len, height))
        current_lt = current_lt + current_len

    return result


def shrink(pil_img, delta_in_pixel):
    width, height = pil_img.size
    new_width = width - delta_in_pixel

    if new_width <= left_margin_len + right_margin_len:
        raise Exception("Cannot generate image for a small new_width: %d" % new_width)

    result = Image.new(pil_img.mode, (new_width, height), 0)

    left_part = pil_img.crop((0, 0, width - right_margin_len - delta_in_pixel, height))
    result.paste(left_part, (0, 0))
    right_part = pil_img.crop((width - right_margin_len, 0, width, height))
    result.paste(right_part, (new_width - right_margin_len, 0))

    return result


def generate_result(msg):
    x = ImageDraw.Draw(my_image).textsize(msg, font=msg_font)[0]
    print("Message", msg, ", message width:", x)

    if x >= anchor_text_size:
        img = extend(my_image, x - anchor_text_size)
    else:
        img = shrink(my_image, anchor_text_size - x)

    image_editable = ImageDraw.Draw(img)
    image_editable.text((155, 70), msg, (48, 48, 48), font=msg_font)

    img.save(RESULT_PATH)


if __name__ == '__main__':
    generate_result('你觉得这河里吗')
