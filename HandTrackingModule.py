from mediapipe.python.solutions.hands import (
    Hands as _genHandsCLS,
    HAND_CONNECTIONS,
    HandLandmark,
)
from mediapipe.python.solutions.drawing_utils import draw_landmarks
import cv2


# from time import time
# def drawFPS(img, pTime: float) -> float:
#     cTime = time()
#     fps = int(1 / (cTime - pTime))
#     pTime = cTime

#     cv2.putText(
#         img, f"FPS: {fps}", (400, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3
#     )
#     return pTime


class HandDetector:
    def __init__(
        self,
        mode=False,
        maxHands=2,
        modelComplexity=1,
        minDetectionCon=0.5,
        minTrackingCon=0.5,
    ):
        self.hands = _genHandsCLS(
            mode,
            maxHands,
            modelComplexity,
            minDetectionCon,
            minTrackingCon,
        )

    def findHands(self, img, draw=True, HAND_CONNECTIONS=HAND_CONNECTIONS):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    draw_landmarks(img, handLms, HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo=0, draw=True):
        lmList = []

        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]

            for id, lm in enumerate(myHand.landmark):
                h, w, _ = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)

                lmList.append([id, cx, cy])

                if draw:
                    cv2.putText(
                        img,
                        f"{id}",
                        (cx, cy - 5),
                        cv2.FONT_HERSHEY_PLAIN,
                        1,
                        (255, 0, 0),
                        1,
                    )
        return lmList


def main():
    cap = cv2.VideoCapture(0)

    detector = HandDetector()

    pTime = 0

    while True:
        _, img = cap.read()
        img = detector.findHands(img)
        detector.findPosition(img)

        # pTime = drawFPS(img, pTime)

        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
