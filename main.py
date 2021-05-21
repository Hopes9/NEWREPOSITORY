import face_recognition

known_image = face_recognition.load_image_file("obama-480p.jpg")

unknown_image_list = [face_recognition.load_image_file("lin-manuel-miranda.png"), face_recognition.load_image_file("2.jpg"), face_recognition.load_image_file("obama.jpg")]

for i in range(len(unknown_image_list)):
  biden_encoding = face_recognition.face_encodings(known_image)[0]
  unknown_encoding = face_recognition.face_encodings(unknown_image_list[i])[0]
  print(face_recognition.compare_faces([biden_encoding], unknown_encoding))
