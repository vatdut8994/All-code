import face_recognition

bill_gates = face_recognition.load_image_file('./img/known/Me.jpg')
face_encoding = face_recognition.face_encodings(bill_gates)[0]

unknown = face_recognition.load_image_file('../me.jpg')
unknown_face_encoding = face_recognition.face_encodings(unknown)[0]

results = face_recognition.compare_faces([face_encoding], unknown_face_encoding)

if results[0]:
    print("This is you")
else:
    print('This is not you')
