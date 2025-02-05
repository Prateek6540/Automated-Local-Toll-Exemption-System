
import string
import easyocr
import cv2
import numpy as np

reader = easyocr.Reader(['en'],gpu=True)
dict_char_to_int = {'O': '0',
                    'I': '1',
                    'J': '3',
                    'A': '4',
                    'G': '6',
                    'S': '5',
                    'Z': '2',
                    'L': '4'}

dict_int_to_char = {'0': 'O',
                    '1': 'I',
                    '3': 'J',
                    '4': 'A',
                    '6': 'G',
                    '5': 'S',
                    '2' : 'Z'}
# import string
# import re
#
# # Dictionary mappings for character corrections
# dict_char_to_int = {'O': '0', 'I': '1', 'J': '3', 'A': '4', 'G': '6', 'S': '5'}
# dict_int_to_char = {'0': 'O', '1': 'I', '3': 'J', '4': 'A', '6': 'G', '5': 'S'}
#
# # List of valid state codes in India
# valid_state_codes = [
#     'AP', 'AR', 'AS', 'BR', 'CG', 'GA', 'GJ', 'HR', 'HP', 'JH', 'KA', 'KL',
#     'MP', 'MH', 'MN', 'ML', 'MZ', 'NL', 'OD', 'PB', 'RJ', 'SK', 'TN', 'TS',
#     'TR', 'UP', 'UK', 'WB'
# ]
#
# # Function to apply character corrections using the mapping dictionaries
# def apply_mappings(text):
#     corrected_text = ''
#     for i, char in enumerate(text):
#         # Check if character needs to be converted from dict_char_to_int or dict_int_to_char
#         if char in dict_char_to_int:
#             corrected_text += dict_char_to_int[char]
#         elif char in dict_int_to_char:
#             corrected_text += dict_int_to_char[char]
#         else:
#             corrected_text += char
#     return corrected_text
#
# # Function to check if the license plate format is valid based on state codes and patterns
# def license_format(text):
#     # Apply character mappings to correct common OCR errors
#     text = apply_mappings(text)
#
#     # Check if the first two characters are valid state codes
#     state_code = text[:2]
#     if state_code not in valid_state_codes:
#         return False
#
#     # Define the valid patterns for Indian license plates with last four digits constraint
#     patterns = [
#         r'^[A-Z]{2}\d{2}[A-Z]{2}\d{4}$',  # Format: KA47VW1234 (state + rto + series + 4-digit number)
#         r'^[A-Z]{2}\d{2}[A-Z]{1}\d{4}$',  # Format: KA47V1234 (state + rto + series + 4-digit number)
#         r'^[A-Z]{2}\d{2}\d{4}$',          # Format: KA471234 (state + rto + 4-digit number)
#     ]
#
#     # Check against all patterns
#     for pattern in patterns:
#         if re.match(pattern, text):
#             return True
#
#     return False
#
# # Function to format the license plate text based on dictionary mappings and patterns
# def format_license(text):
#     if len(text) < 6:
#         return text  # Return original if not enough characters
#
#     # Apply character mappings to correct common OCR errors
#     license_plate_ = apply_mappings(text)
#
#     # Ensure the first two characters are a valid state code
#     state_code = license_plate_[:2]
#     if state_code not in valid_state_codes:
#         return text  # Return original if not a valid state code
#
#     return license_plate_



# Example usage


# def license_format(text):
#
#     if len(text) != 7:
#         return False
#
#     if (text[0] in string.ascii_uppercase or text[0] in dict_int_to_char.keys()) and \
#        (text[1] in string.ascii_uppercase or text[1] in dict_int_to_char.keys()) and \
#        (text[2] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[2] in dict_char_to_int.keys()) and \
#        (text[3] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[3] in dict_char_to_int.keys()) and \
#        (text[4] in string.ascii_uppercase or text[4] in dict_int_to_char.keys()) and \
#        (text[5] in string.ascii_uppercase or text[5] in dict_int_to_char.keys()) and \
#        (text[6] in string.ascii_uppercase or text[6] in dict_int_to_char.keys()):
#         return True
#     else:
#         return False

def license_format(text):
    if len(text) < 8:
          return False

    if len(text) == 8:

        if (text[0] in string.ascii_uppercase) and \
           (text[1] in string.ascii_uppercase) and \
           ((text[2] in string.digits)) and \
           ((text[3] in string.digits)) and \
           ((text[4] in string.digits)) and \
           ((text[5] in string.digits)) and \
           ((text[6] in string.digits)) and \
           ((text[7] in string.digits) ):
            return True
        else:
            return False
    if len(text) == 9 :
        if (text[0] in string.ascii_uppercase) and \
           (text[1] in string.ascii_uppercase) and \
           ((text[2] in string.digits)) and \
           ((text[3] in string.digits)) and \
           ((text[4] in string.ascii_uppercase)) and \
           ((text[5] in string.digits) or (text[5] in string.ascii_uppercase)) and \
           ((text[6] in string.digits) or (text[6] in string.ascii_uppercase)) and \
           ((text[7] in string.digits)) and \
           ((text[8] in string.digits)):
            return True
        else:
            return False
    else:
        if (text[0] in string.ascii_uppercase) and \
           (text[1] in string.ascii_uppercase) and \
           ((text[2] in string.digits)) and \
           ((text[3] in string.digits)) and \
           ((text[4] in string.ascii_uppercase)) and \
           ((text[5] in string.ascii_uppercase)) and \
           ((text[6] in string.digits) ) and \
           ((text[7] in string.digits)) and \
           ((text[8] in string.digits)) and \
           ((text[9] in string.digits)):
            return True
        else:
            return False



#
def format_license(text):
    if len(text) < 8:
        return text
    license_plate_ = ''
    mapping8 = {0: dict_int_to_char, 1: dict_int_to_char, 4: dict_char_to_int, 5: dict_char_to_int, 6: dict_char_to_int,
               2: dict_char_to_int, 3: dict_char_to_int, 7:dict_char_to_int}
    mapping9 = {0: dict_int_to_char, 1: dict_int_to_char, 4: dict_int_to_char, 5: dict_char_to_int, 6: dict_char_to_int,
                2: dict_char_to_int, 3: dict_char_to_int, 7: dict_char_to_int,8:dict_char_to_int}
    mapping10 = {0: dict_int_to_char, 1: dict_int_to_char, 4: dict_int_to_char, 5: dict_int_to_char, 6: dict_char_to_int,
                2: dict_char_to_int, 3: dict_char_to_int, 7: dict_char_to_int,8:dict_char_to_int, 9:dict_char_to_int}

    if len(text) == 8:
        for j in [0, 1, 2, 3, 4, 5, 6,7]:
            if text[j] in mapping8[j].keys():
                license_plate_ += mapping8[j][text[j]]
            else:
                license_plate_ += text[j]

        return license_plate_
    elif len(text) ==9:
        for j in [0, 1, 2, 3, 4, 5, 6,7,8]:
            if text[j] in mapping9[j].keys():
                license_plate_ += mapping9[j][text[j]]
            else:
                license_plate_ += text[j]
        return license_plate_

    else:
        for j in [0, 1, 2, 3, 4, 5, 6,7,8,9]:
            if text[j] in mapping10[j].keys():
                license_plate_ += mapping10[j][text[j]]
            else:
                license_plate_ += text[j]
        return license_plate_




def get_car(plates,track_ids):
    x1, y1, x2, y2, conf, cls = plates
    found = False
    for j in range(len(track_ids)):
        xcar1, ycar1, xcar2, ycar2, carid =track_ids[j]
        if x1>xcar1 and y1>ycar1 and x2<xcar2 and y2<ycar2:
            found = True
            ID = j
            break

    if found:
        return track_ids[ID]
    return -1,-1,-1,-1,-1





    return 0,0,0,0,0
def preprocess_plate(cropedplate):
    # Convert to grayscale
    cropedplategray = cv2.cvtColor(cropedplate, cv2.COLOR_BGR2GRAY)

    # Increase contrast and brightness
    alpha = 1.5  # Contrast control (1.0-3.0)
    beta = 30    # Brightness control (0-100)
    enhanced_plate = cv2.convertScaleAbs(cropedplategray, alpha=alpha, beta=beta)

    # Adaptive thresholding
    cropedplatetresh = cv2.adaptiveThreshold(
        enhanced_plate, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV, 11, 2
    )

    # Apply morphological operations
    kernel = np.ones((3, 3), np.uint8)
    cropedplatetresh = cv2.morphologyEx(cropedplatetresh, cv2.MORPH_CLOSE, kernel)

    # Denoise the image
    cropedplate_denoised = cv2.fastNlMeansDenoising(cropedplatetresh, None, 30, 7, 21)

    return cropedplate_denoised
def read_license_plate(img):
    detections = reader.readtext(img)
    for detection in detections:
        bbox,text,score = detection
        text=text.upper().replace(' ','')
        # print(format_license(text))
        # Print the length of the text before slicing
        print("Iam here")
        print('text')
        print(f"Original Text: {text}, Length: {len(text)}")

        # Trim the text to 10 characters if it's longer than 10
        if len(text) > 10:
            text = text[:10]

        # Print the text after slicing to verify
        # print(f"Sliced Text: {text}, Length: {len(text)}")
        text = format_license(text)
        print(text)
        if text[1]=='H':
            text = 'M' + text[1:]
        if license_format(text):
            return format_license(text),score
        # if True:
        #     return format_license(text),score


    return None,None


