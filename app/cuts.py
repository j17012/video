import cv2
import os
from os.path import splitext, dirname, basename, join
from .models import UploadFile, UploadImage

#保存する画像の名前と拡張子
def save_frames(video_path, frame_dir, 
                name="image", ext="jpg"):

    print(video_path)
    print(frame_dir)

    #動画ファイルを読み込む
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        return
    v_name = splitext(basename(video_path))[0]
    if frame_dir[-1:] == "\\" or frame_dir[-1:] == "/":
        frame_dir = dirname(frame_dir)
    frame_dir_ = join(frame_dir, v_name)
    
    base_path = join(frame_dir_, name) #出力先ディレクトリとファイル名を結合

    idx = 0
    while cap.isOpened():
        idx += 1
        ret, frame = cap.read()
        if ret:
            if cap.get(cv2.CAP_PROP_POS_FRAMES) == 1:  # 0秒のフレームを保存
                cv2.imwrite("{}_{}.{}".format(base_path, "0000", ext),
                            frame)
            elif idx < cap.get(cv2.CAP_PROP_FPS):
                continue
            else:  # 1秒ずつフレームを保存
                second = int(cap.get(cv2.CAP_PROP_POS_FRAMES)/idx)
                filled_second = str(second).zfill(4)
                #　ディレクトリに画像を保存
                cv2.imwrite("{}_{}.{}".format(base_path, filled_second, ext),
                            frame)
                idx = 0
        else:
            break