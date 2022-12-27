import cvlib as cv

faces, confidences = cv.detect_face("AEBC9D04-6561-4AD9-988F-55DA62408547.jpeg")

label, confidence = cv.detect_gender(face)

print(f"{label} : {confidence}")
