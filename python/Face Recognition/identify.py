import face_recognition
from PIL import Image, ImageDraw

Papa = face_recognition.load_image_file('./img/known/Papa.jpeg')
Papa_encoding = face_recognition.face_encodings(Papa)[0]

Mommy = face_recognition.load_image_file('./img/known/Mommy.JPG')
Mommy_encoding = face_recognition.face_encodings(Mommy)[0]

Me = face_recognition.load_image_file('./img/known/Me.jpg')
My_encoding = face_recognition.face_encodings(Me)[0]

Didi = face_recognition.load_image_file('./img/known/Didi.jpg')
Didi_encoding = face_recognition.face_encodings(Didi)[0]


known_face_encodings = [
    Papa_encoding,
    Mommy_encoding,
    My_encoding,
    Didi_encoding
]

known_face_names = [
    "Manoj Kumar",
    "Geeta",
    "Vatsal Dutt",
    "Bhumika Dutt"
]

test_image = face_recognition.load_image_file('./img/groups/Diwali me and papa.jpg')

face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)

pil_image = Image.fromarray(test_image)

draw = ImageDraw.Draw(pil_image)

for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

    name = "Unknown Person"

    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]

    draw.rectangle(((left, top - 10,), (right, bottom)), outline=(255, 255, 255))
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom + text_height + 10), (right, bottom)), fill=(0, 0, 0), outline=(0, 0, 0))
    draw.text((left + 6, bottom + text_height - 5), name, fill=(255, 255, 255, 255))

del draw

pil_image.show()
