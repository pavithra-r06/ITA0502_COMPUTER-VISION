import cv2, sys
path = sys.argv[1] if len(sys.argv) > 1 else "video.mp4"
cap = cv2.VideoCapture(path)
if not cap.isOpened(): raise SystemExit("Video not found or cannot be opened.")
frames = []
while True:
    ok, frame = cap.read()
    if not ok: break
    frames.append(frame)
cap.release()
if not frames: raise SystemExit("No frames found.")
fps = 25
writer = cv2.VideoWriter("reverse_video.mp4", cv2.VideoWriter_fourcc(*"mp4v"), fps,
                         (frames[0].shape[1], frames[0].shape[0]))
for frame in reversed(frames):
    writer.write(frame)
    cv2.imshow("Reverse video (press q to stop)", frame)
    if cv2.waitKey(max(1, int(1000/fps))) & 0xFF == ord("q"): break
writer.release(); cv2.destroyAllWindows()
