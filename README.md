# video

## アプリの機能  
1．動画の再生  
2．動画の分割(開発中)  
3．動画のアップロード  

## 操作手順   
git clone https://github.com/j17012/video.git  
cd video  
pip3 install -r requirements.txt
python3 manage.py migrate  
python3 manage.py runserver  
http://localhost:8000/top  

## エラーと解決策
ModuleNotFoundWrror:No module named 'skbuild'  
→pip3 install -U pip  
