import cvlib as cv

faces, confidences = cv.detect_face("idk.jpeg")

label, confidence = cv.detect_gender(face)

print(f"{label} : {confidence}")
