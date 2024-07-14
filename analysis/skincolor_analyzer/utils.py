from PIL import Image

def analyze_skin_tone(image_path):
    image = Image.open(image_path)
    pixels = list(image.getdata())
    r, g, b = zip(*pixels)
    avg_r = sum(r) / len(r)
    avg_g = sum(g) / len(g)
    avg_b = sum(b) / len(b)
    avg_hex = '#%02x%02x%02x' % (int(avg_r), int(avg_g), int(avg_b))

    # Simple categorization based on average hex value (customize as needed)
    if avg_hex < '#6b4f2d':
        return 'dark'
    elif avg_hex < '#b8956d':
        return 'medium'
    elif avg_hex < '#dfb385':
        return 'light'
    else:
        return 'pale'
